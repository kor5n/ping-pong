from pygame import *
window = display.set_mode((700, 500))
display.set_caption("Пинг-Понг")
game = True
clock = time.Clock()
class Player(sprite.Sprite):
    def __init__(self, x, y, width, height, who_plays, color1, color2, color3):
        self.x = x
        self.y = y
        self.who_plays = who_plays
        self.width = width
        self.height = height
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.rect = self.color1.get_rect()
        #self.image_pl = Surface((self.width, self.height))
        #self.image_pl.fill((self.color1, self.color2, self.color3 ))
        
    def show(self):
        
        window.blit(self.rect, (self.x, self.y))
    def move(self):
        keys_pressed = key.get_pressed()
        if self.who_plays == "left_pl":
            if keys_pressed[K_UP]:
                self.y -= 5
            elif keys_pressed[K_DOWN]:
                self.y += 5
        elif self.who_plays == "right_pl":
            if keys_pressed[K_w]:
                self.y -= 5
            if keys_pressed[K_s]:
                self.y += 5
        self.show()
player1 = Player(10, 250, 20, 100, "right_pl", 200, 255, 255)
player2 = Player(690, 250, 20, 100, "left_pl", 200, 255, 255)
class Ball(sprite.Sprite):
    def __init__(self, width, height, image, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = transform.scale(image.load(image), (self.width, self.height))
    def show(self):
        window.blit(self.image, (350, 450))
    def bounce(self):
        pass
while game:
    player1.move()
    player2.move()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(60)