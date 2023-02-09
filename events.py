import pygame, requests, sys
from math import ceil
from mapview import MapView


def events(screen, maps, counter, coords):
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            # Уменьшить
            if event.key == pygame.K_DOWN:
                counter.z -= 1
                create_matrix(screen, maps, counter, coords)
            # Увеличить
            elif event.key == pygame.K_UP:
                counter.z += 1
                create_matrix(screen, maps, counter, coords)


def cords_to_img(cords, counter, name="map"):
    cords = ','.join(cords)
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={cords}&z={counter.z}&l=map&size=450,450"
    response = requests.get(map_request)

    map_file = f"images/{name}.png"
    with open(map_file, 'wb') as file:
        file.write(response.content)


def update(bg_color, screen, maps):
    # Обновление экрана
    screen.fill(bg_color)
    maps.draw(screen)
    pygame.display.flip()


def create_matrix(screen, maps, counter, coords):
    # Создаём матрицу, для просчёта расстояния
    params = (ceil(screen.get_width() / 450), ceil(screen.get_height() / 450))
    if params[0] % 2 == 0:
        params = (params[0] + 1, params[1])
    if params[1] % 2 == 0:
        params = (params[0], params[1] + 1)
    for i in range(params[0]):
        for j in range(params[1]):
            name = f'map{i}{j}'
            rng = (ceil(params[0] / 2) - i - 1, ceil(params[1] / 2) - j - 1)
            cords_to_img([f'{coords[0] + rng[0] * (2 ** (8.91 + 17 - counter.z)) / (10 ** 5)}',
                          f'{coords[1] - rng[1] * (2 ** (8 + 17 - counter.z)) / (10 ** 5)}'],
                         counter, name)
            view = MapView(screen, name)
            view.rect.centerx += rng[0] * 450
            view.rect.centery += rng[1] * 450
            maps.add(view)
