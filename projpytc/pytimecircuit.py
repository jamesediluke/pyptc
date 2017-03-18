#Time circuit from BTTF
import pygame as pg
import collections


#LED Object
class led7(pg.sprite.Sprite):
    def __init__(self, startedstate, ss2):
        pg.sprite.Sprite.__init__(self)
        self.state = (startedstate, ss2)
        self.image = pg.Surface((102,202))
        self.h_strip = pg.image.load(r'c:\\python27\gfx_led_h.png').convert()
        self.v_strip = pg.image.load(r'c:\\python27\\gfx_led_v.png').convert()
        #Locations of horiz strips
        self.strips_h = collections.OrderedDict(
            [('h1',(1,1)), 
            ('h2',(1,85)), 
            ('h3', (1,170))]
            )
        #Locations of vert strips
        self.strips_v = collections.OrderedDict(
            [('v1',(1,5)), 
            ('v2',(75,5)), 
            ('v3',(1,90)), 
            ('v4',(75,90))]
            )
        self.ledcodes = {
            0: ([1,0,1],[1,1,1,1]),
            1: ([0,0,0],[0,1,0,1]),
            2: ([1,1,1],[0,1,1,0]),
            3: ([1,1,1],[0,1,0,1]),
            4: ([0,1,0],[1,1,0,1]),
            5: ([1,1,1],[1,0,0,1]),
            6: ([0,1,1],[1,0,1,1]),
            7: ([1,0,0],[0,1,0,1]),
            8: ([1,1,1],[1,1,1,1]),
            9: ([1,1,1],[1,1,0,1])}
        self.rect = self.image.get_rect()

    def showstate(self, leds_h, leds_v):
        surface = self.image
        self.image.fill((0,0,0))
        for ledpos, state in enumerate(leds_h):
            if state == 1:
                self.image.blit(self.h_strip, self.strips_h.items()[ledpos][1])
        for ledpos, state in enumerate(leds_v):
            if state == 1:
                self.image.blit(self.v_strip, self.strips_v.items()[ledpos][1])
        return surface

    def off(self):
        self.image.fill((0,0,0))
        return self.image

#init
game = pg.init()
screen = pg.display.set_mode((640,400))
running = 1

#create led objects
led1 = led7([0,1,0],[0,0,0,0])
led2 = led7([1,1,0],[0,1,1,0])
led3 = led7([0,1,0],[0,1,1,0])
led4 = led7([0,1,0],[0,1,1,0])

row1 = pg.sprite.Group()
led1.add(row1)



#Blinks passed led
def blink(led, times):
    for time in range(times):    
        screen.blit(led.showstate(led2.state[0], led.state[1]),(110,20))
        pg.time.wait(800)
        pg.display.flip()
        screen.blit(led2.off(), (110,20))

    

#Main
import time

localtime = time.asctime( time.localtime(time.time()) )[5]
print localtime



while running:

    clock = pg.time.Clock()
    clock.tick(200)

    

    #user input
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_0:
                led1.state = (led1.ledcodes[0])
            elif event.key == pg.K_1:
                led1.state = (led1.ledcodes[1])
            elif event.key == pg.K_2:
                led1.state = (led1.ledcodes[2])
            elif event.key == pg.K_3:
                led1.state = (led1.ledcodes[3])
            elif event.key == pg.K_4:
                led1.state = (led1.ledcodes[4])
            elif event.key == pg.K_5:
                led1.state = (led1.ledcodes[5])
            elif event.key == pg.K_6:
                led1.state = (led1.ledcodes[6])
            elif event.key == pg.K_7:
                led1.state = (led1.ledcodes[7])
            elif event.key == pg.K_8:
                led1.state = (led1.ledcodes[8])
            elif event.key == pg.K_9:
                led1.state = (led1.ledcodes[9])

    
    row1.draw()

    #draw routine
    #screen.fill((0,0,0))
    #blink(led2,2)
    #screen.blit(led1.showstate(led1.state[0], led1.state[1]),(20,20))

    



    pg.display.flip()

    event = pg.event.poll()
    if event.type == pg.QUIT:
        running = 0