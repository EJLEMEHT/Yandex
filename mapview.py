import pygame
import requests
from location import Location
from numpy import sin, cos, arccos, round, pi


class MapView(pygame.sprite.Sprite):
    # Получение карты
    def cords_to_img(self):
        coords = ','.join(map(str, self.coords))
        print(coords)
        if self.pt:
            map_request = f"http://static-maps.yandex.ru/1.x/?ll={coords}&z={self.z}&l={self.lay_type}&size=450,450&pt={self.pt}"
        else:
            map_request = f"http://static-maps.yandex.ru/1.x/?ll={coords}&z={self.z}&l={self.lay_type}&size=450,450"
        response = requests.get(map_request)
        map_file = f"images/map.png"
        # Обновление карты
        with open(map_file, 'wb') as file:
            file.write(response.content)
        self.image = pygame.image.load(f'images/map.png')

    def search(self, name, loc):
        self.loc = loc
        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
        geocoder_params = {
            "apikey": "5b8c3077-c60d-4573-8990-122d645eddde",
            "geocode": name,
            "format": "json"}
        response = requests.get(geocoder_api_server, params=geocoder_params)
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]

        loc.text = toponym["metaDataProperty"]["GeocoderMetaData"]['text']
        self.postal_code = toponym["metaDataProperty"]["GeocoderMetaData"]['Address']['postal_code']
        if loc.postal_code:
            loc.text += ', Почтовый индекс: ' + toponym["metaDataProperty"]["GeocoderMetaData"]['Address']['postal_code']

        cords = toponym["Point"]["pos"].split(' ')
        self.pt = f"{','.join(cords)},pm2dgl"
        self.coords = tuple([float(elem) for elem in toponym["Point"]["pos"].split(' ')])
        self.cords_to_img()

    def postal_code_update(self):
        if self.loc.postal_code and self.postal_code:
            self.loc.text += ', Почтовый индекс: ' + self.postal_code
        else:
            self.loc.text = self.loc.text[:-25]


    def search_org(self, cords, loc):
        search_api_server = "https://search-maps.yandex.ru/v1/"
        api_key = "f576937a-cfa6-471f-9a3e-c6da6a4e04fa"
        address_ll = ','.join(cords.split())
        search_params = {
            "apikey": api_key,
            "lang": "ru_RU",
            "ll": address_ll,
            "type": "biz"
        }
        response = requests.get(search_api_server, params=search_params)
        response_json = response.json()
        organization = response_json['features'][0]
        point = [str(elem) for elem in organization['geometry']['coordinates']]
        org_longt, org_latt = point[0], point[1]
        toponym_longitude, toponym_lattitude = cords
        if self.getDistanceBetweenPoints(float(org_latt), float(org_longt), float(toponym_lattitude), float(toponym_longitude)) < 50:
            loc.text = organization['properties']['CompanyMetaData']['name']

    def getDistanceBetweenPoints(self, latitude1, longitude1, latitude2, longitude2):
        theta = longitude1 - longitude2

        distance = 60 * 1.1515 * self.rad2deg(
            arccos(
                (sin(self.deg2rad(latitude1)) * sin(self.deg2rad(latitude2))) +
                (cos(self.deg2rad(latitude1)) * cos(self.deg2rad(latitude2)) * cos(self.deg2rad(theta)))
            )
        )
        km = round(distance * 1.609344, 3)
        return km * 1000

    def rad2deg(self, radians):
        degrees = radians * 180 / pi
        return degrees

    def deg2rad(self, degrees):
        radians = degrees * pi / 180
        return radians

    # Отображение карты
    def __init__(self, screen, z, coords, loc):
        # Инициализируем и задаём начальную позицию
        super(MapView, self).__init__()
        # Экран
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Начальные параметры
        self.postal_code = ''
        self.loc = loc
        self.pt = ''
        self.z = z
        self.coords = coords
        self.lay_type = 'map'
        # Подгрузка изображения
        self.cords_to_img()
        # Рабочая область карты
        self.rect = self.image.get_rect()
        self.rect.top = self.screen_rect.top
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

    # Переключение на гибрид
    def change_lay_hybr(self):
        self.lay_type = 'sat,skl'
        self.cords_to_img()

    # Удаление метки
    def delete_pt(self):
        self.pt = ''
        self.cords_to_img()

    # Вывод карты
    def draw(self):
        self.screen.blit(self.image, self.rect)



