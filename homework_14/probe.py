import csv
import json
import re
from collections import defaultdict
from datetime import datetime
from decimal import Decimal, ROUND_HALF_EVEN
from pprint import pprint

field_names = ['current_location', 'current_experience', 'current_date']


# time_quest = int(re.findall(r'tm(\d{,1000000000})', path)[0])

class Action:

    def __init__(self):
        self.path = "Location_0_tm0"
        self.number_action = None
        self.currently_action = None
        self.user_action = None
        self.experience = 0
        self.remaining_time = Decimal('1234567890.0987654321')

    def run(self):
        with open("rpg.json", "r") as read_file:
            loaded_json_file = json.load(read_file)
        currently_location = loaded_json_file[self.path]
        while True:
            self.currently_action = []
            for action in currently_location:
                if isinstance(action, str):
                    self.currently_action.append(action)
                    continue
                type_in_list = list(action)
                self.currently_action.append(type_in_list[0])
            while True:
                self._log()
                time_quest = int(re.findall(r'tm(\d{,1000000000})', self.user_action)[0])
                if 'Location' in self.user_action:
                    self.path = self.user_action
                    for action in currently_location:
                        if self.user_action in action:
                            self.remaining_time -= time_quest
                            currently_location = action.get(self.user_action)
                            break
                else:
                    exp_quest = int(re.findall(r'exp(\d{,1000000000})', self.user_action)[0])
                    self.experience += exp_quest
                    self.remaining_time -= time_quest
                    self.currently_action.remove(self.user_action)
                    continue
                break




    def _log(self):
        self.number_action = 0
        print(f'{"*"*20} --- {"*"*20}\n'
              f'Вы находитесь в локации {self.path}\n'
              f'У вас {self.experience} опыта и осталось {self.remaining_time} секунд\n'
              f'Внутри вы видите:')
        for x in self.currently_action:
            print(f'            --{x}')
        print(f'Выберите действие:')
        for x in self.currently_action:
            if 'Location' in x:
                self.number_action += 1
                print(f'{self.number_action} -- Войти в {x}')
                continue
            else:
                self.number_action += 1
                print(f'{self.number_action} -- Атаковать {x}')
                continue
        self.number_action += 1
        print(f'{self.number_action} -- Выход')
        self._user_input()
        while self.N_A not in range(1, self.number_action + 1):
            self._user_input()
        else:
            if self.N_A in range(1, self.number_action):
                self.user_action = self.currently_action[self.N_A-1]
            else:
                print('Игра закончена')
                raise SystemExit

    def _user_input(self):

        user_action = input('Введите действие:')
        if user_action.isdigit():
            self.N_A = int(user_action)
        else:
            self._user_input()


game = Action()

game.run()