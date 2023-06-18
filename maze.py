#создай игру "Лабиринт"!
from pygame import *

win_height = 500
win_width = 700
window = display.set_mode((win_width, win_height))
display.set_caption('Лаберинт')

class GameSprite(sprite.Sprite):
    def __init__(self, play_image, play_x, play_y, play_speed):
        super().__init__()
        self.image = transform.scale(image.load(play_image), (65, 65))
        self.speed = play_speed
        self.rect = self.image.get_rect()
        self.rect.x = play_x
        self.rect.y = play_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update(self):
        keys_ressed = key.get_pressed()
        if keys_ressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_ressed[K_s]and self.rect.y < 435:
            self.rect.y += self.speed
        if keys_ressed[K_d] and self.rect.x < 635:
            self.rect.x += self.speed
        if keys_ressed[K_a]and self.rect.x > 0:
            self.rect.x -= self.speed

class Enemy(GameSprite):

    direction = 'left'
    
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= 635:
            self.direction = 'left'
        
        if self.direction == 'right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed

class Wall(sprite.Sprite):
    def __init__(self, wall_h, wall_w, wall_x, wall_y, color_1, color_2, color_3):
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_w
        self.height = wall_h
        self.image = Surface((self.width, self.height))
        self.image.fill((self.color_1, self.color_2, self.color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

font.init()
font = font.SysFont('Arial', 70)
win = font.render('YOU WIN', True, (250, 0, 0))
lose = font.render('YOU LOSE', True, (250, 0, 0) )
player = Player('hero.png', 20, 50, 8)
monster = Enemy('cyborg.png', 622, 300, 2)
treasure = GameSprite('treasure.png', 500, 400, 0)

background = transform.scale(image.load('background.jpg'), (win_width, win_height))

mixer.init()
mixer.music.load('jungles.ogg')
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')
mixer.music.play()

wall1 = Wall(350, 10, 100, 50, 32, 137, 4)
wall2 = Wall(10, 550, 100, 50, 32, 137, 4)
wall3 = Wall(350, 10, 225, 150, 32, 137, 4)
wall4 = Wall(350, 10, 335, 50, 32, 137, 4)
wall5 = Wall(350, 10, 460, 150, 32, 137, 4)

speed = 10

FPS = 60

clock = time.Clock()
game = True
final = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    keys_ressed = key.get_pressed()

    if final != True:
        window.blit(background, (0, 0))
        player.reset()
        monster.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        treasure.reset()

        player.update()
        monster.update()
   
        if sprite.collide_rect(player, treasure):
            final = True
            window.blit(win, (200, 200))
            money.play()
            
        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4) or sprite.collide_rect(player, wall5):
            final = True
            window.blit(lose, (200, 200))
            kick.play()
        
    display.update()
        
    clock.tick(FPS)   





