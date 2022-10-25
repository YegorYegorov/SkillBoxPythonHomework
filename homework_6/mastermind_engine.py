from random import randint

bulls_and_cows = {'Bulls': 0,
                  'Cows': 0}
numbers = []



def set_numbers():
    global numbers
    numbers = []
    LIST_FOR_NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    max_random = 9
    for i in range(1, 5):
        random_number = randint(0, max_random)
        add_number = LIST_FOR_NUMBERS.pop(random_number)
        numbers.append(add_number)
        max_random -= 1
    return numbers

def check_numbers(quantity):
    user_check = list(quantity)
    user_check_2 = list(map(int, user_check))
    for x in range(4):
        if numbers[x] == user_check_2[x]:
            bulls_and_cows['Bulls'] += 1
        elif user_check_2[x] in numbers:
            bulls_and_cows['Cows'] += 1
    return bulls_and_cows


def is_gameover():
    if bulls_and_cows['Bulls'] == 4:
        print('Вы выиграли')


