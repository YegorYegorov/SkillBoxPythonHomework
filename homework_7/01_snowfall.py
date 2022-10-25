# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку
sd.resolution = (1200, 600)
sd.background_color = sd.COLOR_BLACK


class Snowflake:
    snow = 1

    def __init__(self):
        self.x = sd.random_number(0, 1200)
        self.y = sd.random_number(600, 800)
        self.lenght = sd.random_number(15, 25)
        self.a = sd.random_number(10, 99) / 100
        self.b = sd.random_number(10, 99) / 100
        self.c = sd.random_number(10, 170)

    def clear_previous_picture(self):
        point = sd.Point(x=self.x, y=self.y)
        sd.snowflake(center=point,
                     length=self.lenght,
                     color=sd.background_color,
                     factor_a=self.a,
                     factor_b=self.b,
                     factor_c=self.c)

    def move(self):
        if self.y < 10:
            sd.Point(x=self.x, y=self.y)
        self.y -= 60 / self.lenght
        self.x += sd.random_number(-1, 2)

    def draw(self):
        point = sd.Point(x=self.x, y=self.y)
        sd.snowflake(center=point,
                     length=self.lenght,
                     color=sd.COLOR_WHITE,
                     factor_a=self.a,
                     factor_b=self.b,
                     factor_c=self.c)

    def can_fall(self):
        if self.y < 10:
            print('Снежинка {} упала'.format(self.snow))
            self.snow += 1
            self.x = sd.random_number(0, 600)
            self.y = sd.random_number(600, 610)
            self.lenght = sd.random_number(5, 18)
            return

    def get_fallen_flakes(self):
        fallen_flakes = 0
        for x in flakes:
            if self.y < 10:
                fallen_flakes += 1
        return fallen_flakes



flake = Snowflake()
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if flake.can_fall():
#         break
#     sd.sleep(0.05)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = []
delete_flakes = []


def get_flakes(count):
    for flake in range(count):
        flake = Snowflake()
        flakes.append(flake)



def get_fallen_flakes():
    fallen_flakes = 0
    for x in flakes:
        y = getattr(x, 'y')
        if y < 10:
            delete_flakes.append(x)
            fallen_flakes += 1
    for flake in delete_flakes:
        flakes.remove(flake)
    delete_flakes.clear()
    return fallen_flakes

def append_flakes(count):
    for x in range(count):
        flake = Snowflake()
        flakes.append(flake)


N = 300
get_flakes(count=N)  # создать список снежинок
while True:
    sd.start_drawing()
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подcчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.0002)
    sd.finish_drawing()
    if sd.user_want_exit():
        break

sd.pause()
