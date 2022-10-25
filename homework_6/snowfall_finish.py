import simple_draw as sd

list_point = []
list_lenght = []
list_x = []
list_y = []
color = sd.COLOR_WHITE
list_quantity = []
list_delete_numbers = []
sugrob = 0


def create_snow(quantity):
    if len(list_delete_numbers) > 0:
        for number in range(quantity):
            x = sd.random_number(-25, 575)
            y = sd.random_number(600, 800)
            point = sd.get_point(x, y)
            lenght = sd.random_number(10, 22)
            list_x.append(x)
            list_y.append(y)
            list_point.append(point)
            list_lenght.append(lenght)
            add_quantity = list_delete_numbers[number]
            list_quantity.append(add_quantity)
    else:
        for number in range(quantity):
            x = sd.random_number(-25, 575)
            y = sd.random_number(100, 700)
            point = sd.get_point(x, y)
            lenght = sd.random_number(10, 22)
            list_x.append(x)
            list_y.append(y)
            list_point.append(point)
            list_lenght.append(lenght)
            list_quantity.append(number)

def draw_snow(color):
    list_delete_numbers.clear()
    list_quantity.sort()
    for x in list_quantity:
        sd.snowflake(center=list_point[x], length=list_lenght[x], color=color)

def step_snows():
    for new in list_quantity:
        step_x = sd.random_number(-1, 1)
        step_y = sd.random_number(1, 3)
        step_lenght = list_lenght[new] * 0.05
        new_x = list_x[new] + step_x
        new_y = list_y[new] - step_y
        new_point = sd.get_point(new_x, new_y)
        list_point.pop(new)
        list_point.insert(new, new_point)
        list_x.pop(new)
        list_x.insert(new, new_x)
        list_y.pop(new)
        list_y.insert(new, new_y)

def number_snows_fall():
    x = 0
    for y in list_y:
        if y < sugrob:
            list_delete_numbers.insert(x, x)
        x += 1

def delete_snows():
    for numbers in reversed(list_delete_numbers):
        list_y.pop(numbers)
        list_x.pop(numbers)
        list_lenght.pop(numbers)
        list_point.pop(numbers)
        list_quantity.pop(numbers)
