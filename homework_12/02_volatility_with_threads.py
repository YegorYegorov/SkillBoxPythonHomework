# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
import os
import threading
from collections import defaultdict
from operator import itemgetter
from pprint import pprint
from typing import Dict, Any

from utils import time_track


PATH = []
DICT = {}

class Volatility(threading.Thread):

    def __init__(self, path, *args, **kwargs):
        super(Volatility, self).__init__(*args, **kwargs)
        self.path = path
        self.price = []
        self.dict = {}
        self.sum_quantity = 0
        self.volatility = {}

    def run(self):
        with open(self.path, 'r', encoding='utf8') as ff:
            for line in ff:
                line = line[:-1]
                directory = line.split(',')
                if 'SECID,TRADETIME,PRICE,QUANTITY' in line: continue
                if directory[0] not in self.dict:
                    name_directory = directory[0]
                    self.dict[name_directory] = 0
                self.price.append(float(directory[2]))
                self.sum_quantity += int(directory[3])
            if len(self.price) > 1:
                print(f'Работа с {self.path}')
                self.price.sort()
                min_price = self.price.pop(0)
                max_price = self.price.pop()
                average_price = (max_price + min_price) / 2
                self.dict[name_directory] = average_price
                volatility = ((max_price - min_price) / average_price) * 100
                self.volatility[name_directory] = round(volatility, 2)
                DICT.update(self.volatility)
            else:
                print(f'Работа с {self.path}')
                self.volatility[name_directory] = 0
                DICT.update(self.volatility)




step_path = 'trades'
for file in os.listdir(step_path):
    create_path = os.path.join(step_path, file)
    PATH.append(create_path)
@time_track
def main():
    sizers = [Volatility(path=path) for path in PATH]

    for sizer in sizers:
        sizer.start()
    for sizer in sizers:
        sizer.join()

    sort = sorted(DICT.items(), key=itemgetter(1), reverse=True)
    max_vol = []
    for ticket in range(3):
        max_vol.append(sort.pop(0))

    print(f'{"*" * 15} МАКСИМАЛЬНАЯ ВОЛАТИЛЬНОСТЬ {"*" * 15}')
    for ticket, valuer in max_vol:
        print(f'{" " * 20} {ticket} --- {valuer}% {" " *  15}')


if __name__ == '__main__':
    main()
