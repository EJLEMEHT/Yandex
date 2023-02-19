import pygame as pg
from mapview import MapView
import controls
from button import Button
from inputs import InputBox
from location import Location


def run():
    # Параметры вывода
    width, height = 1200, 500

    # Начальные параметры
    bg_color = (64,  68, 75)
    coords = (56.22846, 58.00933)
    z = 16

    # Создаем игру и окно
    pg.init()
    pg.display.set_caption("Map")
    font = pg.font.SysFont('Arial', 16)
    screen = pg.display.set_mode((width, height))

    # Передаваемые объекты
    # Карта
    mapview = MapView(screen, z, coords)
    # Адресс
    loc = Location(screen, '', font, '#ffffff')
    # Сообщения
    alerts = []
    # Инпуты
    input_boxes = [
        InputBox(screen, 350, 300, 200, 50, '#ffffff', (150, 150, 150), font, func=mapview.search, loc=loc)
    ]

    def clear_textpt():
        mapview.delete_pt()
        loc.text = ''
    # Кнопки
    buttons = [
        # Кнопки переключения слоёв
        Button(screen, 350, 25, 200, 50, font, 'Схема', mapview.change_lay_map),
        Button(screen, 350, 100, 200, 50, font, 'Спутник', mapview.change_lay_sat),
        Button(screen, 350, 175, 200, 50, font, 'Гибрид', mapview.change_lay_hybr),

        # Кнопка искать
        Button(screen, 350, 375, 200, 50, font, 'Искать', input_boxes[0].clear_input),

        # Сброс результатов
        Button(screen, 1050, 25, 200, 50, font, 'Сброс', clear_textpt)
    ]

    while True:
        controls.events(mapview, screen, font, alerts, input_boxes)
        controls.update(bg_color, screen, mapview, buttons, alerts, input_boxes, loc)
        pg.display.flip()


if __name__ == '__main__':
    run()
