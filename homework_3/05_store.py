# -*- coding: utf-8 -*-
from pprint import pprint
# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара на складе c помощью циклов
# То есть: всего по лампам, стульям, етс.
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе
user_input = input("Введите, пожалуйста, что вас интересует: ")
good = str(user_input)

sum_price = 0
lampa_count = 0
sum_count_stols = 0
sum_stols_quantity = 0

for name in store:
    if name == '12345':
        lamps = store.get('12345')
        for lamps_p in lamps:
            lampa_count = lamps_p.get('quantity') * lamps_p.get('price')
            # print('Товара', lampa_count)
    if name == '23456':
        stols = store.get('23456')
        for stols_p in stols:
            stol_count = stols_p.get('quantity') * stols_p.get('price')
            stols_quantity = stols_p.get('quantity')
            sum_stols_quantity += stols_p.get('quantity')
            sum_count_stols += stol_count
        # print(sum_stols_quantity, sum_count_stols)

if good == 'Стул':
    print('Общая стоимость стульев составляет', lampa_count, 'рублей')
else:
    print('На складе находится', sum_stols_quantity, 'стола')
    print('Общая стоимость столов составляет', sum_count_stols, 'рублей')
