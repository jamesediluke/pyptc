#Time circuit from BTTF
import pygame as pg
import collections
import pdb
import random
import time


#Tape - good for DYMO.ttf
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

#TAPE2 Object
class tape2(pg.sprite.Sprite):
    def __init__(self, startstate, col, background, fontsize):
        pg.sprite.Sprite.__init__(self)
        pg.font.init()
        self.font = pg.font.Font(r'c:\python27\projpytc\microgram.ttf', fontsize)
        self.font.set_bold(True)
        self.fontpic = self.font.render(startstate, 1, col, background)
        self.image = pg.Surface((self.fontpic.get_rect().width + 3, self.fontpic.get_rect().height + 5))
        self.image.fill(background)
        #paste font image onto surface
        self.image.blit(self.fontpic, (1,3))
        self.rect = self.image.get_rect()
        self.irect = {'day':pg.Rect(0,0,120,62), 'month':pg.Rect(160,0,120,62)}

    def set(self, state):
        #Need to blit new image onto self.image
        self.image.blit(self.font.render(state, 1, (200,0,0),(0,0,0)),(0,0))
        return self.image

#LED Object
class led14(pg.sprite.Sprite):
    def __init__(self, startstate, col, background, TransBG = False):
        pg.sprite.Sprite.__init__(self)
        pg.font.init()
        self.font = pg.font.Font(r'c:\python27\projpytc\DSEG14Modern-Italic.ttf', 64)
        self.image = self.font.render(startstate, 1, col, background)
        if TransBG:
            self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.irect = {'day':pg.Rect(0,0,120,62), 'month':pg.Rect(160,0,120,62)}

    def set(self, state):
        #Need to blit new image onto self.image
        self.image.blit(self.font.render(state, 1, (200,0,0),(0,0,0)),(0,0))
        return self.image

#LED TESTNG  Object - not for live code
class ledBG(pg.sprite.Sprite):
    def __init__(self, startstate, col, background):
        pg.sprite.Sprite.__init__(self)
        pg.font.init()
        self.font = pg.font.Font(r'c:\python27\projpytc\DSEG14Modern-Italic.ttf', 64)
        self.image = self.font.render(startstate, 1, col, background)
        #self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.irect = {'day':pg.Rect(0,0,120,62), 'month':pg.Rect(160,0,120,62)}

    def set(self, state):
        #Need to blit new image onto self.image
        self.image.blit(self.font.render(state, 1, (200,0,0),(0,0,0)),(0,0))
        return self.image

#Ajust screen x location
def createrow(resx, border, l1, l2,l3, l4, l5):
    l1.rect.x = 5
    l2.rect.x=  l1.rect.x + l1.image.get_width() + border
    l3.rect.x = l2.rect.x + l2.image.get_width() + border 
    l4.rect.x = l3.rect.x + l3.image.get_width() + border + border + 5
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

#All INT (yr, mon, hr, min, sec, wday)

#Colours
TAPE_RED = (164, 44, 54)
WHITE = (255,255,255)
BLACK = (0,0,0)
LEDREDBG = (50,0,0)
LEDRED = (220,0,0)
LEDGREENBG = (0,40,0)
LEDYELLOWBG = (40,0,40)

#load bg image
bground = pg.image.load(r'c:\python27\projpytc\metalbackground800.jpg')

#load music and sound
pg.mixer.music.load(r'c:\python27\projpytc\opening.ogg')
pg.mixer.music.play()
keysound = pg.mixer.Sound(r'c:\python27\projpytc\key.ogg') 

#Create tape (txt, bg col, font col ) - topleft tuple describes tape location
DT_month_tape = tape2("MONTH", WHITE, TAPE_RED,  25)
DT_month_tape.rect.topleft = (15,10)
DT_day_tape = tape2("DAY", WHITE, TAPE_RED,  25)
DT_day_tape.rect.topleft = (190,11)
DT_year_tape = tape2("YEAR", WHITE, TAPE_RED,  25)
DT_year_tape.rect.topleft = (360,10)
DT_hour_tape = tape2("HOUR", WHITE, TAPE_RED,  25)
DT_hour_tape.rect.topleft = (575,10)
DT_min_tape = tape2("MIN", WHITE, TAPE_RED,  25)
DT_min_tape.rect.topleft = (720,9)
DT_destination_tape = tape2("DEPARTED TIME", WHITE, BLACK,   25)
DT_destination_tape.rect.topleft = (250,120)

PT_month_tape = tape2("MONTH", WHITE, TAPE_RED,  25)
PT_month_tape.rect.topleft = (14,178)
PT_day_tape = tape2("DAY", WHITE, TAPE_RED,  25)
PT_day_tape.rect.topleft = (190,177)
PT_year_tape = tape2("YEAR", WHITE, TAPE_RED,  25)
PT_year_tape.rect.topleft = (360,178)
PT_hour_tape = tape2("HOUR", WHITE, TAPE_RED,  25)
PT_hour_tape.rect.topleft = (575,179)
PT_min_tape = tape2("MIN", WHITE, TAPE_RED,  25)
PT_min_tape.rect.topleft = (720,172)
PT_destination_tape = tape2("PRESENT TIME", WHITE, BLACK,   27)
PT_destination_tape.rect.topleft = (261,290)

TD_month_tape = tape2("MONTH", WHITE, TAPE_RED,  25)
TD_month_tape.rect.topleft = (14,346)
TD_day_tape = tape2("DAY", WHITE, TAPE_RED,  25)
TD_day_tape.rect.topleft = (190,346)
TD_year_tape = tape2("YEAR", WHITE, TAPE_RED,  25)
TD_year_tape.rect.topleft = (360,346)
TD_hour_tape = tape2("HOUR", WHITE, TAPE_RED,  25)
TD_hour_tape.rect.topleft = (575,346)
TD_min_tape = tape2("MIN", WHITE, TAPE_RED,  25)
TD_min_tape.rect.topleft = (720,346)
TD_destination_tape = tape2("TIME DEPARTED", WHITE, BLACK,   27)
TD_destination_tape.rect.topleft = (261,460)

#create led objects
#input {month, day, year, hr, min}

#DEPART TIME
#DT BACKGROUND
DT_monthBG = led14("000", LEDREDBG,(0,0,0))
DT_dayBG = led14("00", LEDREDBG,(0,0,0))
DT_yearBG = led14("0000", LEDREDBG,(0,0,0))
DT_hrBG = led14(" 00", LEDREDBG,(0,0,0))
DT_minBG = led14("00", LEDREDBG,(0,0,0))
DT_monthBGA = led14("***", LEDRED,(0,0,0), True)
DT_dayBGA = led14("**", LEDRED,(0,0,0), True)
DT_yearBGA = led14("****", LEDRED,(0,0,0), True)
DT_hrBGA = led14(" **", LEDRED,(0,0,0), True)
DT_minBGA = led14("**", LEDRED,(0,0,0), True)

#Disp
DT_month = led14("Feb", LEDRED,(0,0,0), True)
DT_day = led14("06", LEDRED,(0,0,0), True)
DT_year = led14("1955", LEDRED,(0,0,0), True)
DT_hr = led14(" 04", LEDRED,(0,0,0), True)
DT_min = led14("55", LEDRED,(0,0,0), True)


#CT BACKGROUND
PT_monthBG = led14("000", LEDGREENBG,(0,0,0))
PT_dayBG = led14("00", LEDGREENBG,(0,0,0))
PT_yearBG = led14("0000", LEDGREENBG,(0,0,0))
PT_hrBG = led14(" 00", LEDGREENBG,(0,0,0))
PT_minBG = led14("00", LEDGREENBG,(0,0,0))
PT_monthBGA = led14("***", LEDGREENBG,(0,0,0), True)
PT_dayBGA = led14("**", LEDGREENBG,(0,0,0), True)
PT_yearBGA = led14("****", LEDGREENBG,(0,0,0), True)
PT_hrBGA = led14(" **", LEDGREENBG,(0,0,0), True)
PT_minBGA = led14("**", LEDGREENBG,(0,0,0), True)
#CURRENT TIME
PT_month = led14("Mar", (0,220,0),(0,0,0), True)
PT_day = led14("06", (0,220,0),(0,0,0), True)
PT_year = led14("1955", (0,220,0),(0,0,0), True)
PT_hr = led14(" 04", (0,220,0),(0,0,0), True)
PT_min = led14("55", (0,220,0),(0,0,0), True)

#TIME DEP
TD_monthBG = led14("000", LEDYELLOWBG,(0,0,0))
TD_dayBG = led14("00", LEDYELLOWBG,(0,0,0))
TD_yearBG = led14("0000", LEDYELLOWBG,(0,0,0))
TD_hrBG = led14(" 00", LEDYELLOWBG,(0,0,0))
TD_minBG = led14("00", LEDYELLOWBG,(0,0,0))
TD_monthBGA = led14("***", LEDYELLOWBG,(0,0,0), True)
TD_dayBGA = led14("**", LEDYELLOWBG,(0,0,0), True)
TD_yearBGA = led14("****", LEDYELLOWBG,(0,0,0), True)
TD_hrBGA = led14(" **", LEDYELLOWBG,(0,0,0), True)
TD_minBGA = led14("**", LEDYELLOWBG,(0,0,0), True)

TD_month = led14("Mar", (150,150,0),(0,0,0), True)
TD_day = led14("06", (150,150,0),(0,0,0), True)
TD_year = led14("1955", (150,150,0),(0,0,0), True)
TD_hr = led14(" 04", (150,150,0),(0,0,0), True)
TD_min = led14("55", (150,150,0),(0,0,0), True)

#Create LEDs in Tuples, spaced for rows
row1ledsBG = createrow(800, 20, DT_monthBG, DT_dayBG, DT_yearBG, DT_hrBG,DT_minBG)
row1ledsBGA = createrow(800, 20, DT_monthBGA, DT_dayBGA, DT_yearBGA, DT_hrBGA,DT_minBGA)

row2ledsBG = createrow(800, 20, PT_monthBG, PT_dayBG, PT_yearBG, PT_hrBG,PT_minBG)
row2ledsBGA = createrow(800, 20, PT_monthBGA, PT_dayBGA, PT_yearBGA, PT_hrBGA,PT_minBGA)

row3ledsBG = createrow(800, 20, TD_monthBG, TD_dayBG, TD_yearBG, TD_hrBG, TD_minBG)
row3ledsBGA = createrow(800, 20, TD_monthBGA, TD_dayBGA, TD_yearBGA, TD_hrBGA, TD_minBGA)

row1leds = createrow(800, 20, DT_month, DT_day, DT_year, DT_hr,DT_min)
row2leds = createrow(800, 20, PT_month, PT_day, PT_year, PT_hr, PT_min)
row3leds = createrow(800, 20, TD_month, TD_day, TD_year, TD_hr, TD_min)

#Set Y coord for line
r1BG = sety(row1ledsBG, 45)
r1BGA = sety(row1ledsBG, 45)
r1 = sety(row1leds, 45)

r2BG = sety(row2ledsBG, 210)
r2BGA = sety(row2ledsBG, 210)
r2 = sety(row2leds, 210)

r3BG = sety(row3ledsBG, 380)
r3BGA = sety(row3ledsBG, 380)
r3 = sety(row3leds, 380)
#pdb.set_trace()

while running:

    localtime = time.localtime(time.time())
    rtime = time.asctime(localtime)
    print rtime


    clock = pg.time.Clock()
    clock.tick(500)
    
    clock.tick(500)
    

    #Insantiate sprite groups
    row1BG = pg.sprite.Group()
    row2BG = pg.sprite.Group()
    row3BG = pg.sprite.Group()
    row1 = pg.sprite.Group()
    row2 = pg.sprite.Group()
    row3 = pg.sprite.Group()
    taperow1 = pg.sprite.Group()
    taperow2 = pg.sprite.Group()
    taperow3 = pg.sprite.Group()

    row1BG.add(r1BG,r1BGA) 
    row2BG.add(r2BG,r2BGA)
    row3BG.add(r3BG,r3BGA)  
    row1.add(r1)
    row2.add(r2)
    row3.add(r3)

    taperow1.add(DT_month_tape, DT_day_tape, DT_year_tape,DT_hour_tape,DT_min_tape, DT_destination_tape)
    taperow2.add(PT_month_tape, PT_day_tape, PT_year_tape,PT_hour_tape,PT_min_tape, PT_destination_tape)
    taperow3.add(TD_month_tape, TD_day_tape, TD_year_tape,TD_hour_tape,TD_min_tape, TD_destination_tape)

    #row1.add(DT_year)
    #row1.add(DT_hr)
    #row1.add(DT_min)

    screen.blit(bground,(0,0))

    #screen.blit(month.image,(20,45))

    #test bg
    #screen.blit(DT_month_bck.image,(5,45))

    #(DT_month, DT_day, DT_year, DT_hr,DT_min)
    row1BG.draw(bground)
    row1.draw(bground)

    row2BG.draw(bground)
    row2.draw(bground)

    row3BG.draw(bground)
    row3.draw(bground)

    taperow1.draw(bground)
    taperow2.draw(bground)
    taperow3.draw(bground)



   

    #row3.draw(screen)

    #draw routine
    #screen.fill((0,0,0))
    #blink(led2,2)
    #screen.blit(led1.image,led1.rect)

    '''EXPERIMENTAL LIGHTING
    redch = random.randint(0,255)
    greench = random.randint(0,255)
    bluech = random.randint(0,255)
    #light = pg.image.load(r'c:\python27\projpytc\circ.png')
    light = pg.surface.Surface((600,480))
    light.fill((redch,greench,bluech))
    filter = pg.surface.Surface((640, 480))
    filter.fill(pg.color.Color('White'))
    #filter.blit(light, map(lambda x: x-50, pg.mouse.get_pos()))
    filter.blit(light, (0,0))
    screen.blit(filter, (0, 0), special_flags=pg.BLEND_RGBA_SUB)'''



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


    


   