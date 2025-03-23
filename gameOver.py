from main import play_game
import pygame
import Player

def game_over(score):
    WIDTH = 982
    HEIGHT = 736
    FPS = 60
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.blit(pygame.image.load("deepocean.png").convert(), (0, 0))
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
    score_text = font.render(f"score: {score}", True, text_color)
    score_rect = score_text.get_rect()
    score_rect.topleft = ((WIDTH - score_rect.width) // 2, 10)
    pygame.display.flip()

