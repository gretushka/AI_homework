import time
import turtle
from itertools import cycle


class TrafficLight:
    __color = 'green'
    light_time = {
        'red': 7,
        'yellow': 2,
        'green': 4
    }

    def __init__(self, col='green', r=7, y=2, g=4):
        if col in ['red', 'yellow', 'green']:
            self.__color = col
        else:
            self.__color = 'green'
        try:
            self.light_time['red'] = int(r)
        except ValueError:
            self.light_time['red'] = 7
        try:
            self.light_time['yellow'] = int(y)
        except ValueError:
            self.light_time['yellow'] = 2
        try:
            self.light_time['green'] = int(g)
        except ValueError:
            self.light_time['green'] = 4

    def running(self, work_time=30):
        working_time = 0

        # draw a pattern
        turtle.title("Traffic Light")
        circle = turtle.Turtle()
        circle.hideturtle()
        circle.speed(11)
        circle.pensize(5)
        circle.pencolor("red")
        circle.penup()
        circle.goto(0, 100)
        circle.pendown()
        circle.circle(100)
        circle.pencolor("yellow")
        circle.penup()
        circle.goto(0, -100)
        circle.pendown()
        circle.circle(100)
        circle.pencolor("green")
        circle.penup()
        circle.goto(0, -300)
        circle.pendown()
        circle.circle(100)

        for col in cycle(self.light_time.keys()):
            if col != self.__color:
                continue

            circle.fillcolor(col)
            circle.pencolor(col)
            circle.penup()
            if col == 'green':
                circle.goto(0, -300)
                self.__color = 'red'
            elif col == 'yellow':
                circle.goto(0, -100)
                self.__color = 'green'
            else:
                circle.goto(0, 100)
                self.__color = 'yellow'
            circle.pendown()
            circle.begin_fill()
            circle.circle(100)
            circle.end_fill()

            time.sleep(self.light_time[col])
            working_time += self.light_time[col]

            circle.fillcolor('white')
            circle.begin_fill()
            circle.circle(100)
            circle.end_fill()
            if working_time >= work_time:
                break


tr = TrafficLight('yellow', 2, 1, 3)
tr.running(20)
