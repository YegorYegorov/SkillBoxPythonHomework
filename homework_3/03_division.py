# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ


a, b = 179, 37
# i = a
# int_div = 0
# while i >= 0:
#     i -= b
#     if i > 0:
#         int_div += 1
#         print('Целочисленное деление', a, 'на', b, 'дает', int_div)



# m = 5
# z = round(a/b, m)
# while z != int(z):
#     m -= 1
#     z = round(z, m)

intr = 4
while intr >= 0:
    f = round(a / b, intr)
    intr -= 1

print('Целочисленное деление', a, 'на', b, 'дает', f)




