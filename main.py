import pygame as pg
import sys, events
from screeninfo import get_monitors
from mapview import Counter
from pygame.sprite import Group


def run():
    # Параметры вывода
    WIDTH, HEIGHT = get_monitors()[0].width, get_monitors()[0].height
    FPS = 60
    z = 16

    # Задаем цвета
    bg_color = (0, 155, 155)

    coords = (56.22846, 58.00933)

    # Создаем игру и окно
    pg.init()
    pg.mixer.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Map")
    clock = pg.time.Clock()
    maps = Group()
    counter = Counter(z)
    events.create_matrix(screen, maps, counter, coords)

    # Цикл игры
    while True:
        clock.tick(FPS)
        events.events(screen, maps, counter, coords)
        events.update(bg_color, screen, maps)
        pg.display.flip()


run()
