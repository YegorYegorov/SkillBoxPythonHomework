# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1000, 600)

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

point_0 = sd.get_point(500, 50)
angle_0 = 90
lenght_0 = 200


def draw_branches(start_point, angle, lenght):
    if lenght < 8:
        return
    random1 = sd.random_number(70, 120) / 100
    random2 = sd.random_number(80, 120) / 100
    v1 = sd.get_vector(start_point=start_point, angle=angle + 20, length=lenght, width=3)
    v1.draw(color=sd.COLOR_PURPLE)
    v2 = sd.get_vector(start_point=start_point, angle=angle - 20, length=lenght, width=3)
    v2.draw(color=sd.COLOR_PURPLE)
    next_lenght = (lenght * (0.75 * random2))
    next_point = v1.end_point
    next_angle = (angle + (30 * random1))
    next_point2 = v2.end_point
    next_angle2 = (angle - (30 * random1))
    draw_branches(start_point=next_point, angle=next_angle, lenght=next_lenght)
    draw_branches(start_point=next_point2, angle=next_angle2, lenght=next_lenght)



draw_branches(start_point=point_0, angle=90, lenght=lenght_0)






# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви


# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()
sd.pause()


point_0 = sd.get_point(x, y)
random_lenght = sd.random_number(30, 50)
random_a = sd.random_number(10, 99) / 100
random_b = sd.random_number(10, 99) / 100
random_c = sd.random_number(30, 180)

sd.snowflake(center=point_0, length=random_lenght, factor_a=random_a, factor_b=random_b, factor_c=random_c)