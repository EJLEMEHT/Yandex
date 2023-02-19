class Location:
    def __init__(self, screen, text, font, color):
        self.message_rect = None
        self.message_img = None
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text = text
        self.font = font
        self.color = color
        self.postal_code = False
        self.update()

    def update(self):
        self.message_img = self.font.render(self.text, True, self.color)
        self.message_rect = self.message_img.get_rect()
        self.message_rect.x = self.screen_rect.left + 25
        self.message_rect.y = self.screen_rect.bottom - 25

    def enable_postal_code(self, button):
        if self.postal_code:
            button.text = 'Включить почтовый индекс'
            self.postal_code = False
        else:
            button.text = 'Выключить почтовый индекс'
            self.postal_code = True
        print(self.postal_code)
        button.buttonSurf = self.font.render(button.text, True, (20, 20, 20))
        button.screen.blit(button.buttonSurface, button.buttonRect)

    def draw(self):
        self.screen.blit(self.message_img, self.message_rect)
