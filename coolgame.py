from pygame import *
p1=0
p2=0
winner=""
class GameSprite(sprite.Sprite):
    def __init__(self, img, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(img), (100, 100))
        self.speed_x = speed
        self.speed_y = speed
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        soyuz.blit(self.image, (self.rect.x, self.rect.y))

class Player(sprite.Sprite):
    def __init__(self, img, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(img), (30, 300))
        self.speed_x = speed
        self.speed_y = speed
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        soyuz.blit(self.image, (self.rect.x, self.rect.y))
    def move1(self):
        keys_p=key.get_pressed()
        if keys_p[K_DOWN] and self.rect.y<495:
            self.rect.y+=self.speed_y
        if keys_p[K_UP] and self.rect.y>5:
            self.rect.y-=self.speed_y
    def move2(self):
        keys_p=key.get_pressed()
        if keys_p[K_s] and self.rect.y<495:
            self.rect.y+=self.speed_y
        if keys_p[K_w] and self.rect.y>5:
            self.rect.y-=self.speed_y
soyuz=display.set_mode((700,500))
display.set_caption("Весёлые приключения")
racket=Player("racket.png", 3, 50, 100)
racketa=Player("racket.png", 3, 600, 100)
ball=GameSprite("ball1.png", 3, 300, 200)
game = True
finish=False
FPS=6000
clock=time.Clock()
clock=time.Clock()
font.init()
mixer.init()
mixer.music.load("DailyRay - Вот он, настоящий пельмень (TikTok).mp3")
mixer.music.play()
back=transform.scale(image.load("flat.jpg"),(700,500))
font1=font.Font(None, 70)
win = font1.render(winner+'победил!', True, (0, 255, 0))
font2=font.Font(None, 50)
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    if not finish:
        ball.rect.x+=ball.speed_x
        ball.rect.y+=ball.speed_y
        if ball.rect.y > 450 or ball.rect.y < 0:
            ball.speed_y*=-1
        if sprite.collide_rect(ball, racket) or sprite.collide_rect(ball, racketa):
            ball.speed_x*=-1
        if ball.rect.x > 700:
            ball.rect.x=300
            ball.rect.y=200
            p1+=1
        if ball.rect.x < 0:
            ball.rect.x=300
            ball.rect.y=200
            p2+=1
        if p1==5:
            display.set_caption("Первый игрок выиграл!!!!")
        if p2==5:
            display.set_caption("Второй игрок выиграл!!!!")

        soyuz.blit(back, (0,0))
        racket.reset()
        racketa.reset() 
        racket.move2()
        racketa.move1()
        ball.reset()
        display.update()
        clock.tick(FPS)
