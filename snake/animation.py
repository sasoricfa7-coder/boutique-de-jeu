"""
#Modèle de base 
from turtle import *
from colorsys import *

setposition(50, -50)
speed(0)
bgcolor("black")
pensize(2)
n = 100
h = 0
for i in range(120) :
    for j in range(4) :
        color(hsv_to_rgb(h, 1, 1))
        h += 0.003
        circle(40 + j * 5 , 90)
        forward(250)
        left(90)
    rt(10)
    hideturtle()
done()
"""
from turtle import *
from colorsys import *

# Affiche une image toutes les 5 étapes pour garder l'animation en mode rapide
tracer(5)

setposition(50, -50)
speed(0)
bgcolor("black")
pensize(2)
n = 100
h = 0

for i in range(120) :
    for j in range(4) :
        color(hsv_to_rgb(h, 1, 1))
        h += 0.003
        circle(40 + j * 5 , 90)
        forward(250)
        left(90)
    rt(10)
    hideturtle()

done()
