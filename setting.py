# game options/settings
TITLE = "TEST"
WIDTH = 800
HEIGHT = 600
FPS = 60

# Player properties
PLAYER_ACC = 1.5 # 플레이어 초기 가속도 = 1.5
PLAYER_FRICTION = -0.2 # 초기 마찰계수
PLAYER_GRAVITY = 0.8 # 플레이어 중력 = 0.8

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),# 발판의 크기와 그려질 위치
                 (WIDTH/2 - 50, HEIGHT*3/4, 100, 20),
                 (125, HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 50)] # (x좌표, y좌표, 가로 길이, 


# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
