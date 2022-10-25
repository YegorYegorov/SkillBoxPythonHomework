# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor


class TicketMaker:

    def __init__(self, fio, from_, to, date, template=None, font_path=None):
        self.fio = fio
        self.from_ = from_
        self.to = to
        self.date = date
        self.template = "ticket_template.png" if template is None else template
        if font_path is None:
            self.font_path = os.path.join("fonts", "ofont.ru_Gnuolane.ttf")
        else:
            self.font_path = font_path


    def make_ticket(self, out_path=None):
        im = Image.open(self.template)
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(self.font_path, size=20)

        y = im.size[1] - 10 - (10 + font.size) * 2
        message = f"{self.fio}"
        draw.text((45, 120), message, font=font, fill=ImageColor.colormap['black'])

        y = im.size[1] - 10 - (10 + font.size) * 2
        message = f"{self.from_}"
        draw.text((45, 190), message, font=font, fill=ImageColor.colormap['black'])

        y = im.size[1] - 10 - (10 + font.size) * 2
        message = f"{self.to}"
        draw.text((45, 255), message, font=font, fill=ImageColor.colormap['black'])

        y = im.size[1] - 10 - (10 + font.size) * 2
        message = f"{self.date}"
        draw.text((290, 255), message, font=font, fill=ImageColor.colormap['black'])

        # im.show()
        out_path = out_path if out_path else 'probe.png'
        im.save(out_path)
        print(f'Post card saved az {out_path}')

if __name__ == '__main__':
    ticket = TicketMaker(fio='Асланов', from_='Луна', to='Moscow', date='19.02')
    ticket.make_ticket()








# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
