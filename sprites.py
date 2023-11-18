import pygame as pg
from settings import * # settings의 변수들 불러오기
vec = pg.math.Vector2 # vec은 파이게임 수학 벡터2


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40)) # 가로 30, 세로 40의 네모 생성
        self.image.fill(0, 0, 255) # 네모를 노란색으로 채우기
        self.rect = self.image.get_rect() #
        self.rect.center = (WIDTH/2, HEIGHT/2) # 만든 사각형을 전체 창의 밑변과 높이의 절반 되는 지점에 놓기

        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        # jump only if standing on a platform
        self.rect.y += 0.1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 0.1
        if hits:
            self.vel.y = -20  # 20만큼 점프해서 올라가기

    def update(self):
        self.acc = vec(0, PLAYER_GRAVITY) # ACC = 벡터(0, 0.8)
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]: # 만약 키보드 왼쪽 이 눌렸다면 
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]: # 만약 키보드 오른쪽이 눌렸다면 
            self.acc.x = PLAYER_ACC

        self.acc.x += self.vel.x*PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5*self.acc

        if self.pos.x > WIDTH: # 만약 x가 폭보다 크다면 
            self.pos.x = WIDTH # 폭과 같도록 만들고
        if self.pos.x < 0: # 만약 x가 폭보다 작다면 
            self.pos.x = 0 # x를 0으로 바꾼다

        self.rect.midbottom = self.pos


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h)) # 
        self.image.fill(GREEN) # 초록색으로 채우기
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
