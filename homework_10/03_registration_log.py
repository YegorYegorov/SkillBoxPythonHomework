# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def alpha(name_file):
    if not name_file.isalpha():
        raise NotNameError('***В имени содержатся буквы***')


def mail(mail_file):
    if not '@' in mail_file or not '.' in mail_file:
        raise NotEmailError('***В почте отсутствуют собака и точка***')


def age(age):
    if not 10 < age < 99:
        raise ValueError('***поле возраст НЕ является числом от 10 до 99***')


def parser():
    name_file, mail_file, age_file = line.split(' ')
    name_file = str(name_file)
    age_file = int(age_file)
    alpha(name_file=name_file)
    mail(mail_file=mail_file)
    age(age=age_file)
    with open('good_log.log', 'a', encoding='utf8') as good_log:
        good_log.write(f'{line_number} - {line}')
        good_log.write('\n')


def bad_log():
    with open('bad_log.log', 'a', encoding='utf8') as bad_log:
        bad_log.write(f'{line_number} - {line}')
        bad_log.write(f'\n{exc}\n')

print('Начинаем парсинг')
with open('registrations.txt', 'r', encoding='utf8') as ff:
    line_number = 0
    for line in ff:
        line = line[:-1]
        line_number += 1
        try:
            parser()
        except ValueError as exc:
            bad_log()
        except NotNameError as exc:
            bad_log()
        except NotEmailError as exc:
            bad_log()
print('Окончен')