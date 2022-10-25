# -*- coding: utf-8 -*-

import os, time, shutil, zipfile


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
from pprint import pprint


class Sorted:

    def __init__(self, file_name):
        self.new_directory = None
        self.root_directory = None
        self.path = None
        self.file_name = file_name
        self.stat = {}
        self.list = []

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def copy(self, path, root_directory):
        self.path = path
        self.root_directory = root_directory
        # if self.file_name.endswith('.zip'):
        #     self.unzip()
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(full_file_path)
                file_time = time.gmtime(secs)
                str_year = str(file_time[0])
                str_month = str(file_time[1])
                create_way_year = os.path.join(self.root_directory, str_year)
                create_way_month = os.path.join(create_way_year, str_month)
                if os.path.isdir(create_way_year):
                    if os.path.isdir(create_way_month):
                        shutil.copy2(full_file_path, create_way_month)
                    else:
                        os.makedirs(create_way_month)
                        shutil.copy2(full_file_path, create_way_month)
                else:
                    os.makedirs(create_way_year)
                    os.makedirs(create_way_month)
                    shutil.copy2(full_file_path, create_way_month)



way = 'D:\\Python-course\\[boominfo.ru][SkillBox] [Вадим Шандринов] Python-разработчик\\' \
       '[boominfo.ru] 9. Работа с файлами и форматированный вывод\\lesson_009\\icons'

root_directory = 'D:\\Homework\\'

sort = Sorted(file_name='icons.zip')
sort.unzip()
sort.copy(path=way, root_directory=root_directory)







# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
