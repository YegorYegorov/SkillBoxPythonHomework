# -*- coding: utf-8 -*-


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок (x, y)
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

import simple_draw as sd
sd.resolution = (1200, 600)
sd.background_color = sd.COLOR_BLACK
N = 40
list_x = []
list_y = []
list_l = []
list_a = []
list_c = []
list_b = []
sugrob = 15
def list_pop(V):
    list_x.pop(V - 1)
    list_y.pop(V - 1)
    list_x.insert(V - 1, sd.random_number(50, 1150))
    list_y.insert(V - 1, sd.random_number(600, 800))
    list_l.pop(V - 1)
    list_l.insert(V - 1, sd.random_number(5, 23))
    list_a.pop(V - 1)
    list_a.insert(V - 1, (sd.random_number(10, 80) / 100))
    list_b.pop(V - 1)
    list_b.insert(V - 1, (sd.random_number(10, 80) / 100))
    list_c.pop(V - 1)
    list_c.insert(V - 1, sd.random_number(10, 160))


for _ in range(N):
    x = sd.random_number(50, 1150)
    list_x.append(x)
    y = sd.random_number(100, 700)
    list_y.append(y)
    lenght = sd.random_number(5, 23)
    list_l.append(lenght)
    random_a = sd.random_number(1, 100) / 100
    list_a.append(random_a)
    random_b = sd.random_number(1, 100) / 100
    list_b.append(random_b)
    random_c = sd.random_number(1, 179)
    list_c.append(random_c)

def snow(x, y, lenght, sugrob):
    while True:
        V = 0
        sugrob += 0.01
        for _ in range(N):
            x_perem = list_x[V]
            y_perem = list_y[V]
            lenght = list_l[V]
            random_a = list_a[V]
            random_b = list_a[V]
            random_c = list_c[V]
            V += 1
            sd.start_drawing()
            point_next = sd.Point(x=x_perem, y=y_perem)
            x = x_perem
            y = y_perem
            point = point_next
            sd.snowflake(center=point,
                         length=lenght,
                         factor_a=random_a,
                         factor_b=random_b,
                         factor_c=random_c)
            if lenght > 15:
                y -= sd.random_number(1, 2)
            else:
                y -= sd.random_number(5, 8)
            x += sd.random_number(-1, 1)
            point_next = sd.Point(x=x, y=y)
            sd.snowflake(center=point,
                         length=lenght,
                         color=sd.background_color,
                         factor_a=random_a,
                         factor_b=random_b,
                         factor_c=random_c)
            sd.snowflake(center=point_next,
                         length=lenght,
                         factor_a=random_a,
                         factor_b=random_b,
                         factor_c=random_c)
            list_x.pop(V - 1)
            list_y.pop(V - 1)
            list_x.insert(V - 1, x)
            list_y.insert(V - 1, y)
            sd.finish_drawing()
            sd.sleep(0.000001)
            if y < sugrob:
                point_end = sd.Point(x=x, y=y)
                sd.start_drawing()
                sd.snowflake(center=point_end,
                             length=lenght,
                             factor_a=random_a,
                             factor_b=random_b,
                             factor_c=random_c)
                sd.finish_drawing()
                list_pop(V=V)
        if sd.user_want_exit():
            break

snow(x=list_x[0], y=list_y[0], lenght=lenght, sugrob=sugrob)
sd.pause()


# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()





# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

