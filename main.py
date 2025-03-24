import pygame
from extras import Player, Fish


def play_game(running):
    pygame.init()
    WIDTH = 982
    HEIGHT = 736
    screen = pygame.display.set_mode((WIDTH, HEIGHT), )
    screen.blit(pygame.image.load("extras/deepocean.png").convert(), (0, 0))
    pygame.display.set_caption("fish eat fish")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    running = running
    clock = pygame.time.Clock()
    FPS = 50

    fishlist = pygame.sprite.Group()
    for _ in range(10):
        fishlist.add(Fish.fish(WIDTH, HEIGHT))
    player1 = Player.player(WIDTH, HEIGHT)
    font = pygame.font.Font(None, 36)
    text_color = (255, 255, 255)
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
                fishlist.add(Fish.fish(WIDTH, HEIGHT))
            else:
                fish_i.update()
            if pygame.sprite.collide_mask(player1, fish_i):
                if player1.size > fish_i.size:
                    player1.score += 1
                    fishlist.remove(fish_i)
                    player1.size += fish_i.size // 20
                    fishlist.add(Fish.fish(WIDTH, HEIGHT))
                else:
                    running = False
                    game_over(player1.score)

        screen.blit(pygame.image.load("extras/deepocean.png").convert(), (0, 0))
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
def game_over(score):
    WIDTH = 982
    HEIGHT = 736
    FPS = 60
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.blit(pygame.image.load("extras/deepocean.png").convert(), (0, 0))
    pygame.display.set_caption("fish eat fish")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            play_game(True)
        font = pygame.font.Font(None, 36)
        text_color = (255, 255, 255)
        score_text = font.render(f"Press SPACE on the keyboard to rest", True, text_color)
        score_rect = score_text.get_rect()
        score_rect.topleft = ((WIDTH - score_rect.width) // 2, HEIGHT // 2)
        clock = pygame.time.Clock()
        screen.blit(score_text, score_rect)
        clock.tick(FPS)
        pygame.display.flip()
play_game(True)