# -*- coding: utf-8 -*-
import time
# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

def generator(file_name):
    dict_time = {}
    last = 0
    with open(file_name, 'r', encoding='utf8') as file:
        for line in file:
            if 'NOK' in line:
                new_line = ''
                for char in line:
                    if char.isdigit():
                        new_line += str(char)
                    elif char == '-':
                        new_line += str(char)
                    elif char == ':':
                        new_line += str(char)
                    elif char == ' ':
                        new_line += str(char)
                    elif char == '.':
                        break
                deadline = time.strptime(new_line, "%Y-%m-%d %H:%M:%S")
                time_min = time.strftime("%Y-%m-%d %H:%M", deadline)
                if time_min in dict_time:
                    dict_time[time_min] += 1
                    continue
                else:
                    dict_time[time_min] = 1
                    continue
            else:
                continue
        for group_time, event_count in dict_time.items():
            yield group_time, event_count


grouped_events = generator(file_name='events.txt')
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
