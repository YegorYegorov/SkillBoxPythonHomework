# -*- coding: utf-8 -*-
import time
# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
from pprint import pprint


class Pereborka:

    def __init__(self, file_name):
        self.file_name = file_name
        self.dict = {}
        self.new_line = ''
        self.list = []
        self.ordered_list = []

    def read(self):
        with open(self.file_name, 'r', encoding='utf8') as file:
            for line in file:
                if 'NOK' in line:
                    self.new_line = ''
                    for char in line:
                        if char.isdigit():
                            self.new_line += str(char)
                        elif char == '-':
                            self.new_line += str(char)
                        elif char == ':':
                            self.new_line += str(char)
                        elif char == ' ':
                            self.new_line += str(char)
                        elif char == '.':
                            break
                    deadline = time.strptime(self.new_line, "%Y-%m-%d %H:%M:%S")
                    self.list.append(deadline)

    def write(self, out_file_name):
        if out_file_name is not None:
            file = open(out_file_name, 'w', encoding='utf8')
        else:
            file = None
        for new_time in self.list:
            time_min = time.strftime("%Y-%m-%d %H", new_time)
            self.ordered_list.append(time_min)
        for data in self.ordered_list:
            if data in self.dict:
                self.dict[data] += 1
            else:
                self.dict[data] = 1
        for keys, values in self.dict.items():
            file.write(keys)
            file.write('  ')
            file.write(str(values))
            file.write('\n')









# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828


perebor = Pereborka(file_name='events.txt')
time.gmtime()
perebor.read()
perebor.write(out_file_name='lol.txt')


