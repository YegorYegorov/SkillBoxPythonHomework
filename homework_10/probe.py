class DivisionError(Exception):

    def __init__(self, message, input_data=None):
        self.message = message
        self.input_data = input_data

    def __str__(self):
        return self.message
# Но этим лучше не злоупотреблять - ломаются все автоматические обработчики исключений.
# Ваш код может быть библиотекой, которую будут использовать другие программисты.
# И другие программисты полагаются на стандарт, не заставляйте их ковыряться в вашем коде - проклянут же.


def division(a, b):
    if a < b:
        raise DivisionError('Нельзя делить меньшее на большее', input_data=dict(a=a, b=b))
    return a/b


try:
    division(1, 2)
except DivisionError as exc:
    print(f'Поймано моё исключение {exc}, входные данные при ошибке {exc.input_data}')