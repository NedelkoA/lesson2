import os
import redis
from urllib.parse import urlparse
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader
from datetime import datetime


class Advertisement:
    def __init__(self, config):
        self.redis = redis.Redis(config['redis_host'], config['redis_port'])
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),
                                     autoescape=True)
        self.url_map = Map([
            Rule('/', endpoint='main'),
            Rule('/new_ad', endpoint='new_ad'),
            Rule('/ad_<ad_id>', endpoint='details'),
            Rule('/comment_<ad_id>', endpoint='add_comment')
        ])

    def ads(self):
        keys = self.redis.keys('board:*')
        keys.sort()
        count = 1
        ads_list = []
        for key in keys:
            ads_list.append((
                count,
                self.redis.get(key).decode('utf-8')
            ))
            count += 1
        return ads_list[::-1]

    def on_main(self, request):
        return self.render_template('main.html', ads=self.ads())

    def on_new_ad(self, request):
        if request.method == "POST":
            board_name = request.form['board_name']
            creator = request.form['creator']
            board_id = self.insert_ad(board_name, creator)
            return redirect('/ad_' + board_id)
        return self.render_template('create_ad.html')

    def insert_ad(self, board_name, creator):
        board = self.redis.get('board:' + board_name)
        if board is not None:
            return board
        board_num = self.redis.incr('last-board-id')
        board = base36_encode(board_num)
        self.redis.set('board:' + board, board_name)
        self.redis.set('creator:board:' + board, creator)
        self.redis.set('date:board:' + board, datetime.date(datetime.now()))
        return board

    def on_details(self, request, ad_id):
        creator = self.redis.get('creator:board:' + ad_id).decode('utf-8')
        board_name = self.redis.get('board:' + ad_id).decode('utf-8')
        date = self.redis.get('date:board:' + ad_id).decode('utf-8')
        args = {
            'creator': creator,
            'board_name': board_name,
            'ad_id': ad_id,
            'date': date
        }
        return self.render_template('details.html', args=args, comments=self.get_comments(ad_id))

    def on_add_comment(self, request, ad_id):
        if request.method == "POST":
            comment_text = request.form['comment_text']
            creator = request.form['creator']
            self.insert_comment(comment_text, creator, ad_id)
            return redirect('/ad_' + ad_id)
        return self.render_template('add_comment.html')

    def insert_comment(self, comment_text, creator, ad_id):
        comment = self.redis.get('comment:' + comment_text)
        if comment is not None:
            return comment
        comment_num = self.redis.incr('last-comment-id')
        comment = base36_encode(comment_num)
        self.redis.set('comment:' + comment, comment_text)
        self.redis.set('creator:comment:' + comment, creator)
        self.redis.lpush('comment:board:' + ad_id, comment)
        return comment

    def get_comments(self, ad_id):
        len_commets = self.redis.llen('comment:board:' + ad_id)
        comments_list = []
        keys = [
            self.redis.lindex('comment:board:' + ad_id, i).decode('utf-8')
            for i in range(len_commets)
        ]
        for key in keys:
            comments_list.append((
                self.redis.get('comment:' + key).decode('utf-8'),
                self.redis.get('creator:comment:' + key).decode('utf-8')
            ))
        return comments_list

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, 'on_' + endpoint)(request, **values)
        except HTTPException as e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def base36_encode(number):
    assert number >= 0, 'positive integer required'
    if number == 0:
        return '0'
    base36 = []
    while number != 0:
        number, i = divmod(number, 36)
        base36.append('0123456789abcdefghijklmnopqrstuvwxyz'[i])
    return ''.join(reversed(base36))


def create_app(redis_host='localhost', redis_port=6379, with_static=True):
    app = Advertisement({
        'redis_host': redis_host,
        'redis_port': redis_port
    })
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static': os.path.join(os.path.dirname(__file__), 'static')
        })
        return app


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)
