import pygame


class MapView(pygame.sprite.Sprite):
    # Отображение карты
    def __init__(self, screen, name):
        # Инициализируем и задаём начальную позицию
        super(MapView, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load(f'images/{name}.png')
        self.rect = self.image.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.centerx
        self.rect.size = self.screen_rect.size

    def draw(self):
        # Вывод карты
        self.screen.blit(self.image, self.rect)


class Counter:
    def __init__(self, z):
        self.z = z
