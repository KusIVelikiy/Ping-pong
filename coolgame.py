from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, img, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(img), (100, 100))
        self.speed = speed
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        soyuz.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, img, speed, x, y):
        super().__init__(img, speed, x, y)
        self.image = transform.scale(image.load(img), (30, 300))
    def move1(self):
        keys_p=key.get_pressed()
        if keys_p[K_DOWN] and self.rect.y<495:
            self.rect.y+=self.speed
        if keys_p[K_UP] and self.rect.y>5:
            self.rect.y-=self.speed
    def move2(self):
        keys_p=key.get_pressed()
        if keys_p[K_s] and self.rect.y<495:
            self.rect.y+=self.speed
        if keys_p[K_w] and self.rect.y>5:
            self.rect.y-=self.speed
soyuz=display.set_mode((700,500))
display.set_caption("Весёлые приключения")
racket=Player("racket.png", 3, 50, 100)
racketa=Player("racket.png", 3, 600, 100)
ball=GameSprite("UTB84YGmhCbIXKJkSaefq6yasXXaw.jpg", 4, 300, 200)
game = True
finish=False
FPS=6000
clock=time.Clock()
clock=time.Clock()
font.init()
font1=font.Font(None, 70)
win = font1.render('Ты победил!', True, (0, 255, 0))
font2=font.Font(None, 50)
back=transform.scale(image.load("flat-pin-pong-table-top-view-ping-pong-field-w-vector-21075789.jpg"),(700,500))
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    if not finish:
        soyuz.blit(back, (0,0))
        racket.reset()
        racketa.reset() 
        racket.move2()
        racketa.move1()
        ball.reset()
        display.update()
        clock.tick(FPS)
