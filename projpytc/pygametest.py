import pygame

#init
game = pygame.init()
screen = pygame.display.set_mode((640,400))
running = 1
pic = pygame.image.load(r'c:\\python27\box.png')

#block
block = pygame.Surface((400,50))
block.fill((255,192,203))
block2 = pygame.Surface((200,20))
block2.fill((255,192,203))
rect1 = pygame.Rect((10,15, 75,65))



#Timing
#clock = pygame.time.Clock()
#FPS = 800

#Main
while running:
    
    for i in range(300):
        #clock.tick(FPS)
        screen.fill((0,0,0))
        screen.blit(pic,(i,20), area=rect1)
        screen.blit(block2,(i,100))
        pygame.display.flip()

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        running = 0