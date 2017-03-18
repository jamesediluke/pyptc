import pygame as pg
class block(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r'c:\\python27\gfx_led_h.png').convert()
        self.rect = self.image.get_rect()

#init
game = pg.init()
screen = pg.display.set_mode((640,400))
running = 1

while running:
    blob = block()
    blob.rect.x = 100
    blob.rect.y = 300


    row1 = pg.sprite.Group()
    row1.add(blob)

    row1.draw(screen)

    pg.display.flip()

    event = pg.event.poll()

    if event.type == pg.QUIT:
        running = 0