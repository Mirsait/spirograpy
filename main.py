""" Main.py """

import turtle as t
import spirograpy as spiro
from convert_eps_png import convert_eps_to_png


t.colormode(255)
tim = t.Turtle()
tim.speed(10)
tim.hideturtle()
tim.pensize(1)


for R in range(10, 11):
    for r in range(15, 16):
        for d in range(10, 12):
            tim.pencolor(spiro.get_color())
            spiro.spirography(turtle=tim, stat_rad=R, move_rad=r, distance=d)
        filename = spiro.get_name(R, r, d)
        spiro.save(t, filename)
        tim.clear()
    tim.clear()

convert_eps_to_png()

t.exitonclick()
