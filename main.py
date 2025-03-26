import pygame
from extras import Player, Fish,level_2
import os
import sys
def load_resource(filename):
    """Helper function to load resources."""
    if hasattr(sys, '_MEIPASS'):
        path = os.path.join(sys._MEIPASS, filename)
    else:
        path = os.path.join(os.path.dirname(__file__), filename)
    return pygame.image.load(path)

def level_up(level,player):
    images=[("extras\my fish right.png","extras\my fish left.png"),("extras\level_2.PNG","extras\level_2.PNG")]
    if player.score == 2:
        level+=1
        player.image = load_resource(images[level][0]).convert_alpha()
        player.image = pygame.transform.scale(player.image, (player.size, player.size))
        player.mask = pygame.mask.from_surface(player.image)
        player.score = 0

def play_game(running,level0):

    pygame.init()
    WIDTH = 982
    HEIGHT = 736
    screen = pygame.display.set_mode((WIDTH, HEIGHT), )
    screen.blit(load_resource("extras\ocean.png").convert(), (0, 0))
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
        level_up(level0,player1)
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

        screen.blit(load_resource("extras\ocean.png").convert(), (0, 0))
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
    screen.blit(load_resource("extras\ocean.png").convert(), (0, 0))
    pygame.display.set_caption("fish eat fish")
    running = True;
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            play_game(True,0)
        font = pygame.font.Font(None, 36)
        text_color = (255, 255, 255)
        score_text = font.render(f"Press SPACE on the keyboard to rest or esc to Quit", True, text_color)
        score_rect = score_text.get_rect()
        score_rect.topleft = ((WIDTH - score_rect.width) // 2, HEIGHT // 2)
        clock = pygame.time.Clock()
        screen.blit(score_text, score_rect)
        clock.tick(FPS)
        pygame.display.flip()
play_game(True,0)