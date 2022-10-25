import os, time, shutil, zipfile, os.path
from pprint import pprint

path = 'D:\\Python-course\\[boominfo.ru][SkillBox] [Вадим Шандринов] Python-разработчик\\' \
       '[boominfo.ru] 9. Работа с файлами и форматированный вывод\\lesson_009'

list = []

for dirpath, dirnames, filenames in os.walk(path):
    for file in filenames:
        full_file_path = os.path.join(dirpath, file)
        secs = os.path.getmtime(full_file_path)
        file_time = time.gmtime(secs)
        time_min = time.strftime("%H:%M:%S %d-%m-%Y", file_time)
        if file_time[1] == 11:
            list.append(full_file_path)
            print(f'{file:<70} {time_min:>70}')

path_2 = list[0]
secs = os.path.getmtime(path_2)
file_time = time.gmtime(secs)
time_min = time.strftime("%H:%M:%S %d-%m-%Y", file_time)
print(path_2)
print(time_min)
# way = os.makedirs('D:\\lol')
# shutil.copy2(path_2, way, )
directory = "ihritik"

# Parent Directories
parent_dir = "D:\\"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'ihritik'
os.makedirs(path)
print("Directory '%s' created" % directory)
shutil.copy2(path_2, path)