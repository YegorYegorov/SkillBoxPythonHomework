# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.
sd.resolution = (1200, 800)


def get_polygon(n):

    def draw(point, angle, length):
        for line in range(n):
            sum_angle = 180 * (n - 2)
            v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
            v1.draw()
            point = v1.end_point
            angle += (360 / n)

    return draw


draw_triangle = get_polygon(n=3)
point = sd.get_point(600, 300)
draw_triangle(point=point, angle=13, length=200)


sd.pause()
