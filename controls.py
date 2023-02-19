import pygame as pg
import sys
from alerts import Alert


def events(mapview, screen, font, alerts):
    # Обработка событий
    for event in pg.event.get():

        # Выход через крестик
        if event.type == pg.QUIT:
            sys.exit()

        elif event.type == pg.KEYDOWN:
            # Выход
            if event.key == pg.K_ESCAPE:
                sys.exit()
            # Уменьшить
            elif event.key == pg.K_PAGEDOWN:
                if mapview.z > 3:
                    mapview.z -= 1
                    mapview.cords_to_img()
                else:
                    if len(alerts) != 0:
                        alerts.pop(0)
                    alerts.append(Alert(screen, "Слишком далеко", '#ffffff', font))
                    print("Слишком далеко")
            # Увеличить
            elif event.key == pg.K_PAGEUP:
                if mapview.z < 19:
                    mapview.z += 1
                    mapview.cords_to_img()
                else:
                    if len(alerts) != 0:
                        alerts.pop(0)
                    alerts.append(Alert(screen, "Слишком близко", '#ffffff', font))
                    print("Слишком близко")
            # Перемещение вниз
            elif event.key == pg.K_DOWN:
                if mapview.coords[1] - 2 ** (8 + 17 - mapview.z) / (10 ** 5) >= -83:
                    mapview.coords = (mapview.coords[0], mapview.coords[1] - 2 ** (8 + 17 - mapview.z) / (10 ** 5))
                    mapview.cords_to_img()
            # Перемещение вверх
            elif event.key == pg.K_UP:
                if mapview.coords[1] + 2 ** (8 + 17 - mapview.z) / (10 ** 5) <= 83:
                    mapview.coords = (mapview.coords[0], mapview.coords[1] + 2 ** (8 + 17 - mapview.z) / (10 ** 5))
                    mapview.cords_to_img()
            # Перемещение вправо
            elif event.key == pg.K_RIGHT:
                if mapview.coords[0] + (2 ** (8.91 + 17 - mapview.z)) / (10 ** 5) <= 180:
                    mapview.coords = (mapview.coords[0] + (2 ** (8.91 + 17 - mapview.z)) / (10 ** 5), mapview.coords[1])
                else:
                    mapview.coords = (mapview.coords[0] + (2 ** (8.91 + 17 - mapview.z)) / (10 ** 5) - 360,
                                      mapview.coords[1])
                mapview.cords_to_img()
            # Перемещение влево
            elif event.key == pg.K_LEFT:
                if mapview.coords[0] - (2 ** (8.91 + 17 - mapview.z)) / (10 ** 5) >= -180:
                    mapview.coords = (mapview.coords[0] - (2 ** (8.91 + 17 - mapview.z)) / (10 ** 5), mapview.coords[1])
                else:
                    mapview.coords = (mapview.coords[0] - (2 ** (8.91 + 17 - mapview.z)) / (10 ** 5) + 360,
                                      mapview.coords[1])
                mapview.cords_to_img()


def update(bg_color, screen, mapview, layer_buttons, alerts):
    # Обновление экрана
    screen.fill(bg_color)
    mapview.draw()
    for button in layer_buttons:
        button.process()
    for alert in alerts:
        if alert.timer > 0:
            alert.timer -= 1
            alert.draw()
        else:
            alerts.pop(0)
