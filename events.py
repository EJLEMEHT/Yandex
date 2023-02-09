import pygame
import requests
import sys


def cords_to_img(cords, z):
    cords = ','.join(cords)
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={cords}&z={z}&l=map&z=12"
    response = requests.get(map_request)

    map_file = f"map.png"
    with open(map_file, 'wb') as file:
        file.write(response.content)

