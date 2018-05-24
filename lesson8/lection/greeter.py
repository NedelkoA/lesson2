from datetime import datetime
import logging

logging.basicConfig(filename='lesson8/lection/logi.log', level=logging.INFO)


class Greeter:
    def greet(self, name):
        name = name.replace(' ', '')
        name = name.title()
        date = datetime.now()
        print(date)
        logging.info(name)
        if 12 >= date.hour and 6 <= date.hour:
            return "Good morning " + name
        elif 22 > date.hour and 18 <= date.hour:
            return "Good evening " + name
        elif 6 > date.hour and 0 <= date.hour:
            return "Good night " + name
        elif 24 > date.hour and 22 <= date.hour:
            return "Good night " + name
        return "Hello " + name
