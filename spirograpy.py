""" Drawing and saving a spirograph """

import math
import random
from datetime import datetime
from turtle import Turtle


def get_color():
    """ Return random color from list """
    return random.choice(['red', 'green', 'blue', 'violet', 'orange', 'black'])


def spirography(turtle: Turtle, stat_rad: float, move_rad: float, distance: float, angle_step: int):
    '''
        stat_rad — радиус неподвижной окружности;
        move_rad — радиус окружности, катящейся по внутренней стороне другой окружности;
        distance — расстояние от центра катящейся окружности до точки
        angle_step - шаг поворота в град
    '''
    turtle.penup()
    one = 10
    stat_rad = one * stat_rad
    move_rad = one * move_rad
    distance = one * distance
    diff = stat_rad - move_rad
    pos_x = diff * math.cos(0) + distance * math.cos(0)
    pos_y = diff * math.sin(0) + distance * math.sin(0)
    turtle.setpos(pos_x, pos_y)
    start_position = turtle.pos()
    is_run = True
    angle = 0
    turtle.pendown()
    while is_run:
        rad = math.radians(angle)
        pos_x = diff * math.cos(rad) + distance * math.cos(diff/move_rad * rad)
        pos_y = diff * math.sin(rad) - distance * math.sin(diff/move_rad * rad)
        turtle.setpos(pos_x, pos_y)
        if angle > 360 and turtle.distance(start_position) < 1:
            is_run = False
        angle += angle_step


def get_name(stat_rad: float, move_rad: float, distance: float):
    """ Creating a name from params and current datetime """
    #FIXME: correct format
    date_str = datetime.today().isoformat()
    return f"R{stat_rad}.r{move_rad}.d{distance}.{date_str}"


def save(turtle, file_name: str):
    """ Saving turtle screen to file_name.eps """
    turtle_screen = turtle.getscreen()
    turtle_screen.getcanvas().postscript(file=f"images/{file_name}.eps")
