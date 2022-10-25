# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water():

    def __init__(self, ):
        self.content = 'Вода'

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if other == Air():
            new_element = Storm()
            return new_element
        elif other == Fire():
            new_element = Par()
            return new_element

    def __eq__(self, other):
        return self.content == other.content


class Fire():

    def __init__(self, ):
        self.content = 'Огонь'

    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if other == Water():
            new_element = Par()
            return new_element
        elif other == Air():
            new_element = Light()
            return new_element

    def __eq__(self, other):
        return self.content == other.content


class Air():

    def __init__(self, ):
        self.content = 'Воздух'

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if other == Fire():
            new_element = Light()
            return new_element
        elif other == Water():
            new_element = Storm()
            return new_element

    def __eq__(self, other):
        return self.content == other.content



class Storm():

    def __init__(self):
        self.content = None

    def __str__(self):
        return 'Шторм'

class Light():

    def __init__(self):
        self.content = None

    def __str__(self):
        return 'Молния'


class Par():

    def __init__(self):
        self.content = []

    def __str__(self):
        return 'Пар'


print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
