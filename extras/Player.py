import pygame
import os
import sys

def load_resource(filename):
    """Helper function to load resources."""
    if hasattr(sys, '_MEIPASS'):
        path = os.path.join(sys._MEIPASS, 'extras', filename)
    else:
        path = os.path.join(os.path.dirname(__file__), filename)
    try:
        return pygame.image.load(path)
    except FileNotFoundError as message:
        path = os.path.join(sys._MEIPASS, 'extras', filename)
        return pygame.image.load(path)


class player(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        super().__init__()
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.score = 0
        self.speed = 0.25
        self.slowdownspeed = 0.5
        self.accelartionx = 0
        self.accelartiony = 0
        self.size = 50
        image_right = load_resource("my fish right.png").convert_alpha()
        self.rect = image_right.get_rect()
        image_right = pygame.transform.scale(image_right, (self.size, self.size))
        self.mask = pygame.mask.from_surface(image_right)
        image_left = load_resource("my fish left.png").convert_alpha()
        self.rect = image_left.get_rect()
        image_left = pygame.transform.scale(image_left, (self.size, self.size))
        self.mask = pygame.mask.from_surface(image_left)
        self.images = (image_right,image_left)
        self.image = image_right
        self.dellay = pygame.time.get_ticks()
        self.lastmove = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.dellay > 5:
            if self.accelartiony > 0:
                self.accelartiony -= self.slowdownspeed
            if self.accelartiony < 0:
                self.accelartiony += self.slowdownspeed
            if self.accelartionx > 0:
                self.accelartionx -= self.slowdownspeed
            if self.accelartionx < 0:
                self.accelartionx += self.slowdownspeed
            self.dellay = pygame.time.get_ticks()
        if abs(self.accelartionx) < 1 and  pygame.time.get_ticks() - self.lastmove > 100:
            self.accelartionx = 0
        if abs(self.accelartiony) < 1 and  pygame.time.get_ticks() - self.lastmove > 100:
            self.accelartiony = 0
        self.x += self.accelartionx
        self.y += self.accelartiony
        self.rect.topleft = (self.x + self.accelartionx, self.y + self.accelartiony)
        self.mask = pygame.mask.from_surface(self.image)

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.lastmove = pygame.time.get_ticks()
            if abs(self.accelartionx) < 5:

                if pygame.time.get_ticks() - self.dellay > 15:
                    self.dellay = pygame.time.get_ticks()
                    self.accelartionx -= self.speed
            self.x += self.accelartionx
            self.image = load_resource("my fish left.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
        if keys[pygame.K_RIGHT]:
            self.lastmove = pygame.time.get_ticks()
            if abs(self.accelartionx) < 5:
                if pygame.time.get_ticks() - self.dellay > 15:
                    self.dellay = pygame.time.get_ticks()
                    self.accelartionx += self.speed
            self.x += self.speed
            self.image = load_resource("my fish right.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
        if keys[pygame.K_UP]:
            self.lastmove = pygame.time.get_ticks()
            if abs(self.accelartiony) < 5:
                if pygame.time.get_ticks() - self.dellay > 15:
                    self.dellay = pygame.time.get_ticks()
                    self.accelartiony -= self.speed
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.lastmove = pygame.time.get_ticks()
            if abs(self.accelartiony) < 5:
                if pygame.time.get_ticks() - self.dellay > 15:
                    self.dellay = pygame.time.get_ticks()
                    self.accelartiony += self.speed
            self.y += self.speed


