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

led2 = led7("This is 2")
led2.rect.x = 23
led2.rect.y = 309

led3 = led7("2 is one and two")
led3.rect.x = 23
led3.rect.y = 309

led4 = led7("This is 4")

led5 = led7("this is led5")



row1 = pg.sprite.Group()
row1.add(led1)


row2 = pg.sprite.Group()

row2.add(led2)
#row2.add(led3)
#row2.add(led4)


#row3 = pg.sprite.Group()
#row3.add(led5)

def animate(group, sprite, nextframe):
    group.remove(sprite)
    print group.sprites()
    group.add(nextframe)  
    print group.sprites()





while running:

    clock = pg.time.Clock()
    clock.tick(500)
    screen.fill((0,0,0))
    localtime = time.asctime( time.localtime(time.time()) )
    clock.tick(500)
    led1.set(localtime)


    
    row1.draw(screen)

    animate(row2, led2, led3)
    row2.draw(screen)
    if clock.tick() == 2000:
        screen.fill((0,0,0))
        animate(row2, led3, led2)
    row2.draw(screen)

    #row3.draw(screen)

    #draw routine
    #screen.fill((0,0,0))
    #blink(led2,2)
    #screen.blit(led1.image,led1.rect)

    



    pg.display.flip()

    #user input
    if led1.irect['day'].collidepoint(pg.mouse.get_pos()):
        print "Inside Day"
        print led2.rect.x
        led2.rect.x += 3
        if led2.rect.x >= 480:
            led2.rect.x = 0
    elif led1.irect['month'].collidepoint(pg.mouse.get_pos()):
        print "Inside month"


    


    event = pg.event.poll()
    if event.type == pg.QUIT:
        running = 0