import pygame


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
        self.image = pygame.image.load("extras\my fish right.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.mask = pygame.mask.from_surface(self.image)
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
        print(self.accelartionx, self.accelartiony)

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.lastmove = pygame.time.get_ticks()
            if abs(self.accelartionx) < 5:

                if pygame.time.get_ticks() - self.dellay > 15:
                    self.dellay = pygame.time.get_ticks()
                    self.accelartionx -= self.speed
            self.x += self.accelartionx
            self.image = pygame.image.load("extras\my fish left.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
        if keys[pygame.K_RIGHT]:
            self.lastmove = pygame.time.get_ticks()
            if abs(self.accelartionx) < 5:
                print(self.accelartionx)
                if pygame.time.get_ticks() - self.dellay > 15:
                    self.dellay = pygame.time.get_ticks()
                    self.accelartionx += self.speed
            self.x += self.speed
            self.image = pygame.image.load("extras\my fish right.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
        if keys[pygame.K_UP]:
            self.lastmove = pygame.time.get_ticks()
            if abs(self.accelartiony) < 5:
                print(self.accelartiony)
                if pygame.time.get_ticks() - self.dellay > 15:
                    self.dellay = pygame.time.get_ticks()
                    self.accelartiony -= self.speed
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.lastmove = pygame.time.get_ticks()
            if abs(self.accelartiony) < 5:
                print(self.accelartiony)
                if pygame.time.get_ticks() - self.dellay > 15:
                    self.dellay = pygame.time.get_ticks()
                    self.accelartiony += self.speed
            self.y += self.speed


