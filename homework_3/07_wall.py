# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
x = 0
y = -50
yellow = sd.COLOR_RED
for z in range (20):
    if z % 2 == 0:
        x = -50
    else: x = 0
    y += 50
    for _ in range(6):
        left = sd.get_point(x, y)
        right = sd.get_point((x + 100), (y + 50))
        sd.rectangle(left_bottom=left, right_top=right, color=yellow, width=1)
        x += 100


sd.pause()
