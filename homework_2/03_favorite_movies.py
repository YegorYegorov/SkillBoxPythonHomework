#!/usr/bin/env python3

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов
my_films = 'Gay'
my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

test = my_favorite_movies.find('Терминатор')
print(test)

first = my_favorite_movies[0:10]
second = my_favorite_movies[0:10]
thirty = my_favorite_movies[0:10]
four = my_favorite_movies[0:10]


print(first)

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.
