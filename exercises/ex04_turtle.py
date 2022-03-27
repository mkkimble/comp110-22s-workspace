"""Drawing a mini church because that's the first thing that came to mind."""

__author__ = "730244272"

from turtle import Turtle, colormode, done
colormode(255)
piggie: Turtle = Turtle()


def main() -> None:
    """The entrypoint of my scene."""
    piggie: Turtle = Turtle()
    draw_body(piggie, -100, -100)
# Lines 28-40
    draw_roof(piggie, 0, 200)
# Lines 43-58
    draw_window(piggie, -50, 20)
# Window is lines 61-70
    draw_window(piggie, 50, 20)
# 2nd window
    draw_window(piggie, 0, 120)
# 3rd window (I was going for attic window, not quite sure if it looks like that.)
    draw_door(piggie, -25, -100)
# Lines 73-88
    draw_cross1(piggie, -2, 200)
# Lines 95-110
    draw_cross2(piggie, -12, 220)
# Lines 113-127
    done()


def draw_body(start: Turtle, x: float, y: float) -> None:
    """Drawing body of house in blue--square."""
    piggie.color(97, 212, 229)
    piggie.begin_fill()
    piggie.penup()
    piggie.goto(x, y)
    piggie.pendown()
    i: int = 0
    while i < 4:
        piggie.forward(200)
        piggie.left(90)
        i += 1
    piggie.end_fill()
    

def draw_roof(second: Turtle, z: float, w: float) -> None:
    """Drawing the roof in black--triangle."""
    piggie.setheading(0.0)
    piggie.color(0, 0, 0)
    piggie.begin_fill()
    piggie.penup()
    piggie.goto(z, w)
    piggie.pendown()
    piggie.setheading(0.0)
    piggie.right(45)
    piggie.forward(142)
    piggie.right(135)
    piggie.forward(200)
    piggie.right(135)
    piggie.forward(142)
    piggie.end_fill()


def draw_window(three: Turtle, a: float, b: float) -> None:
    """Drawing one window in white--circle."""
    piggie.setheading(0.0)
    piggie.color(255, 255, 255)
    piggie.begin_fill()
    piggie.penup()
    piggie.goto(a, b)
    piggie.pendown()
    piggie.circle(20)
    piggie.end_fill()


def draw_door(last: Turtle, c: float, d: float) -> None:
    """Drawing one window in red--rectangle."""
    piggie.setheading(0.0)
    piggie.color(221, 54, 18)
    piggie.begin_fill()
    piggie.penup()
    piggie.goto(c, d)
    piggie.pendown()
    piggie.forward(50)
    piggie.left(90)
    piggie.forward(100)
    piggie.left(90)
    piggie.forward(50)
    piggie.left(90)
    piggie.forward(100)
    piggie.end_fill()


def draw_cross1(finishing: Turtle, e: float, f: float) -> None:
    """Drawing the cross for top of building."""
    piggie.setheading(0.0)
    piggie.penup()
    piggie.goto(e, f)
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


def draw_cross2(touch: Turtle, g: float, h: float) -> None:
    """Drawing second half of the cross."""
    piggie.setheading(0.0)
    piggie.penup()
    piggie.goto(g, h)
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
  

if __name__ == "__main__":
    main()