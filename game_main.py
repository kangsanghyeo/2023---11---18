import math
import pygame
import random
import time
from pygame import draw
from pygame.color import Color
from pygame.sprite import Sprite

from key import *
from PLATFORM_LIST import *

FPS = 60
stone_count = 15
score = 0
alien_score = 0
timer = 60
choice1 = 0
choice2 = 0
choice3 = 0
choice4 = 0
choice5 = 0
vel = 5

isjump = False
jumpCount = 10

def rectcollide(sprite, rect):
    if sprite.rect.left <= rect.left <= sprite.rect.right:
        if sprite.rect.top <= rect.top <= sprite.rect.bottom:
            return True
    return False

def decrement_stones():
    global stone_count
    stone_count -= 1
    
class Background(Sprite):
    def __init__(self):
        self.sprite_image = 'background.png'
        self.image = pygame.image.load(
            self.sprite_image).convert()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.dx = 1

        Sprite.__init__(self)

    def update(self):
        self.rect.x -= self.dx
        if self.rect.x == -800:
            self.rect.x = 0

if __name__ == "__main__":
    pygame.init()

    size = (700, 300)
    screen = pygame .display.set_mode(size)

    pygame.display.set_caption("Catapult VS Alien")

    run = True
    clock  = pygame.time.Clock()
    t = 0
    fire_sound = pygame.mixer.Sound('fire.ogg')
    crash_sound = pygame.mixer.Sound('crash.ogg')

    power = 15
    direction = 45

    game_state = GAME_INIT
    background = Background()
    background_group = pygame.sprite.Group()
    background_group.add(background)

    stone = Stone()
    stone.rect.y = -100
    stone_group = pygame.sprite.Group()
    stone_group.add(stone)

    catapult = Catapult(stone)
    catapult.rect.x = 50
    catapult.rect.y = BASE_Y
    catapult_group = pygame.sprite.Group()
    catapult_group.add(catapult)

    alien2 = Alien()
    alien2.rect.x = 340
    alien2.rect.y = BASE_Y
    alien_group2 = pygame.sprite.Group()
    alien_group2.add(alien2)

    alien1 = Alien()
    alien1.rect.x = 450
    alien1.rect.y = BASE_Y
    alien_group1 = pygame.sprite.Group()
    alien_group1.add(alien1)
    
    explosion1 = Explosion()
    explosion_group1 = pygame.sprite.Group()
    explosion_group1.add(explosion1)

    explosion2 = Explosion()
    explosion_group2 = pygame.sprite.Group()
    explosion_group2.add(explosion2)


    platforms = pygame.sprite.Group()
    for x,y,w,h in PLATFORM_LIST:
        p = Platform(x,y,w,h ) 
        platforms.add(p)
    

    game_time1=3660
    po = random.randint(250, 450)
    pos = [po, 250]
    lo = random.randint(250, 450)
    pos2 = [lo, 250]
    square = pygame.Rect(pos, (20, 20))
    ellipse = pygame.Rect(pos2, (20, 20))
    
    # 게임 루프
    while run:
        # 1) 사용자 입력 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    # 초기 화면에서 스페이스를 입력하면 시작
                    if game_state == GAME_INIT:
                        game_state = GAME_PLAY
                    elif game_state == GAME_PLAY:
                        # GAME_PLAY 상태일떄 스페이스를 입력하면 발사
                        if stone.state == STONE_READY:
                            t = 0
                            catapult.fire(power, direction)
                            fire_sound.play()
                            

        if game_state == GAME_PLAY:
            game_time1-= 1
            tttt = game_time1//60
            #print(tttt)
            if tttt < 0:
                # 타이머가 0이 되었을때
                game_state = GAME_CLEAR
                
            if tttt <= 50 and choice1 == 0:
                po = random.randint(250, 450)
                pos = [po, 250]
                lo = random.randint(250, 450)
                pos2 = [lo, 250]
                square = pygame.Rect(pos, (20, 20))
                ellipse = pygame.Rect(pos2, (20, 20))
                choice1 = 1
                
            
            if tttt <= 40 and choice2 == 0:
                po = random.randint(250, 450)
                pos = [po, 250]
                lo = random.randint(250, 450)
                pos2 = [lo, 250]
                square = pygame.Rect(pos, (20, 20))
                ellipse = pygame.Rect(pos2, (20, 20))
                choice2 = 1
            
            if tttt <= 30 and choice3 == 0:
                po = random.randint(250, 450)
                pos = [po, 250]
                lo = random.randint(350, 450)
                pos2 = [lo, 250]
                square = pygame.Rect(pos, (20, 20))
                ellipse = pygame.Rect(pos2, (20, 20))
                choice3 = 1
          
            if tttt <= 20 and choice4 == 0:
                po = random.randint(250, 450)
                pos = [po, 250]
                lo = random.randint(250, 450)
                pos2 = [lo, 250]
                square = pygame.Rect(pos, (20, 20))
                ellipse = pygame.Rect(pos2, (20, 20))
                choice4 = 1
         
            if tttt <= 10 and choice5 == 0:
                po = random.randint(250, 450)
                pos = [po, 250]
                lo = random.randint(250, 450)
                pos2 = [lo, 250]
                square = pygame.Rect(pos, (20, 20))
                ellipse = pygame.Rect(pos2, (20, 20))
                choice5 = 1
                
        
            # 누르고 있는 키 확인하기
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                catapult.backward()
            elif keys[pygame.K_RIGHT]:
                catapult.forward()
            elif keys[pygame.K_UP]:
                if direction < MAX_DIRECTION:
                    direction += 1
            elif keys[pygame.K_DOWN]:
                if direction > MIN_DIRECTION:
                    direction -= 1
            elif keys[pygame.K_SPACE]:
                if power > MAX_POWER:
                    power = MIN_POWER
                else:
                    power += 0.2
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                alien1.backward()
                alien2.backward()
            elif keys[pygame.K_3]:
                alien1.forward()
                alien2.forward()

            if not (isjump):
                if keys[pygame.K_2]:
                    isjump  = True
            else:
                if jumpCount >= -10:
                    alien1.rect.y -= (jumpCount * abs(jumpCount)) * 0.4

                    jumpCount -= 1
                else:
                    jumpCount = 10
                    isjump = False
                    
            if not(isjump):
                if keys[pygame.K_2]: 
                    isjump = True
            else:
                if jumpCount >= -10:
                    alien2.rect.y -= (jumpCount * abs(jumpCount)) * 0.4
                    
                    jumpCount -= 1
                else:
                    jumpCount = 10
                    isjump = False
        
        # 게임 상태 업데이트

        if alien1.rect.y > 0:
            hits = pygame.sprite.spritecollide(alien1, platforms, False)
            if hits:
                alien1.y = hits[0].rect.top + 0.1
                alien1.y = 0
                print("ekgdma")

        if alien2.rect.y > 0:
            hits = pygame.sprite.spritecollide(alien2, platforms, False)
            if hits:
                alien2.y = hits[0].rect.top + 0.1
                alien2.y = 0
                print ("ekgdma")
        
        if stone.state == STONE_FLY:
            t += 0.5
            stone.move(t, 
                       (screen.get_width(), screen.get_height()),
                       decrement_stones)

        if alien1.alive(): # alien2이 아직 살아있는 동안에는 stone과의 충돌여부를 확인
            collided = pygame.sprite.groupcollide(
                        stone_group, alien_group1, False, True)
            
            if collided:
                explosion1.rect.x = \
                   (alien1.rect.x + alien1.rect.width/2) - \
                    explosion1.rect.width/2
                explosion1.rect.y = \
                    (alien1.rect.y + alien1.rect.height/2) - \
                    explosion1.rect.height/2 # 출돌한 경우에는 explosion 스프라이트의 위치를 alien2객체가 있던 곳으로 옮기고 충돌 효과음 재생
                crash_sound.play()
                score += 5
                

        if alien2.alive(): # alien1이 아직 살아있는 동안에는 stone과의 충돌여부를 확인
            collided = pygame.sprite.groupcollide(
                        stone_group, alien_group2, False, True)
            
            if collided: 
                explosion2.rect.x = \
                   (alien2.rect.x + alien2.rect.width/2) - \
                    explosion2.rect.width/2
                explosion2.rect. y = \
                    (alien2.rect.y + alien2.rect.height/2) - \
                    explosion2.rect.height/2 # 충돌한 경우에는 explosion 스프라이트의 위치를 alien1객체가 있던 곳으로 옮기고 충돌 효과음 재생
                crash_sound.play()
                score += 5
                
        if score == 100:
            # 점수가 100점 채워졌을때
            game_state = GAME_CLEAR

        # 외계인이 살아있는데 돌맹이수가 0이면 게임 오버
        if  stone_count == 0:
            game_state = GAME_CLEAR

        if game_state == GAME_PLAY:
            catapult_group.update()
            stone_group.update()
            alien_group1.update()
            alien_group2.update()

        # 게임 상태 그리기
        background_group.update()
        background_group.draw(screen)
        
            
        if game_state == GAME_PLAY: # alien들이 닿았을때 0.1점씩 점수가 깎이는 원 그리기
            pygame.draw.ellipse(screen,
            pygame.color.Color(255, 0, 0),
            ellipse)
            if rectcollide(alien1, ellipse):
                alien_score -= 0.1
            if rectcollide(alien2, ellipse):
                alien_score -= 0.1                  
        
        if game_state == GAME_PLAY: # alien들이 닿았을떄 0.1점씩 점수가 늘어나는 사각형 그리기
            pygame.draw.rect(screen,
            pygame.color.Color(0, 0, 255),
            square)
            if rectcollide(alien1, square):
                alien_score += 0.1
            if rectcollide(alien2, square):
                alien_score += 0.1
                

        if not alien1.alive():
            explosion_group1.update()
            explosion_group1.draw(screen)

        if not explosion1.alive():
            alien1 = Alien()
            alien1.rect.x = random.randint(250, 340)
            alien1.rect.y = BASE_Y 
            alien_group1 = pygame.sprite.Group()
            alien_group1.add(alien1) # explosion이 끝났을떄 새로운 alien 생성
            explosion_group1.add(explosion1) # 새로운 폭발 애니매이션 추가


        if not alien2.alive(): # alien이 돌에 맞아 죽었다면 폭발 애니매이션 재생
            explosion_group2.update()
            explosion_group2.draw(screen)

        if not explosion2.alive():
            alien2 = Alien()
            alien2.rect.x = random.randint(350, 450)
            alien2.rect.y = BASE_Y
            alien_gorup2 = pygame.sprite.Group()
            alien_group2.add(alien2)
            explosion_group2.add(explosion2)
            
        if game_state == GAME_INIT:
            # 초기 화면
            sf = pygame.font.SysFont("Arial", 20 , bold=True)
            title_str = "Catapult VS Alien"
            title = sf.render(title_str, True, (255, 0, 0))
            title_size = sf.size(title_str)
            title_pos = (screen.get_width()/2 - title_size[0]/2, 100)

            sub_title_str = "Press [Space] Key To Start"
            sub_title = sf.render(sub_title_str, True, (255, 0, 0))
            sub_title_size = sf.size(sub_title_str)
            sub_title_pos = (screen.get_width()/2 - sub_title_size[0]/2, 200)

            screen.blit(title, title_pos)
            screen.blit(sub_title, sub_title_pos)

        elif game_state == GAME_PLAY:
            # 플레이 화면
            catapult_group.draw(screen)
            stone_group.draw(screen)
            alien_group1.draw(screen)
            alien_group2.draw(screen)
            platforms.draw(screen)

            # 파워와 각도를 선으로 표시
            line_len = power * 5
            r = math.radians(direction)
            pos1 = (catapult.rect.x+32, catapult.rect.y)
            pos2 = (pos1[0] + math.cos(r)*line_len,
                    pos1[1] - math.sin(r)*line_len)
            draw.line(screen,Color(255, 0, 0), pos1, pos2)

            # 파워와 각도를 텍스트로 표시
            sf = pygame.font.SysFont("Arial", 15)
            text = sf.render("{0} ˚, {1} m/s".
                             format(direction, int(power)), True, (0, 0, 0))
            screen.blit(text, pos2)

            # 돌의 개수를 표시
            sf = pygame.font.SysFont("Monospace", 20)
            text = sf.render('stones : {0}'.
                             format(stone_count), True, (0, 0, 255))
            screen.blit(text, (240, 40))

            # 투석기 점수를 표시
            sf = pygame.font.SysFont("Monospace", 20)
            text_score = sf.render('Catapult score : {0}'.
                                   format(score), True, (0, 0, 255))
            screen.blit(text_score, (10, 60))

            # 외계인 점수를 표시
            sf = pygame.font.SysFont("Monospace", 20)
            text_score = sf.render('Alien score : {0}'.
                                   format(alien_score), True, (0, 0, 255))
            screen.blit(text_score, (400, 60))

            # 현재 타이머를 표시
            sf = pygame.font.SysFont("Monospace", 20)
            text_time1 = sf.render('Time Limit  : {0}'.
                                   format(tttt), True, (0, 0, 255))
            screen.blit(text_time1, (240, 10))
                
        elif game_state == GAME_CLEAR:
            # 게임 클리어
            sf = pygame.font.SysFont("Arial", 20, bold=True)
            if score == alien_score:
                game_state = GAME_OVER
            elif score > alien_score :
                title_str = "Player 1  Win"
            elif score < alien_score :
                title_str = "Player 2  Win"
            title = sf.render(title_str, True, (0, 0, 255))
            title_size = sf.size(title_str)
            title_pos = (screen.get_width()/2 - title_size[0]/2, 100)
            screen.blit(title, title_pos)

        if game_state == GAME_OVER:
            # 게임 오버
            sf = pygame.font.SysFont("Arial", 20, bold=True)
            title_str = "TIE"
            title = sf.render(title_str, True, (255,0,0))
            title_size = sf.size(title_str)
            title_pos = (screen.get_width()/2 - title_size[0]/2, 100)
            screen.blit(title, title_pos)

        pygame.display.flip()
        clock.tick(FPS)
        
    pygame.quit()
