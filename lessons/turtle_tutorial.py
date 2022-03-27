from turtle import Turtle, colormode, done
colormode(255)
piggie: Turtle = Turtle()


piggie.color(97, 212, 229)
piggie.begin_fill()
piggie.penup()
piggie.goto(-100, -100)
piggie.pendown()
i: int = 0
while i < 4:
    piggie.forward(200)
    piggie.left(90)
    i += 1
piggie.end_fill()

# for roof
piggie.setheading(0.0)
piggie.color(0, 0, 0)
piggie.begin_fill()
piggie.penup()
piggie.goto(0, 200)
piggie.pendown()
piggie.right(45)
piggie.forward(142)
piggie.right(135)
piggie.forward(200)
piggie.right(135)
piggie.forward(142)
piggie.end_fill()
piggie.penup()

piggie.setheading(0.0)
piggie.penup()
piggie.goto(-2, 200)
piggie.pendown
piggie.begin_fill()
piggie.color(104, 104, 104)
piggie.forward(5)
piggie.left(90)
piggie.forward(40)
piggie.left(90)
piggie.forward(5)
piggie.left(90)
piggie.forward(40)
piggie.end_fill()

piggie.setheading(0.0)
piggie.penup()
piggie.goto(-12, 220)
piggie.pendown
piggie.begin_fill()
piggie.color(104, 104, 104)
piggie.forward(25)
piggie.left(90)
piggie.forward(5)
piggie.left(90)
piggie.forward(25)
piggie.left(90)
piggie.forward(5)
piggie.end_fill()




# for window
piggie.setheading(0.0)
piggie.color(255, 255, 255)
piggie.begin_fill()
piggie.penup()
piggie.goto(-50, 20)
piggie.pendown()
piggie.circle(20)
piggie.end_fill()

piggie.setheading(0.0)
piggie.color(255, 255, 255)
piggie.begin_fill()
piggie.penup()
piggie.goto(50, 20)
piggie.pendown()
piggie.circle(20)
piggie.end_fill()

piggie.setheading(0.0)
piggie.color(221, 54, 18)
piggie.begin_fill()
piggie.penup()
piggie.goto(-25, -100)
piggie.pendown()
piggie.forward(50)
piggie.left(90)
piggie.forward(100)
piggie.left(90)
piggie.forward(50)
piggie.left(90)
piggie.forward(100)
piggie.end_fill()


piggie.setheading(0.0)
piggie.color(255, 255, 255)
piggie.begin_fill()
piggie.penup()
piggie.goto(0, 120)
piggie.pendown()
piggie.circle(20)
piggie.end_fill()

done()
