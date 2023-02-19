import pygame as pg


class InputBox:

    def __init__(self, screen, x, y, w, h, color_active, color_inactive, font, func=None, loc=None, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.screen = screen
        self.loc = loc
        self.func = func
        self.screen_rect = self.screen.get_rect()
        self.rect.x = self.screen_rect.right - x
        self.rect.y = self.screen_rect.top + y
        self.color_active = color_active
        self.color_inactive = color_inactive
        self.color = self.color_inactive
        self.font = font
        self.text = text
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def clear_input(self):
        self.func(self.text, self.loc)
        self.text = ''
        self.txt_surface = self.font.render(self.text, True, self.color)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    self.clear_input()
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self):
        # Blit the text.
        self.screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(self.screen, self.color, self.rect, 2)