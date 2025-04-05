import pygame
from extras import Player, Fish
import os
import sys
def load_resource(filename):
    if hasattr(sys, '_MEIPASS'):
        path = os.path.join(sys._MEIPASS, filename)
    else:
        path = os.path.join(os.path.dirname(__file__), filename)
    return path

def level_up(player):
    if player.score == 50:
        player.level_up()

def toggle_fullscreen(fullscreen):
    fullscreen = not fullscreen
    if fullscreen:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((982, 736))
    return screen



def load_high_score():
    if os.path.exists(load_resource("extras\highscore.txt")):
        with open(load_resource("extras\highscore.txt"), "r") as f:
            try:
                return int(f.readline())
            except ValueError:
                return 0
    else:
        return 0

def save_high_score(score):
    with open(load_resource("extras\highscore.txt"), "w") as f:
        f.write(str(score))


def play_game(running):

    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    pygame.mixer.music.load(load_resource("extras\game-music-loop-6-144641.mp3"))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    WIDTH = 982
    HEIGHT = 736
    screen = pygame.display.set_mode((WIDTH, HEIGHT), )
    screen.blit(pygame.image.load(load_resource("extras\ocean.png")).convert(), (0, 0))
    pygame.display.set_caption("fish eat fish")
    running = running
    clock = pygame.time.Clock()
    FPS = 50
    fishlist = pygame.sprite.Group()
    for _ in range(10):
        fishlist.add(Fish.fish(WIDTH, HEIGHT,0))
    player1 = Player.player(WIDTH, HEIGHT)
    font = pygame.font.Font(None, 36)
    text_color = (255, 255, 255)
    fullscreen = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            """if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    screen = toggle_fullscreen(fullscreen)"""

        keys = pygame.key.get_pressed()
        player1.move(keys)

        player1.update()
        level_up(player1)
        for fish_i in fishlist:
            if player1.level != fish_i.level:
                fish_i.level=player1.level
            if fish_i.isdisappear():
                fishlist.remove(fish_i)
                fishlist.add(Fish.fish(WIDTH, HEIGHT,player1.level))
            else:
                fish_i.update()
            if pygame.sprite.collide_mask(player1, fish_i):
                if player1.size > fish_i.size:
                    player1.eatting(fish_i.size)
                    fishlist.remove(fish_i)
                    fishlist.add(Fish.fish(WIDTH, HEIGHT,player1.level))
                else:
                    running = False
                    game_over(player1.score,screen)

        screen.blit(pygame.image.load(load_resource("extras\ocean.png")).convert(), (0, 0))
        players = pygame.sprite.Group()
        players.add(player1)
        players.draw(screen)
        clock.tick(FPS)
        fishlist.draw(screen)

        score_text = font.render(f"score: {player1.score} level: {player1.level}", True, text_color)
        score_rect = score_text.get_rect()
        score_rect.topleft = ((WIDTH - score_rect.width) // 2, 10)
        screen.blit(score_text, score_rect)
        pygame.display.flip()

    pygame.quit()
def game_over(score, screen):
    pygame.mixer.music.load(load_resource("extras\lose_video-game.mp3"))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    if score > load_high_score():
        save_high_score(score)
    high_score = load_high_score()
    WIDTH = 982
    HEIGHT = 736
    FPS = 60
    screen.blit(pygame.image.load(load_resource("extras\ocean.png")).convert(), (0, 0))
    pygame.display.set_caption("fish eat fish")
    running = True
    font = pygame.font.Font(None, 36) # אתחול הפונטים מחוץ ללולאה
    text_color = (255, 255, 255)
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit() # סגירה כאן אם המשתמש יוצא ממצב GAME OVER
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit() # סגירה כאן אם המשתמש יוצא ממצב GAME OVER
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    play_game(True) # הפעלה מחדש של המשחק

        text = font.render(f"Press SPACE on the keyboard to rest or esc to Quit", True, text_color)
        text_rect = text.get_rect(center=((WIDTH // 2), HEIGHT // 2))
        screen.blit(text, text_rect)
        text = font.render(f"your best score is {high_score}", True, text_color)
        score_rect = text.get_rect(center=((WIDTH // 2), 50))
        screen.blit(text, score_rect)
        pygame.display.flip()
        clock.tick(FPS)
play_game(True)