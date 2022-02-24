"""Drawing a mini house because that's the first thing that came to mind."""

__author__ = "730244272"

from turtle import Turtle, colormode, done
colormode(255)
piggie: Turtle = Turtle()


def main() -> None:
    """The entrypoint of my scene."""
    piggie: Turtle = Turtle()
    draw_body(piggie, -100, -100)
# Lines 22-34
    draw_roof(piggie, 0, 200)
# Lines 38-54
    draw_window(piggie, -50, 20)
# Window is lines 40-56
    draw_window(piggie, 50, 20)
# 2nd window
    draw_window(piggie, 0, 120)
# 3rd window (I was going for attic window, not quite sure if it looks like that.)
    draw_door(piggie, -25, -100)
# Lines 72-87
    draw_top_tree(piggie, 200, 20)
# Lines 94-107
    draw_bottom_tree(piggie, 230, -100)
# Lines 112-126
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


def draw_window(three4th: Turtle, a: float, b: float) -> None:
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


def draw_top_tree(f: float, g: float) -> None:
    """Drawing tree-top, shaded in a darker green than the line color."""
    piggie.penup()
    piggie.goto(f, g)
    piggie.pendown()
    piggie.begin_fill()
    piggie.fillcolor(67, 166, 65)
    piggie.pencolor(18, 192, 14)
    i: int = 0
    while i < 3:
        piggie.forward(100)
        piggie.left(120)
        i += 1 
    piggie.end_fill()


def draw_bottom_tree(h: float, i: float) -> None:
    """Drawing trunk of tree in brown."""
    piggie.penup()
    piggie.goto(h, i)
    piggie.pendown()
    piggie.begin_fill()
    piggie.color(130, 75, 55)
    piggie.forward(30)
    piggie.left(90)
    piggie.forward(120)
    piggie.left(90)
    piggie.forward(30)
    piggie.left(90)
    piggie.forward(120)
    piggie.end_fill()


if __name__ == "__main__":
    main()