# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
radius = 40
radius_eye = 5
color = sd.COLOR_RED
for _ in range(10):
        center = sd.random_point()
        eye1 = sd.get_point(center.x + 15, center.y + 10)
        eye2 = sd.get_point(center.x - 15, center.y + 10)
        smile1 = sd.get_point(center.x - 15, center.y - 15)
        smile2 = sd.get_point(center.x - 5, center.y - 25)
        smile3 = sd.get_point(center.x + 5, center.y - 25)
        smile4 = sd.get_point(center.x + 15, center.y - 15)
        sd.circle(center_position=center, radius=radius, color=color, width=3)
        sd.circle(center_position=eye1, radius=radius_eye, color=color, width=5)
        sd.circle(center_position=eye2, radius=radius_eye, color=color, width=5)
        sd.lines(point_list=(smile1, smile2, smile3, smile4), color=color, closed=False, width=2)
sd.pause()
