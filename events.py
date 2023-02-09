import pygame, requests, sys
from random import *
from math import ceil
from mapview import MapView


def events():
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def cords_to_img(cords, z, name="map"):
    cords = ','.join(cords)
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={cords}&z={z}&l=map&size=650,450"
    response = requests.get(map_request)

    map_file = f"images/{name}.png"
    with open(map_file, 'wb') as file:
        file.write(response.content)


def update(bg_color, screen, maps):
    # Обновление экрана
    screen.fill(bg_color)
    maps.draw(screen)
    pygame.display.flip()


def create_matrix(screen, maps, z, coords):
    # Создаём матрицу, для просчёта расстояния
    params = (ceil(screen.get_width() / 650), ceil(screen.get_height() / 450))
    if params[0] % 2 == 0:
        params = (params[0] + 1, params[1])
    if params[1] % 2 == 0:
        params = (params[0], params[1] + 1)
    matrix = []
    for i in range(params[0]):
        for j in range(params[1]):
            name = f'map{i}{j}'
            rng = (ceil(params[0] / 2) - i - 1, ceil(params[1] / 2) - j - 1)
            cords_to_img([f'{coords[0]}', f'{coords[1]}'], f'{z}', name)
            view = MapView(screen, name)
            view.rect.centerx += rng[0] * 650
            view.rect.centery += rng[1] * 450
            maps.add(view)

