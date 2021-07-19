import colorgram
import turtle as t
import random


def get_colors(image, color_count):
    image_colors = colorgram.extract(image, color_count)
    colors_list = []
    for color in image_colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        if r > 200 and g > 200 and b > 200:
            print("Color value is to white.")
        else:
            new_color = (r, g, b)
            colors_list.append(new_color)

        # new_color = tuple(color.rgb)
        # colors_list.append(new_color)

        # colors_list.append(tuple(color.rgb))

    return colors_list


def draw(color, dot_count):
    if dot_count == 1 \
            or dot_count == 11 \
            or dot_count == 21 \
            or dot_count == 31 \
            or dot_count == 41 \
            or dot_count == 51 \
            or dot_count == 61 \
            or dot_count == 71 \
            or dot_count == 81 \
            or dot_count == 91:
        myTurtle.dot(20, color)
    else:
        myTurtle.penup()
        myTurtle.forward(2)
        # myTurtle.pendown()
        myTurtle.dot(20, color)


def move_horizontal(color_list, row_count):
    dot_count = 1
    color_count = len(color_list)

    while dot_count <= 10:
        color_select = random.randint(0, color_count - 1)

        draw(color_list[color_select], dot_count)
        dot_count += 1
        if row_count == 10 and dot_count >= 10:
            myTurtle.hideturtle()




def move_vertical(colors_list):
    row_count = 1

    while row_count <= 10:
        if row_count == 1:
            move_horizontal(colors_list, row_count)
        else:
            if myTurtle.pos() >= (18.0, 0.0):
                myTurtle.penup()
                myTurtle.left(90)
                myTurtle.forward(2)
                myTurtle.left(90)
            else:
                myTurtle.penup()
                myTurtle.right(90)
                myTurtle.forward(2)
                myTurtle.right(90)
            move_horizontal(colors_list, row_count)

        row_count += 1


colors = get_colors('image.jpg', 42)
s = t.Screen()
s.colormode(255)

t.setworldcoordinates(-1, -1, 20, 20)
myTurtle = t.Turtle('turtle')

move_vertical(colors)

s.exitonclick()
