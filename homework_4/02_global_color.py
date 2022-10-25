# -*- coding: utf-8 -*-
import simple_draw as sd
from pprint import pprint

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

sd.resolution = (1200, 600)
point = sd.get_point(300, 300)
colors = {
    '1': 'RED',
    '2': 'ORANGE',
    '3': 'YELLOW',
    '4': 'GREEN',
    '5': 'CYAN',
    '6': 'BLUE',
    '7': 'COLOR_PURPLE',
}


def triangle(point, angle, lenght):
    v1 = sd.get_vector(start_point=point, angle=angle, length=lenght, width=3)
    v1.draw(color=color_user)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=lenght, width=3)
    v2.draw(color=color_user)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=lenght, width=3)
    v3.draw(color=color_user)


print('Возможные цвета:')
pprint(colors)
color_user = int(input('Введите желаемый цвет >' ))
while color_user > 7 or color_user < 1:
    print('Неверное значение')
    color_user = int(input('Введите желаемый цвет > ' ))
else:
    if color_user == 1:
        color_user = sd.COLOR_RED
    elif color_user == 2:
        color_user = sd.COLOR_ORANGE
    elif color_user == 3:
        color_user = sd.COLOR_YELLOW
    elif color_user == 4:
        color_user = sd.COLOR_GREEN
    elif color_user == 5:
        color_user = sd.COLOR_CYAN
    elif color_user == 6:
        color_user = sd.COLOR_BLUE
    elif color_user == 7:
        color_user = sd.COLOR_PURPLE



triangle(point=point, angle=0, lenght=300)

sd.pause()
