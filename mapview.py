import pygame
import requests


class MapView(pygame.sprite.Sprite):
    # Получение карты
    def cords_to_img(self):
        coords = ','.join(map(str, self.coords))
        print(coords)
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={coords}&z={self.z}&l={self.lay_type}&size=450,450"
        response = requests.get(map_request)
        map_file = f"images/map.png"
        # Обновление карты
        with open(map_file, 'wb') as file:
            file.write(response.content)
        self.image = pygame.image.load(f'images/map.png')

    # Отображение карты
    def __init__(self, screen, z, coords):
        # Инициализируем и задаём начальную позицию
        super(MapView, self).__init__()
        # Экран
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Начальные параметры
        self.z = z
        self.coords = coords
        self.lay_type = 'map'
        # Подгрузка изображения
        self.cords_to_img()
        # Рабочая область карты
        self.rect = self.image.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.centerx
        self.rect.size = self.screen_rect.size

    # Переключение на спутник
    def change_lay_sat(self):
        self.lay_type = 'sat'
        self.cords_to_img()

    # Переключение на схему
    def change_lay_map(self):
        self.lay_type = 'map'
        self.cords_to_img()

    def change_lay_hybr(self):
        self.lay_type = 'sat,skl'
        self.cords_to_img()

    # Вывод карты
    def draw(self):
        self.screen.blit(self.image, self.rect)



