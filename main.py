import pygame as pg
import sys
from screeninfo import get_monitors

WIDTH, HEIGHT = get_monitors()[0].width, get_monitors()[0].height
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Map")
clock = pg.time.Clock()

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False

    # Обновление

    # Рендеринг
    screen.fill(BLACK)
    # После отрисовки всего, переворачиваем экран
    pg.display.flip()

pg.quit()