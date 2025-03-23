import random

import pygame


class player(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        super().__init__()
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.score = 0
        self.speed = 0.2
        self.slowdownspeed=0.5
        self.accelartionx = 0
        self.accelartiony = 0
        self.size = 50
        self.image = pygame.image.load("my fish right.png").convert_alpha()
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
            self.image = pygame.image.load("my fish left.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
        if keys[pygame.K_RIGHT]:
            self.lastmove = pygame.time.get_ticks()
            if abs(self.accelartionx) < 5:
                print(self.accelartionx)
                if pygame.time.get_ticks() - self.dellay > 15:
                    self.dellay = pygame.time.get_ticks()
                    self.accelartionx += self.speed
            self.x += self.speed
            self.image = pygame.image.load("my fish right.png").convert_alpha()
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


class fish(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        super().__init__()
        Rrandomcolor = random.randint(0, 255)
        Grandomcolor = random.randint(0, 255)
        tint_color = (Rrandomcolor, Grandomcolor, 0, 255)
        self.x = random.choice((5, WIDTH))
        self.y = random.randint(0, HEIGHT)
        self.size = random.random() * 200
        self.speed = random.randint(1, 5)
        if self.x == 5:
            self.direction = 1
        else:
            self.direction = -1
        if self.direction == 1:
            self.image = pygame.image.load("my fish right.png").convert_alpha()
        else:
            self.image = pygame.image.load("my fish left.png").convert_alpha()
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
        if self.x < 0 or self.x > WIDTH:
            return True


pygame.init()
WIDTH = 982
HEIGHT = 736
screen = pygame.display.set_mode((WIDTH, HEIGHT), )
screen.blit(pygame.image.load("deepocean.png").convert(), (0, 0))
pygame.display.set_caption("fish eat fish")

deepblue = (0, 0, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
running = True
clock = pygame.time.Clock()
FPS = 60

fishlist = pygame.sprite.Group()
for _ in range(10):
    fishlist.add(fish(WIDTH, HEIGHT))
player1 = player(WIDTH, HEIGHT)
font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)
accCounter = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()
    player1.move(keys)

    player1.update()
    for fish_i in fishlist:
        if fish_i.isdisappear():
            fishlist.remove(fish_i)
            fishlist.add(fish(WIDTH, HEIGHT))
        else:
            fish_i.update()
        if pygame.sprite.collide_mask(player1, fish_i):
            if player1.size > fish_i.size:
                player1.score += 1
                fishlist.remove(fish_i)
                player1.size += fish_i.size // 20
                fishlist.add(fish(WIDTH, HEIGHT))
            else:
                pygame.quit()

    screen.blit(pygame.image.load("deepocean.png").convert(), (0, 0))
    players = pygame.sprite.Group()
    players.add(player1)
    players.draw(screen)
    clock.tick(FPS)
    fishlist.draw(screen)

    score_text = font.render(f"score: {player1.score}", True, text_color)
    score_rect = score_text.get_rect()
    score_rect.topleft = ((WIDTH - score_rect.width) // 2, 10)
    screen.blit(score_text, score_rect)
    pygame.display.flip()
pygame.quit()
