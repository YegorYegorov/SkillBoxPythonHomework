# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg
sd.resolution = (1200, 600)
point = sd.get_point(300,300)
def triangle(point, angle, lenght):
    v1 = sd.get_vector(start_point=point, angle=angle, length=lenght, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=lenght, width=3)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=lenght, width=3)
    v3.draw()

# triangle(point=point, angle=0, lenght=300)


def kvadrat(point, angle, lenght):
    v1 = sd.get_vector(start_point=point, angle=angle, length=lenght, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=lenght, width=3)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=lenght, width=3)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=lenght, width=3)
    v4.draw()

point = sd.get_point(300, 100)

# kvadrat(point=point, angle=0, lenght=200)
print('Возможные фигуры:')
figura = int(input('Введите желаемый фигуру >' ))
while figura > 2 or figura < 1:
    print('Неверное значение')
    figura = int(input('Введите желаемый фигуру > '))
else:
    if figura == 1:
        figura = triangle(point=point, angle=0, lenght=300)
    elif figura == 2:
        figura = kvadrat(point=point, angle=0, lenght=200)

sd.pause()
