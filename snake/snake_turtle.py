import random
import time
import turtle

wn = turtle.Screen()
wn.title("Snake GAME")
wn.bgcolor("black")
wn.setup(600, 600)
wn.tracer(0)

head = turtle.Turtle()
head.shape("square")
head.color("lime")
head.penup()
head.goto(0, 0)
head.direction = "stop"

segments = []

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()

game_over = False

def go_up() :
    if head.direction != "down":
        head.direction = "up"

def go_down() :
    if head.direction != "up":
        head.direction = "down"

def go_left() :
    if head.direction != "right":
        head.direction = "left"

def go_right() :
    if head.direction != "left":
        head.direction = "right"

def mov() :
    match head.direction :
        case "up" : head.sety(head.ycor() + 20)
        case "down" : head.sety(head.ycor() - 20)
        case "left" : head.setx(head.xcor() - 20)
        case "right" : head.setx(head.xcor() + 20)

wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

while not game_over :
    wn.update()

    # 1. Collision avec les bords de l'écran
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290 :
        pen.goto(0, 0)
        pen.write(
            "GAME OVER",
            align = "center",
            font = ("Arial", 24, "bold"),
        )
        game_over = True

    # 2. Collision avec la nourriture
    if head.distance(food) < 20 :
        food.goto(
            random.randint(-14, 14) * 20,
            random.randint(-14, 14) * 20,
        )
        seg = turtle.Turtle()
        seg.shape("square")
        seg.color("green")
        seg.penup()
        segments.append(seg) # CORRECTION : On ajoute le segment au serpent !

    # 3. Déplacement du corps du serpent
    for i in range(len(segments) - 1, 0, -1) :
        segments[i].goto(
            segments[i - 1].xcor(),
            segments[i - 1].ycor(),
        )
    if segments :
        segments[0].goto(
            head.xcor(),
            head.ycor()
        )

    mov()

    # 4. Collision avec son propre corps
    for seg in segments :
        if head.distance(seg) < 20 : # CORRECTION : On passe 'seg' en argument
            pen.goto(0, 0)
            pen.write(
                "GAME OVER",
                align = "center",
                font = ("Arial", 24, "bold"),
            )
            game_over = True
            break

    time.sleep(0.1) # CORRECTION : Vitesse fluide (0.1s au lieu de 1s)

turtle.done()
