import colorgram

colors = colorgram.extract('image.jpg', 42)
colors_list = []

for color in colors:
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

print(colors_list)
