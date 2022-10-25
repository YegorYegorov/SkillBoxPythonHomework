from termcolor import cprint
from random import randint


class House:

    def __init__(self):
        self.food = 50
        self.money = 100
        self.dirt = 0
        self.food_cat = 50

    def __str__(self):
        return 'В доме {} еды, {} денег, {} грязи, {} кошачьей еды'.\
            format(self.food, self.money, self.dirt, self.food_cat)


class Human:

    def __init__(self):
        self.fullness = 30
        self.happiness = 100

    def __str__(self):
        return 'У {} осталось {} сил и счастья {}%'.format(self.name, self.fullness, self.happiness)

    def act(self):
        if self.house.dirt > 90:
            self.happiness -= 10
        elif self.happiness < 10:
            cprint('{} умер от депрессии...'.format(self.name), color='red')
            return False
        elif self.fullness < 10:
            cprint('{} умер от голода...'.format(self.name), color='red')
            return False
        return True

    def go_to_the_house(self, house):
        self.house = house
        cprint('{} вьехал в дом'.format(self.name), color='cyan')

    def eat(self):
        quantity_food = randint(30, 45)
        self.house.food -= quantity_food
        self.fullness += quantity_food
        cprint('{} съел(а) {} позиций еды'.format(self.name, quantity_food), color='green')


class Husband(Human):
    sum_money_work = 0

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return super().__str__()

    def act(self):
        self.house.dirt += 5
        if super().act():
            if self.fullness < 20:
                Human.eat(self)
            elif self.happiness < 25:
                self.gaming()
            else:
                self.work()

    def work(self):
        self.fullness -= 10
        money_work = 150
        self.house.money += money_work
        self.sum_money_work += money_work
        cprint('{} сходил на работу'.format(self.name), color='yellow')

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        cprint('{} играл весь день в танки'.format(self.name), color='yellow')


class Wife(Human):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return super().__str__()

    def act(self):
        if super().act():
            if self.fullness < 20:
                Human.eat(self)
            elif self.happiness < 25:
                self.buy_fur_coat()
            elif self.house.food < 70:
                self.shopping()
            else:
                self.clean_house()

    def shopping(self):
        quantity_shop = randint(100, 120)
        self.house.food_cat += quantity_shop
        self.house.food += quantity_shop
        self.house.money -= (quantity_shop * 2)
        self.fullness -= 10
        cprint('{} купила еды {} позиций'.format(self.name, quantity_shop), color='yellow')


    def buy_fur_coat(self):
        self.fullness -= 10
        self.house.money -= 350
        self.happiness += 60
        cprint('{} купила шубу'.format(self.name), color='yellow')

    def clean_house(self):
        quantity_clean = randint(70, 100)
        self.fullness -= 10
        self.house.dirt -= self.house.dirt
        cprint('{} убрала в квартире'.format(self.name), color='yellow')

class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30

    def __str__(self):
        return 'У {} осталось {} сил'.format(self.name, self.fullness)

    def go_to_the_house(self, house):
        self.house = house
        cprint('{} вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        dice = randint(1,2)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        else:
            self.soil()

    def eat(self):
        quantity_food = randint(20, 30)
        self.house.food_cat -= quantity_food
        self.fullness += (quantity_food * 2)
        cprint('{} съел(а) {} позиций еды'.format(self.name, quantity_food), color='green')

    def sleep(self):
        self.fullness -= 10
        cprint('{} поспал'.format(self.name), color='green')

    def soil(self):
        self.house.dirt += 10
        self.fullness -= 10
        cprint('{} подрал обои'.format(self.name), color='green')


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
murzik = Cat(name='Мурзик')
murzik.go_to_the_house(house=home)
serge.go_to_the_house(house=home)
masha.go_to_the_house(house=home)
for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(murzik, color='cyan')
    cprint(home, color='cyan')

print(serge.sum_money_work)
