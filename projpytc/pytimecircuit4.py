#Time circuit from BTTF
import pygame as pg
import collections
import pdb





#LED Object
class led14(pg.sprite.Sprite):
    def __init__(self, startstate, col, background):
        pg.sprite.Sprite.__init__(self)
        pg.font.init()
        self.font = pg.font.Font(r'c:\python27\projpytc\DSEG14Modern-Italic.ttf', 64)
        self.image = self.font.render(startstate, 1, col, background)
        self.rect = self.image.get_rect()
        self.irect = {'day':pg.Rect(0,0,120,62), 'month':pg.Rect(160,0,120,62)}

    def set(self, state):
        #Need to blit new image onto self.image
        self.image.blit(self.font.render(state, 1, (200,0,0),(0,0,0)),(0,0))
        return self.image


def createrow(resx, border, l1, l2,l3, l4, l5):
    available_x = resx - (border*2)
    l1.rect.x = border
    l2.rect.x=  l1.rect.x + l1.image.get_width() + border
    l3.rect.x = l2.rect.x + l2.image.get_width() + border
    l4.rect.x = l3.rect.x + l3.image.get_width() + border
    l5.rect.x = l4.rect.x + l4.image.get_width() + border
    return (l1,l2,l3,l4,l5)

def sety(row_tup, y):
    for item in row_tup:
        item.rect.y = y
    return row_tup


#Main
#init
game = pg.init()
screen = pg.display.set_mode((800,600))
running = 1
keybuffer = []

#load bg image
bground = pg.image.load('c:\python27\projpytc\metalbackground800.jpg')

#create led objects
#input {month, day, year, hr, min}

#DEPART TIME
DT_month = led14("Feb", (220,0,0),(0,0,0))
DT_day = led14("06", (220,0,0),(0,0,0))
#DT_day.rect.x = 300
#DT_day.rect.y = 700
DT_year = led14("1955", (220,0,0),(0,0,0))
DT_hr = led14(" 04", (220,0,0),(0,0,0))
DT_min = led14("55", (220,0,0),(0,0,0))



#CURRENT TIME
CT_month = led14("Mar", (0,220,0),(0,0,0))
CT_day = led14("06", (0,220,0),(0,0,0))
#DT_day.rect.x = 300
#DT_day.rect.y = 700
CT_year = led14("1955", (0,220,0),(0,0,0))
CT_hr = led14(" 04", (0,220,0),(0,0,0))
CT_min = led14("55", (0,220,0),(0,0,0))

#CURRENT TIME
TD_month = led14("Mar", (150,150,0),(0,0,0))
TD_day = led14("06", (150,150,0),(0,0,0))
#DT_day.rect.x = 300
#DT_day.rect.y = 700
TD_year = led14("1955", (150,150,0),(0,0,0))
TD_hr = led14(" 04", (150,150,0),(0,0,0))
TD_min = led14("55", (150,150,0),(0,0,0))

#Create LEDs in Tuples, spaced for rows
row1leds = createrow(800, 20, DT_month, DT_day, DT_year, DT_hr,DT_min)
row2leds = createrow(800, 20, CT_month, CT_day, CT_year, CT_hr, CT_min)
row3leds = createrow(800, 20, TD_month, TD_day, TD_year, TD_hr, TD_min)

while running:

    clock = pg.time.Clock()
    clock.tick(500)
    
    clock.tick(500)
    
    #Set Y coord for line
    r1 = sety(row1leds, 75)
    r2 = sety(row2leds, 230)
    r3 = sety(row3leds, 400)
    #pdb.set_trace()

    row1 = pg.sprite.Group()
    row2 = pg.sprite.Group()
    row3 = pg.sprite.Group()

    row1.add(r1)
    row2.add(r2)
    row3.add(r3)


    #row1.add(DT_year)
    #row1.add(DT_hr)
    #row1.add(DT_min)

    screen.blit(bground,(0,0))

    #(DT_month, DT_day, DT_year, DT_hr,DT_min)
    row1.draw(bground)
    row2.draw(bground)
    row3.draw(bground)


   

    #row3.draw(screen)

    #draw routine
    #screen.fill((0,0,0))
    #blink(led2,2)
    #screen.blit(led1.image,led1.rect)

    



    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            keybuffer.append(event.unicode)
            if len(keybuffer) == 2:
                print keybuffer[0:2]
                if "".join(keybuffer[0:2]) == "01":
                    DT_month.set("JAN")
                elif "".join(keybuffer[0:2]) == "02":
                    DT_month.set("FEB")
                elif "".join(keybuffer[0:2]) == "03":
                    DT_month.set("MAR")
                elif "".join(keybuffer[0:2]) == "04":
                    DT_month.set("APR")
                elif "".join(keybuffer[0:2]) == "05":
                    DT_month.set("MAY")
                elif "".join(keybuffer[0:2]) == "06":
                    DT_month.set("JUN")
                elif "".join(keybuffer[0:2]) == "07":
                    DT_month.set("JUL")
                elif "".join(keybuffer[0:2]) == "08":
                    DT_month.set("AUG")
                elif "".join(keybuffer[0:2]) == "09":
                    DT_month.set("SEP")
                elif "".join(keybuffer[0:2]) == "10":
                    DT_month.set("OCT")
                elif "".join(keybuffer[0:2]) == "11":
                    DT_month.set("NOV")
                elif "".join(keybuffer[0:2]) == "12":
                    DT_month.set("DEC")
                keybuffer = []


        elif event.type == pg.QUIT:
            running = 0


    


   