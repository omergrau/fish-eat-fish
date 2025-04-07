import pygame
import random
import os
import sys

def load_resource(filename):
    if 'js' in sys.modules:
        path = os.path.join('data', 'extras', filename)
    elif hasattr(sys, '_MEIPASS'):
        path = os.path.join(sys._MEIPASS, 'extras', filename)
    else:
        path = os.path.join(os.path.dirname(__file__), 'extras', filename)
    return path
class fish(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT,level):
        super().__init__()
        Rrandomcolor = random.randint(0, 255)
        Grandomcolor = random.randint(0, 255)
        tint_color = (Rrandomcolor, Grandomcolor, 0, 255)
        self.picturs = [("my fish left.png", "my fish right.png"), ("level_2_left.PNG", "level_2.PNG")]
        self.size = random.random() * 200
        self.x = random.choice((5,WIDTH))
        self.y = random.randint(0, HEIGHT-15)
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.level=level
        self.speed = random.randint(1, 5)
        if self.x == 5:
            self.direction = 1
        else:
            self.direction = -1

        if self.direction == 1:
            self.image = load_resource(self.picturs[self.level][1]).convert_alpha()
        else:
            self.image = load_resource(self.picturs[self.level][0]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        colored_image = self.image.copy()
        tint_surface = pygame.Surface(colored_image.get_size(), pygame.SRCALPHA)
        tint_surface.fill(tint_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.image.set_colorkey((255, 255, 255))
        colored_image.blit(tint_surface, (0, 0), special_flags=pygame.BLEND_RGB_ADD)
        self.image = colored_image

    def check_borders(self):
        if self.x < 0:
            self.x = 982
        if self.x > 982:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.y > 736:
            self.y = 736

    def update(self):
        self.x += self.speed * self.direction
        self.rect.topleft = (self.x, self.y)

    def isdisappear(self):
        if self.x < 0 or self.x > self.WIDTH:
            return True
    def level_up(self,level):
        self.level += 1

