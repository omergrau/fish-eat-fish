import asyncio
import pygame
from extras import Player, Fish
from extras.constants import *
from extras.resources import *


class game():
    def __init__(self):
        self.pause = False
        self.fullscreen = False
        self.pause_pressed = False
        self.images = {}
        self.sounds = {}
        self.load_game_resources()
        self.high_score = 0
        self.game_mode = "game"
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), )
        self.clock = pygame.time.Clock()
        self.fishlist = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.font = pygame.font.Font(None, 36)
        self.text_color = (255, 255, 255)

    def setup(self):
        pygame.mixer.music.load(self.sounds["game music"])
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        pygame.display.set_caption("fish eat fish")
        player1 = Player.player(WIDTH, HEIGHT, self.sounds["eat"],self.images["my fish left"],self.images["my fish right"])
        self.players.add(player1)
        for _ in range(10):
            self.fishlist.add(Fish.fish(WIDTH, HEIGHT))

    def toggle_fullscreen(self):
        if self.fullscreen:
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def update_player(self):
        keys = pygame.key.get_pressed()
        player1 = self.players.sprites()[0]
        player1.move(keys)
        player1.update()

    def update_enemies(self):
        for fish_i in self.fishlist:
            if fish_i.isdisappear():
                self.fishlist.remove(fish_i)
                self.fishlist.add(Fish.fish(WIDTH, HEIGHT))
            else:
                fish_i.update()
            player1 = self.players.sprites()[0]
            if pygame.sprite.collide_mask(player1, fish_i):
                if player1.size > fish_i.size:
                    player1.eating(fish_i.size)
                    self.fishlist.remove(fish_i)
                    self.fishlist.add(Fish.fish(WIDTH, HEIGHT))
                else:
                    self.game_mode = "game over"

    def draw(self):
        self.fishlist.draw(self.screen)
        self.players.draw(self.screen)

    def pausef(self, event):
        if not self.pause_pressed:
            self.pause = not self.pause
            self.pause_pressed = True

    def update_keyboard_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_mode = "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    self.game_mode = "quit"
                if event.key == pygame.K_p:
                    self.pausef(event)
                if event.key == pygame.K_f:
                    self.fullscreen = not self.fullscreen
                    self.toggle_fullscreen()
            else:
                self.pause_pressed = False

    def update_game(self):
        self.screen.blit(pygame.image.load(self.images["ocean"]).convert(), (0, 0))
        if self.game_mode == "quit":
            self.running = False
        if self.game_mode == "game over":
            text = self.font.render(f"Press SPACE on the keyboard to start the game or esc to Quit", True,
                                    self.text_color)
            text_rect = text.get_rect(center=((WIDTH // 2), HEIGHT // 2))
            self.screen.blit(text, text_rect)
            text = self.font.render(f"your best score is {self.high_score}", True, self.text_color)
            score_rect = text.get_rect(center=((WIDTH // 2), 50))
            self.screen.blit(text, score_rect)
            text = self.font.render(f"press f for full screen or p to pause the game", True, self.text_color)
            score_rect = text.get_rect(center=((WIDTH // 2), (HEIGHT // 2) + 80))
            self.screen.blit(text, score_rect)

    def update(self):
        self.update_player()
        self.update_enemies()
        self.update_keyboard_input()

    async def game(self):
        self.running = True
        self.setup()
        while self.running:
            self.update_game()
            if self.game_mode == "game":
                self.update()
                self.draw()
            if self.game_mode == "game over":
                await self.game_over()
                self.update_keyboard_input()
            if self.game_mode == "quit":
                break
            self.clock.tick(FPS)
            pygame.display.flip()
            await asyncio.sleep(0)
        pygame.quit()

    async def game_over(self):
        self.update_keyboard_input()
        pygame.mixer.music.load(self.sounds["lose"])
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game_mode = "game"
                    game1.__init__()
                    await game1.game()
        await asyncio.sleep(0)

    def load_game_resources(self):
        self.load_images()
        self.load_sounds()

    def load_images(self):
        self.images["my fish left"] = load_resource("../assets/images/my fish left.png")
        self.images["my fish right"] = load_resource("../assets/images/my fish right.png")
        self.images["ocean"] = load_resource("../assets/images/ocean.png")

    def load_sounds(self):
        self.sounds["game music"] = load_resource("../assets/music/game-music-loop.wav")
        self.sounds["lose"] = load_resource("../assets/music/lose_video-game.wav")
        self.sounds["eat"] = load_resource("../assets/music/plastic-crunch.wav")



if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    game1 = game()
    game = asyncio.run(game1.game())
