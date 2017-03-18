#Time circuit from BTTF
import pygame as pg
import collections
import pdb


#Tape
class tape(pg.sprite.Sprite):
    def __init__(self, startstate, col, background, fontsize):
        pg.sprite.Sprite.__init__(self)
        pg.font.init()
        self.font = pg.font.Font(r'c:\python27\projpytc\Dymo.ttf', fontsize)
        #font image
        self.fontpic = self.font.render(startstate, 1, col, background)
        #surface for font image, same size as font image
        self.image = pg.Surface((self.fontpic.get_rect().width, self.fontpic.get_rect().height-16))
        #paste font image onto surface
        self.image.blit(self.fontpic, (0,0), pg.Rect(0,10,200,30))
        self.rect = self.image.get_rect()
        self.irect = {'day':pg.Rect(0,0,120,62), 'month':pg.Rect(160,0,120,62)}

    def set(self, state):
        #Need to blit new image onto self.image
        self.image.blit(self.font.render(state, 1, (200,0,0),(0,0,0)),(0,0))
        return self.image

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

#TAPE2 Object
class tape2(pg.sprite.Sprite):
    def __init__(self, startstate, col, background, fontsize):
        pg.sprite.Sprite.__init__(self)
        pg.font.init()
        self.font = pg.font.Font(r'c:\python27\projpytc\microgram.ttf', fontsize)
        self.image = self.font.render(startstate, 1, col, background)
        self.rect = self.image.get_rect()
        self.irect = {'day':pg.Rect(0,0,120,62), 'month':pg.Rect(160,0,120,62)}

    def set(self, state):
        #Need to blit new image onto self.image
        self.image.blit(self.font.render(state, 1, (200,0,0),(0,0,0)),(0,0))
        return self.image

def createrow(resx, border, l1, l2,l3, l4, l5):
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
pg.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
game = pg.init()
screen = pg.display.set_mode((800,600))
running = 1
keybuffer = []

#Colours
TAPE_RED = (164, 44, 54)
WHITE = (255,255,255)
BLACK = (0,0,0)

#load bg image
bground = pg.image.load(r'c:\python27\projpytc\metalbackground800.jpg')

#load music and sound
pg.mixer.music.load(r'c:\python27\projpytc\opening.ogg')
pg.mixer.music.play()
keysound = pg.mixer.Sound(r'c:\python27\projpytc\key.ogg') 

#Create tape (txt, bg col, font col ) - topleft tuple describes tape location
DT_month_tape = tape("MONTH", TAPE_RED, (255,255,255),  40)
DT_month_tape.rect.topleft = (50,10)
DT_day_tape = tape("DAY", TAPE_RED, (255,255,255),  40)
DT_day_tape.rect.topleft = (220,11)
DT_year_tape = tape("YEAR", TAPE_RED, (255,255,255),  40)
DT_year_tape.rect.topleft = (390,10)
DT_hour_tape = tape("HOUR", TAPE_RED, (255,255,255),  40)
DT_hour_tape.rect.topleft = (575,10)
DT_min_tape = tape("MIN", TAPE_RED, (255,255,255),  40)
DT_min_tape.rect.topleft = (720,9)
DT_destination_tape = tape2("DEPARTED TIME", WHITE, BLACK,   30)
DT_destination_tape.rect.topleft = (250,120)


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
    r1 = sety(row1leds, 45)
    r2 = sety(row2leds, 210)
    r3 = sety(row3leds, 380)
    #pdb.set_trace()

    row1 = pg.sprite.Group()
    row2 = pg.sprite.Group()
    row3 = pg.sprite.Group()
    taperow1 = pg.sprite.Group()

    row1.add(r1)
    row2.add(r2)
    row3.add(r3)

    taperow1.add(DT_month_tape, DT_day_tape, DT_year_tape,DT_hour_tape,DT_min_tape, DT_destination_tape)


    #row1.add(DT_year)
    #row1.add(DT_hr)
    #row1.add(DT_min)

    screen.blit(bground,(0,0))

    #screen.blit(month.image,(20,45))

    #(DT_month, DT_day, DT_year, DT_hr,DT_min)
    row1.draw(bground)
    row2.draw(bground)
    row3.draw(bground)
    taperow1.draw(bground)


   

    #row3.draw(screen)

    #draw routine
    #screen.fill((0,0,0))
    #blink(led2,2)
    #screen.blit(led1.image,led1.rect)



    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            keysound.play()
            keybuffer.append(event.unicode)
            if len(keybuffer) == 12:
                print keybuffer[0:1]
                #Month
                if 0 < int("".join(keybuffer[0:2])) > 12: 
                    DT_month.set("Err")
                    keybuffer = []
                elif "".join(keybuffer[0:2]) == "01":
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
                #Day
                if 0< int("".join(keybuffer[2:4])) < 31: 
                    DT_day.set("".join(keybuffer[2:4]))
                else:
                    DT_day.set("Er")
                    keybuffer = []
                #Year
                if 0< int("".join(keybuffer[4:8])) < 9999: 
                    DT_year.set("".join(keybuffer[4:8]))
                else:
                    DT_year.set("Er")
                    keybuffer = []
               #Hour
                if 0< int("".join(keybuffer[8:10])) < 24: 
                    DT_hr.set(" " + "".join(keybuffer[8:10]))
                else:
                    DT_hr.set(" Er")
                    keybuffer = []
                #Min
                if 0< int("".join(keybuffer[10:])) < 60: 
                    DT_min.set("".join(keybuffer[10:]))
                else:
                    DT_min.set("Er")
                
                keybuffer = []


        elif event.type == pg.QUIT:
            running = 0


    


   