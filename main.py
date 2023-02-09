import pygame as pg
import sys, events
from screeninfo import get_monitors
from mapview import MapView
from pygame.sprite import Group


def run():
    # Параметры вывода
    WIDTH, HEIGHT = get_monitors()[0].width, get_monitors()[0].height
    FPS = 30
    z = 17

    # Задаем цвета
    bg_color = (0, 155, 155)

    # Создаем игру и окно
    pg.init()
    pg.mixer.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Map")
    clock = pg.time.Clock()
    maps = Group()
    events.create_matrix(screen, maps, z, (56.22846, 58.00933))

    # Цикл игры
    while True:
        clock.tick(FPS)
        events.events()
        events.update(bg_color, screen, maps)
        pg.display.flip()


run()
