import turtle
import random
wn = turtle.Screen()
ollie = turtle.Turtle()
ollie.speed(0)
ollie.hideturtle()
wn.bgcolor("lightblue")

def draw_stars(t, size):
    t.color(colours[random.randint(0,8)])
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
        t.forward(size)
        t.left(72)
    t.up()
    t.end_fill()
    
def draw_circle(t, x, y, rad, color):
    t.up()
    t.goto(x, y)
    t.setheading(270)
    t.color(color)
    t.begin_fill()
    t.down()
    t.circle(rad)
    t.end_fill()
    
def draw_whiskers(t, a, x, y, rad):
    t.up()
    t.goto(x, y)
    t.down()
    t.color("white")
    for _ in range(4):
        t.setheading(a)
        t.circle(rad, 60)
        t.up()
        y-=40
        t.goto(x, y)
        t.down()

def draw_stripes(t, a, size, thick, color):
    t.up()
    t.color(color)
    t.pensize(thick)
    t.setheading(a)
    t.down()
    t.forward(size)

def draw_line(t, x, y, color, thick, a, size):
    t.up()
    t.color(color)
    t.goto(x, y)
    t.pensize(thick)
    t.setheading(a)
    t.down()
    t.forward(size)


def draw_triangle(t, size, a, x, y, color):
    t.up()
    t.goto(x, y)
    t.setheading(a)
    t.color(color)
    t.down()
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(360/3)
    t.end_fill()

def draw_mouth(t, x, y, a, arc, rad, color):
    t.up()
    t.goto(x, y)
    t.color(color)
    t.setheading(a)
    t.down()
    t.circle(rad, arc)

def draw_thought(t, x, y, color, rad):
    t.up()
    t.goto(x, y)
    t.color(color)
    t.down()
    t.begin_fill()
    for _ in range(2):
        t.setheading(90)
        t.circle(rad, -180)
    t.setheading(0)
    t.circle(rad, -180)
    for _ in range(2):
        t.setheading(270)
        t.circle(rad, -180)
    t.setheading(180)
    t.circle(rad, -180)
    t.end_fill()

def draw_fishies(t, color, x, y, size, height):
    t.setheading(0)
    t.up()
    t.color(color)
    t.goto(x, y)
    t.begin_fill()
    t.down()
    t.setheading(225)
    t.forward(size*1.5)
    t.setheading(90)
    t.forward(height)
    t.setheading(315)
    t.forward(size*1.5)
    t.setheading(0)
    t.circle(height/1.75, 180)
    t.end_fill()
    t.up()
    t.goto(x+15, y-height/2)
    t.dot(5, "black")



if __name__ == "__main__":
    colours = ['yellow', 'lightgreen', 'green', 'blue', 'purple', 'pink', 'red', 'violet', 'indigo']
    for _ in range(75):      #draw background of multicoloured stars
        ollie.up()
        ollie.setpos(random.randint(-600, 600), random.randint(-300, 300))
        ollie.down()
        draw_stars(ollie, 15)

    draw_circle(ollie, -250, 0, 250, "orange")    #draw head shape
    for _ in range(30):                           #draw fur stripes on head
        ollie.up()
        ollie.setpos(random.randint(-200, 160), random.randint(-200, 160))
        ollie.down()
        draw_stripes(ollie, 0, random.randint(20, 50), 15, "darkorange" )

    draw_circle(ollie, -130, 40, 30, "green")     #draw left eye
    draw_circle(ollie, 70, 40, 30, "green")      #draw right eye
    draw_line(ollie, -100, 60, "black", 10, 270, 40) #draw left pupil
    draw_line(ollie, 100, 60, "black", 10, 270, 40) #draw right pupil

    draw_triangle(ollie, 120, 20, -170, 185, "orange")  #draw left ear
    draw_triangle(ollie, 95, 20, -160, 185, "pink")
    draw_triangle(ollie, 120, 330, 110, 195, "orange") #draw right ear, slightly off-centre
    draw_triangle(ollie, 95, 330, 125, 195, "pink")

    draw_triangle(ollie, 50, 180, 25, -40, "pink")  #draw nose

    draw_mouth(ollie, 0, -85, 270, 160, 70, "brown")
    draw_mouth(ollie, -140, -85, 270, 160, 70, "brown") #draw mouth and lip
    draw_line(ollie, -25, -145, "pink", 5, 0, 50)

    draw_whiskers(ollie, 170, -210, 0, 400)    #draw whiskers on left
    draw_whiskers(ollie, 10, 210, 0, -400)   #draw whiskers on right
    ollie.up()
    x = -200
    y = 0
    for _ in range(4):        #draw freckles near whiskers
        ollie.goto(x, y)
        ollie.dot(5, "brown")
        x += 5
        y -= 40
    x = 200
    y = 0
    for _ in range(4):
        ollie.goto(x, y)
        ollie.dot(5, "brown")
        x -= 5
        y -= 40
    draw_thought(ollie, -300, 100, "white", 50)   #draw thought bubble with fish
    draw_circle(ollie, -290, 50, 20, "white")
    draw_fishies(ollie, "red", -400, 175, 50, 50)
    draw_fishies(ollie, "blue", -440, 170, 30, 30)
    draw_fishies(ollie, "green", -300, 180, 45, 45)
    

wn.mainloop()