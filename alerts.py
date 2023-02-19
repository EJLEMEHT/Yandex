class Alert:
    def __init__(self, screen, message, color, font, timer=1600):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.message = message
        self.text_color = color
        self.font = font
        self.timer = timer
        self.message_img = self.font.render(self.message, True, self.text_color)
        self.message_rect = self.message_img.get_rect()
        self.message_rect.x = self.screen_rect.left + 25
        self.message_rect.y = self.screen_rect.top + 25

    def draw(self):
        self.screen.blit(self.message_img, self.message_rect)
