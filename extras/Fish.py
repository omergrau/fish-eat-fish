import pygame
import random

class fish(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        super().__init__()
        Rrandomcolor = random.randint(0, 255)
        Grandomcolor = random.randint(0, 255)
        tint_color = (Rrandomcolor, Grandomcolor, 0, 255)
        self.x = random.choice((5, WIDTH))
        self.y = random.randint(0, HEIGHT)
        self.size = random.random() * 200
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.speed = random.randint(1, 5)
        if self.x == 5:
            self.direction = 1
        else:
            self.direction = -1
        if self.direction == 1:
            self.image = pygame.image.load("extras\my fish right.png").convert_alpha()
        else:
            self.image = pygame.image.load("extras\my fish left.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        colored_image = self.image.copy()
        tint_surface = pygame.Surface(colored_image.get_size(), pygame.SRCALPHA)
        tint_surface.fill(tint_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.image.set_colorkey((255, 255, 255))
        colored_image.blit(tint_surface, (0, 0), special_flags=pygame.BLEND_RGB_ADD)
        self.image = colored_image

    def update(self):
        self.x += self.speed * self.direction
        self.rect.topleft = (self.x, self.y)

    def isdisappear(self):
        if self.x < 0 or self.x > self.WIDTH:
            return True