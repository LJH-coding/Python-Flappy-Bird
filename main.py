import pygame, random, time, sys

# 參數設定
SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512

# 建立遊戲視窗
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# 載入資料
bg_surface = pygame.image.load("./assets/img/background-day.png").convert()
floor_surface = pygame.image.load("./assets/img/base.png").convert()
bird_surface = pygame.image.load("./assets/img/bluebird-midflap.png").convert()

# 位置設定
bird_rect = bird_surface.get_rect(center = (50, SCREEN_HEIGHT // 2))
floor_x_pos = 0


# 遊戲開始介面

# 遊戲迴圈
while True:
    # 取得使用者輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 畫出鳥跟背景
    screen.blit(bg_surface, (0, 0))
    screen.blit(bird_surface, bird_rect)

    # 地板移動
    floor_x_pos -= 1
    if floor_x_pos <= -SCREEN_WIDTH:
        floor_x_pos = 0    
    screen.blit(floor_surface, (floor_x_pos, 450))
    screen.blit(floor_surface, (floor_x_pos + SCREEN_WIDTH, 450))

    # 更新畫面
    pygame.display.update()
    pygame.time.Clock().tick(60)


# 遊戲結束介面