import pygame
import random

Fish_SIZE = 30
Fish_SPEED = 3

class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (Fish_SIZE, Fish_SIZE))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.direction = random.choice([[-1, 0], [1, 0]])

    def update(self, player, Fish_bullets, WIDTH, HEIGHT):


        """if new_x <= 0:
            self.time_from_last_move = 0
            self.direction = random.choice([[1, 0], [0, 1], [0, -1]])
        elif new_x > WIDTH - ALIEN_SIZE:
            new_x = WIDTH - ALIEN_SIZE
            self.direction = random.choice([[-1, 0], [0, 1], [0, -1]])
        if new_y <= 0:
            self.time_from_last_move = 0
            self.direction = random.choice([[-1, 0], [1, 0], [0, 1]])
        elif new_y > HEIGHT - ALIEN_SIZE:
            new_y = HEIGHT - ALIEN_SIZE
            self.direction = random.choice([[-1, 0], [1, 0], [0, -1]])

        self.rect.x = new_x
        self.rect.y = new_y

        if self.fire_timer >= self.fire_rate:
            bullet_x, bullet_y = (
                self.rect.x + ALIEN_SIZE // 2,
                self.rect.y + ALIEN_SIZE // 2,
            )
            alien_bullets.append(((bullet_x, bullet_y), self.direction))
            self.fire_timer = 0"""



    def infect(self):
        self.infected = True

    def is_infected(self):
        return self.infected