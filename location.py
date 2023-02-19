class Location:
    def __init__(self, screen, text, font, color):
        self.message_rect = None
        self.message_img = None
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text = text
        self.font = font
        self.color = color
        self.update()

    def update(self):
        self.message_img = self.font.render(self.text, True, self.color)
        self.message_rect = self.message_img.get_rect()
        self.message_rect.x = self.screen_rect.left + 25
        self.message_rect.y = self.screen_rect.bottom - 25

    def draw(self):
        self.screen.blit(self.message_img, self.message_rect)
