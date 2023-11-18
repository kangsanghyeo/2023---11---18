import pygame as pg
import random
from PLAY_settings import *
from PLAYER import *

run = True

'''pg.init()
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                if game_state == GAME_INIT:
                    game_state = GAME_PLAY'''
GAME_STATE = 0
GAME_INIT = 0
GAME_PLAY = 1
GAME_CLEAR = 2
GAME_OVER = 3

class Game:
    GAME_INIT = 0
    GAME_PLAY = 1
    GAME_CLEAR = 2
    GAME_OVER = 3
    def __init__(self):
        pg.init()
        self.game_state = GAME_INIT
        
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self): 
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            if self.game_state == GAME_INIT:
                fp = pg.font.SysFont("Arial", 20, bold=True)
                title_str = "GOING UP"
                title = fp.render(title_str, True, (255, 0, 0))
                title_size = fp.size(title_str)
                title_pos = (self.screen.get_width()/2 - title_size[0]/2, 100)

                sub_title_str = "Press [Space] Key To Start"
                sub_title = fp.render(sub_title_str, True, (255, 0, 0))
                sub_title_size = fp.size(sub_title_str)
                sub_title_pos = (self.screen.get_width()/2 - sub_title_size[0]/2, 200)

                self.screen.blit(title, title_pos)
                self.screen.blit(sub_title, sub_title_pos)     

    def update(self):
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 0.1
                self.player.vel.y = 0
        
        if self.player.rect.top <= HEIGHT/4 :
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()

        while len(self.platforms) < 6:
            width = random.randrange(50, 100)
            p = Platform(random.randrange(0, WIDTH - width),
                         random.randrange(-75, -30),
                         width, 20)
            self.platforms.add(p)
            self.all_sprites.add(p)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if self.game_state == GAME_INIT:
                        self.game_state = GAME_PLAY
        
                    self.player.jumping()

                  

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass
                        
    

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
