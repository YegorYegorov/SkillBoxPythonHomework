import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

sd.resolution = (1200, 800)
snowflakes = {}
snowflake_size = {'min': 10, 'max': 20}
tick = 0
y_value = 0

class Snowflake:

    def __init__(self):
        self.x = sd.random_number(0, sd.resolution[0])
        self.y = sd.random_number(sd.resolution[1] - 100, sd.resolution[1] + 100)
        self.length = sd.random_number(snowflake_size['min'], snowflake_size['max'])
        self.factor_a = sd.random_number(1, 10) / 10
        self.factor_b = sd.random_number(1, 10) / 10
        self.factor_c = sd.random_number(1, 120)

    def draw(self, color=sd.COLOR_WHITE):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point,
                     length=self.length,
                     color=color,
                     factor_a=self.factor_a,
                     factor_b=self.factor_b,
                     factor_c=self.factor_c)

    def hide(self):
        self.draw(color=sd.background_color)

    def move(self):
        self.x += sd.random_number(0, 2)
        self.y -= snowflake_size['max'] + 1 - self.length


def get_snowflakes(quantity=0):
    while len(snowflakes) <= quantity:
        snowflakes[len(snowflakes)] = Snowflake()

    for num, value in snowflakes.items():
        value.hide()
        value.move()
        value.draw()

        if value.y < y_value:
            snowflakes[num] = Snowflake()


if __name__ == '__main__':

    while True:
        tick += 1
        y_value += 0.06
        sd.start_drawing()
        if tick < 50:
            get_snowflakes(quantity=300)
        elif tick > 50:
            get_snowflakes(quantity=300)

        sd.sleep(0.04)
        sd.finish_drawing()

        if sd.user_want_exit():
            break