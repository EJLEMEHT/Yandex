import pygame as pg
from mapview import MapView
import controls
from button import Button


def run():
    # Параметры вывода
    width, height = 900, 450

    # Начальные параметры
    bg_color = (64,  68, 75)
    coords = (56.22846, 58.00933)
    z = 16

    # Создаем игру и окно
    pg.init()
    pg.display.set_caption("Map")
    font = pg.font.SysFont('Arial', 16)
    screen = pg.display.set_mode((width, height))
    mapview = MapView(screen, z, coords)
    alerts = []

    # Кнопки переключения слоёв
    layer_buttons = [
        Button(screen, 175, 25, 150, 50, font, 'Схема', mapview.change_lay_map),
        Button(screen, 175, 100, 150, 50, font, 'Спутник', mapview.change_lay_sat),
        Button(screen, 175, 175, 150, 50, font, 'Гибрид', mapview.change_lay_hybr)
    ]

    while True:
        controls.events(mapview, screen, font, alerts)
        controls.update(bg_color, screen, mapview, layer_buttons, alerts)
        pg.display.flip()


if __name__ == '__main__':
    run()
