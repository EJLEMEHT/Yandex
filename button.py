import pygame as pg


class Button:
    # Инициализация кнопки
    def __init__(self, screen, x, y, width, height, font, buttonText='Button', onclickFunction=None, onePress=False):
        # Начальные параметры
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.x = self.screen_rect.right - x
        self.y = self.screen_rect.top + y
        self.width = width
        self.height = height
        self.text = buttonText
        # Реакция на нажатие
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        # Изменение цветов при разных положениях
        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pg.Surface((self.width, self.height))
        self.buttonRect = pg.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(self.text, True, (20, 20, 20))

        self.alreadyPressed = False

    def process(self):

        mousePos = pg.mouse.get_pos()

        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pg.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        self.screen.blit(self.buttonSurface, self.buttonRect)
