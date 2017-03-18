#Time circuit from BTTF
import pygame as pg
import collections





#LED Object
class led7(pg.sprite.Sprite):
    def __init__(self, startstate):
        pg.sprite.Sprite.__init__(self)
        pg.font.init()
        self.font = pg.font.Font(r'c:\\python27\\dc7i.ttf', 64)
        self.index = 0
        self.image = self.font.render(startstate, 1, (0,200,0))
        self.images = []
        self.rect = self.image.get_rect()
        self.irect = {'day':pg.Rect(0,0,120,62), 'month':pg.Rect(160,0,120,62)}

    def set(self, state):
        self.image = self.font.render(state, 1, (0,200,0))
        return self.image

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.image[self.index]
        


#init
game = pg.init()
screen = pg.display.set_mode((640,400))
running = 1

#Main
import time

localtime = time.asctime( time.localtime(time.time()) )
#localtime is str

#create led objects
led1 = led7(localtime)
led2 = led7("1")
led2.rect = (0,200)
led3 = led7("2")
led3.rect = (0,200)
led4 = led7("3")
led4.rect = (0,200)
led5 = led7("4")
led5.rect = (0,200)


row1 = pg.sprite.Group()
row1.add(led1)

led2.images = [led2,led3,led4,led5]
row2 = pg.sprite.Group()
row2.add()



    





while running:

    clock = pg.time.Clock()
    clock.tick(500)
    screen.fill((0,0,0))
    localtime = time.asctime( time.localtime(time.time()) )
    clock.tick(500)
    led1.set(localtime)


    
    row1.draw(screen)
    row2.draw(screen)
    print led1.image.get_rect()

    #draw routine
    #screen.fill((0,0,0))
    #blink(led2,2)
    #screen.blit(led1.image,led1.rect)

    



    pg.display.flip()

    #user input
    if led1.irect['day'].collidepoint(pg.mouse.get_pos()):
        print "Inside Day"
    elif led1.irect['month'].collidepoint(pg.mouse.get_pos()):
        print "Inside month"


    event = pg.event.poll()
    if event.type == pg.QUIT:
        running = 0