# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n):
        self.i, self.a, self.n, self.list = 0, 1, n, []

    def __iter__(self):
        self.i, self.a, self.list = 0, 1, []
        return self

    def __next__(self):
        checking = True
        self.i += 1
        self.a += 1
        if self.i > 1:
            if self.i >= self.n:
                raise StopIteration()
            for check in self.list:
                if self.a % check == 0:
                    checking = False
                    break
            if checking:
                self.list.append(self.a)
                return self.a
            return self.__next__()
        elif checking:
            self.list.append(self.a)
            return self.a
        else:
            self.__next__()


prime_number_iterator = PrimeNumbers(n=10000)
for number in prime_number_iterator:
    print(number)


# TODO после подтверждения части 1 преподователем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


for number in prime_numbers_generator(n=10000):
    print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
def lucky_number(n):

    for number in range(n):
        if len(str(number)) % 2 == 0:
            qu = int(len(str(number)) / 2)
            ss = str(number)[:qu]
            sum_ss = 0
            for zx in ss:
                zz = int(zx)
                sum_ss += zz
            sum_vv = 0
            vv = str(number)[qu:]
            for xz in vv:
                xx = int(xz)
                sum_vv += xx
            if sum_ss == sum_vv:
                yield number
        else:
            qu = int(len(str(number)) / 2 - 0.5)
            ss = str(number)[:qu]
            sum_ss = 0
            for zx in ss:
                zz = int(zx)
                sum_ss += zz
            sum_vv = 0
            vv = str(number)[-qu:]
            for xz in vv:
                xx = int(xz)
                sum_vv += xx
            if sum_ss == sum_vv:
                yield number








# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.



def lucky_number(number):
    number = number
    if len(str(number)) % 2 == 0:
        qu = int(len(str(number)) / 2)
        ss = str(number)[:qu]
        sum_ss = 0
        for zx in ss:
            zz = int(zx)
            sum_ss += zz
        sum_vv = 0
        vv = str(number)[qu:]
        for xz in vv:
            xx = int(xz)
            sum_vv += xx
        if sum_ss == sum_vv:
            print(number)
    else:
        qu = int(len(str(number)) / 2 - 0.5)
        ss = str(number)[:qu]
        sum_ss = 0
        for zx in ss:
            zz = int(zx)
            sum_ss += zz
        sum_vv = 0
        vv = str(number)[-qu:]
        for xz in vv:
            xx = int(xz)
            sum_vv += xx
        if sum_ss == sum_vv:
            print(number)


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


for number in prime_numbers_generator(n=100000):
    lucky_number(number)