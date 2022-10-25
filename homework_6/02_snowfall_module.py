# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall


from snowfall_finish import create_snow, draw_snow, step_snows, number_snows_fall, delete_snows
import snowfall_finish
color = sd.COLOR_WHITE

create_snow(quantity=100)
while True:
    sd.start_drawing()
    snowfall_finish.sugrob += 0.05
    draw_snow(color=sd.background_color)
    step_snows()
    draw_snow(color=color)
    number_snows_fall()
    if len(snowfall_finish.list_delete_numbers) > 0:
        delete_snows()
        create_snow(quantity=len(snowfall_finish.list_delete_numbers))
    sd.sleep(0.0001)
    sd.finish_drawing()
    if sd.user_want_exit():
        break
sd.pause()
