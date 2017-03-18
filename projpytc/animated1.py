#Time circuit from BTTF
import pygame as pg
import collections





#LED Object
class spr(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        #pg.font.init()
        #self.font = pg.font.Font(r'c:\\python27\\dc7i.ttf', 64)
        self.index = 0
        self.sheet = pg.transform.scale2x(pg.image.load(r'c:\\python27\characters.png').convert())
        self.rect = self.sheet.get_rect()
        self.frame = {0:pg.Rect(50,0,20,32), 1:pg.Rect(84,0,20,32), 2:pg.Rect(118,0,20,32)}

    def update(self, state):
        self.image = self.font.render(state, 1, (0,200,0))
        return self.image


#init
game = pg.init()
screen = pg.display.set_mode((640,400))
running = 1

#Main

spr1 = spr()
x = 0

while running:

    clock = pg.time.Clock()
    clock.tick(500)
    
 

    #draw routine
    #screen.fill((0,0,0))
    #blink(led2,2)
    for frame in range(len(spr1.frame)):
        image = pg.surface
        screen.blit(spr1.sheet, pg.Rect(x,20, 50,50), spr1.frame[frame])
        pg.time.wait(500)
        pg.display.flip()
        screen.fill((0,0,0))
        x+=15


    



    

    #user input
 

    event = pg.event.poll()
    if event.type == pg.QUIT:
        running = 0