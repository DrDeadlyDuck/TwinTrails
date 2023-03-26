import pygame
import random
import math


pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Twin Trails')
player1 = pygame.image.load(r'Red Player.png')
player2 = pygame.image.load(r'Blue Player.png')
enemy = pygame.image.load(r'Enemy.png')

class Player(pygame.sprite.Sprite):
    def __init__(self, png):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.velocity = 10
        img = pygame.image.load(f"{png}.png")
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
    def draw(self,no, x, y, direction):
        self.x =  x
        self.y = y
        self.no = no
        if self.no == "1":
            self.player = player1
        if self.no == "2":
            self.player = player2
        self.direction = direction
        if self.direction:
            window.blit(self.player, (x, y))
        if not self.direction:
            window.blit(pygame.transform.flip(self.player, True, False), (x, y))


class Enemy:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("Enemy.png")
        self.images = []
        self.x = random.randint(0, 550)
        self.y = random.randint(0, 550)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def spawn(self):
        window.blit(enemy, (self.x, self.y))

def home():
    home_run = True
    clock = pygame.time.Clock()
    bounce = 1
    back = False
    font = pygame.font.Font("pixel.ttf", 160)
    start_font = pygame.font.Font("pixel.ttf", 60)
    while home_run:
        title = font.render(f'TWIN', True, (255, 255, 255))
        title2 = font.render(f'TRAILS', True, (255, 255, 255))
        start = start_font.render(f'Press [SPACE]', True, (255, 255, 255))
        start_rect = start.get_rect(center=(300,400))
        window.fill((40, 43, 48))
        window.blit(start, start_rect)
        if bounce == 1:
            window.blit(title, (50, 75))
            window.blit(title2, (20, 190))
            bounce = 2
            back = False
        elif bounce ==2:
            window.blit(title, (50, 80))
            window.blit(title2, (20, 195))
            if back == False:
                bounce = 3
            else:
                bounce = 1
        elif bounce ==3:
            window.blit(title, (50, 85))
            window.blit(title2, (20, 200))
            if back == False:
                bounce = 4
            else:
                bounce = 2
        elif bounce ==4:
            window.blit(title, (50, 90))
            window.blit(title2, (20, 205))
            if back == False:
                bounce = 5
            else:
                bounce = 3
        else:
            window.blit(title, (50, 95))
            window.blit(title2, (20, 210))
            bounce = 4
            back = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                home_run = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    home_run = False
                    main()
        pygame.display.update()
        clock.tick(10)

def death(score):
    clock = pygame.time.Clock()
    bounce = 1
    reason_font = pygame.font.Font("pixel.ttf", 30)
    back = False
    font = pygame.font.Font("pixel.ttf", 115)
    for i in range(0,30):
        title = font.render(f'YOU DIED', True, (223, 86, 86))
        reason = reason_font.render(f'You went too far apart', True, (223, 86, 86))
        score_text = reason_font.render(f'Score: {score}', True, (223, 86, 86))
        reason_rect = reason.get_rect(center=(300, 225))
        score_rect = score_text.get_rect(center=(300, 275))
        window.fill((40, 43, 48))
        window.blit(reason, reason_rect)
        window.blit(score_text, score_rect)
        if bounce == 1:
            window.blit(title, (40, 75))
            bounce = 2
            back = False
        elif bounce ==2:
            window.blit(title, (40, 80))
            if back == False:
                bounce = 3
            else:
                bounce = 1
        elif bounce ==3:
            window.blit(title, (40, 85))
            if back == False:
                bounce = 4
            else:
                bounce = 2
        elif bounce ==4:
            window.blit(title, (40, 90))
            if back == False:
                bounce = 5
            else:
                bounce = 3
        else:
            window.blit(title, (40, 95))
            bounce = 4
            back = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                home_run = False
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(10)
    main()

def main():
    font = pygame.font.Font("pixel.ttf", 36)
    x1 = 100
    y1 = 100
    x2 = 500
    y2 = 500
    velocity = 50
    direction1 = True
    direction2 = True
    run = True
    gap = 10
    score = 0
    player1 = Player("Red Player")
    player2 = Player("Blue Player")
    en = Enemy()
    clock = pygame.time.Clock()
    while run:
        score_text = font.render(f'{score}', True, (255, 255, 255))
        window.fill((40, 43, 48))
        en.spawn()
        window.blit(score_text, (290, 10))
        line = pygame.draw.line(window, (236, 213, 138), (x1 + gap, y1 + gap), (x2 + gap, y2 + gap), width=7)
        player1.draw("1", x1, y1, direction1)
        player2.draw("2", x2, y2, direction2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    home()

                if event.key == pygame.K_LEFT:
                    x1 -= velocity
                    direction1 = True

                if event.key == pygame.K_RIGHT:
                    x1 += velocity
                    direction1 = False

                if event.key == pygame.K_UP:
                    y1 -= velocity

                if event.key == pygame.K_DOWN:
                    y1 += velocity

                if event.key == pygame.K_a:
                    x2 -= velocity
                    direction2 = True

                if event.key == pygame.K_d:
                    x2 += velocity
                    direction2 = False

                if event.key == pygame.K_w:
                    y2 -= velocity

                if event.key == pygame.K_s:
                    y2 += velocity

            if (en.x>x1 and en.x<x2 or en.x>x2 and en.x<x1) and (en.y > y1 and en.y < y2 or en.y > y2 and en.y < y1):
                score += 1
                en.__init__()
                en.spawn()

            if x1-x2 > 501 or x2-x1 > 501 or y1-y2 > 501 or y2-y1 > 501:
                death(score)
                score = 0
                x1 = 100
                y1=100
                x2=500
                y2=500

        clock.tick(60)
        pygame.display.update()


if __name__ == "__main__":
    home()
