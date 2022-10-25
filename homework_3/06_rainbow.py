# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)





# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
x = 50
y = 50
for color in rainbow_colors:
    start_point = sd.get_point(x=x, y=y)
    end_point = sd.get_point(x=(x+300), y=(y+400))
    x += 5
    sd.line(start_point=start_point, end_point=end_point, color=color, width=4)








radius = 150
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
for color in rainbow_colors:
    center = sd.get_point(300, -50)
    radius += 10
    sd.circle(center_position=center, radius=radius, color=color, width=10)

sd.pause()
