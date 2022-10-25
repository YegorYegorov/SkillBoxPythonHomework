# -*- coding: utf-8 -*-

# С помощью JSON файла rpg.json задана "карта" подземелья.
# Подземелье было выкопано монстрами и они всё ещё скрываются где-то в его глубинах,
# планируя набеги на близлежащие поселения.
# Само подземелье состоит из двух главных разветвлений и нескольких развилок,
# и лишь один из путей приведёт вас к главному Боссу
# и позволит предотвратить набеги и спасти мирных жителей.

# Напишите игру, в которой пользователь, с помощью консоли,
# сможет:
# 1) исследовать это подземелье:
#   -- передвижение должно осуществляться присваиванием переменной и только в одну сторону
#   -- перемещаясь из одной локации в другую, пользователь теряет время, указанное в конце названия каждой локации
# Так, перейдя в локацию Location_1_tm500 - вам необходимо будет списать со счёта 500 секунд.
# Тег, в названии локации, указывающий на время - 'tm'.
#
# 2) сражаться с монстрами:
#   -- сражение имитируется списанием со счета персонажа N-количества времени и получением N-количества опыта
#   -- опыт и время указаны в названиях монстров (после exp указано значение опыта и после tm указано время)
# Так, если в локации вы обнаружили монстра Mob_exp10_tm20 (или Boss_exp10_tm20)
# необходимо списать со счета 20 секунд и добавить 10 очков опыта.
# Теги указывающие на опыт и время - 'exp' и 'tm'.
# После того, как игра будет готова, сыграйте в неё и наберите 280 очков при положительном остатке времени.

# По мере продвижения вам так же необходимо вести журнал,
# в котором должна содержаться следующая информация:
# -- текущее положение
# -- текущее количество опыта
# -- текущая дата (отсчёт вести с первой локации с помощью datetime)
# После прохождения лабиринта, набора 280 очков опыта и проверки на остаток времени (remaining_time > 0),
# журнал необходимо записать в csv файл (назвать dungeon.csv, названия столбцов взять из field_names).

# Пример лога игры:
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 1234567890.0987654321 секунд
# Прошло уже 0:00:00
# Внутри вы видите:
# -- Монстра Mob_exp10_tm0
# -- Вход в локацию: Location_1_tm10400000
# -- Вход в локацию: Location_2_tm333000000
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Выход
import csv
import json
import re
from collections import defaultdict
from datetime import datetime
from decimal import Decimal, ROUND_HALF_EVEN
from pprint import pprint

remaining_time = Decimal('1234567890.0987654321')
# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date']
experience = 0

def log():
    N_A = 0
    number_action = 0
    print(f'Вы находитесь в локации {path}\n'
           f'У вас {experience} опыта и осталось {Decimal(remaining_time)} секунд\n'
           f'Внутри вы видите:')
    pereborka()
    print(f'Выберите действие:')
    for x in currently_action:
        if 'Mob' in x:
            number_action += 1
            print(f'{number_action} -- Атаковать {x}')
            continue
        elif 'Location' in x:
            number_action += 1
            print(f'{number_action} -- Войти в {x}')
            continue
    number_action += 1
    print(f'{number_action} -- Выход')
    while user_input() not in range(1, number_action+1):
        continue
    else:
        print(currently_action[user_input()-1])

def pereborka():

    for x in currently_action:
        print(f'            --{x}')

def user_input():

    user_action = input('Введите действие:')
    if user_action.isdigit():
        N_A = int(user_action)
        return N_A
    else:
        user_input()


with open("rpg.json", "r") as read_file:
    loaded_json_file = json.load(read_file)
path = "Location_0_tm0"
currently_location = loaded_json_file[path]


while True:
    currently_action = []
    for action in currently_location:
        if isinstance(action, str):
            currently_action.append(action)
            continue
        type_in_list = list(action)
        currently_action.append(type_in_list[0])
    log()
    while True:
        if isinstance(currently_location, dict):
            currently_location = currently_location[path]
            currently_action.pop(0)
            break
        continue



time_quest = int(re.findall(r'tm(\d{,1000000000})', path)[0])


# Учитывая время и опыт, не забывайте о точности вычислений!

