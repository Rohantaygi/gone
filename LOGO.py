import turtle
import time
from turtle import *

x = input('background color: ')

color = ("Red", "Blue")
turtle.bgcolor(x)

begin_fill()

while True:
    a = input('function: ')
    b = int(input('value: '))
    if a == 'FT':
        forward(b) 
    if a == 'RT':
        right(b)
    if a == 'LT':
        left(b)
    if a == 'BT':
        backward(b)
    if a == 'quit':
        break
hideturtle

print('good bye!')
time.sleep(5)
