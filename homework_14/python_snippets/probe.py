import json

with open("external_data/json_todos.json", "r") as json_file:
    list_of_tasks = json.load(json_file)
number_of_tasks = len(list_of_tasks)
print(f'Пример записи: {list_of_tasks[0]}')
