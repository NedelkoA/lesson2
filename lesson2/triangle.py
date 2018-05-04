from turtle import *
from random import shuffle

def color_rand():
    colors=['#EBBB66', '#D4EB66', '#9AEB66', '#66EB7C', '#66EBBF', '#66C9EB']
    shuffle(colors)
    return colors[0]

def triangle(large, n):
    color(color_rand())
    if n == 0:
        begin_fill()
        forward(large)
        left(120)
        forward(large)
        left(120)
        forward(large)
        left(120)
        end_fill()
    else:
        triangle(large/2, n-1)
        forward(large/2)
        triangle(large/ 2, n - 1)
        left(120)
        forward(large/2)
        right(120)
        triangle(large/2, n-1)
        right(120)
        forward(large/2)
        left(120)

speed(0)
triangle(300,3)
done()