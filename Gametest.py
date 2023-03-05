import pygame, random, time, sys
print("Flappy Dolphin")
pygame.init()
clock = pygame.time.Clock()
fps = 60
screen_width = 720
screen_height = 648
screen = pygame.display.set_mode((screen_width, screen_height))
try:
    bg = pygame.image.load('BG2.png')
    pygame.display.set_icon(pygame.image.load("Dolphin.png"))
    bird = pygame.image.load("8bitD.png")
except:
    print(" I can't find the game files")
    print("Exiting...")
    pygame.quit()
    sys.exit()
pygame.font.init()
pygame.display.set_caption('Flappy Dolphin')
font, font2 = pygame.font.SysFont('Bauhaus', 72), pygame.font.SysFont('Bauhaus', 46)
title = font.render('Flappy Dolphin', True, (0,0,0), None)
caption = font2.render('Press SPACE to Start', True, (0,0,0), None)
global start, vel, ypos, hscore, p1, p2, tscore, died
start = False
vel = 0
ypos = 300
hscore = 0
pipe = [650,random.randint(0,380)]
tscore = 0
died = False
while True:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if start == False:
                    ypos = 300
                    start = True
                vel = 8.
    if start:
        screen.blit(bird,(50,ypos))
        ypos = ypos - vel
        vel = vel - 0.5
        pygame.draw.rect(screen,(0,120,120),(pipe[0],0,65,pipe[1]))
        pygame.draw.rect(screen,(0,120,120),(pipe[0],pipe[1]+300,65,720))
        screen.blit(font2.render('Score: ' + str(tscore), True, (0,0,0), None),(10,10))
        pipe[0] = pipe[0] - 5
        if pipe[0] < -50:
            pipe[0] = 720
            pipe[1] = random.randint(0,380)
            tscore = tscore + 1
            if tscore > hscore:
                hscore = tscore
    else:
        if died:
         screen.blit(title,(100,100))
        screen.blit(title,(100,100))
        screen.blit(caption,(100,300))
        screen.blit(font2.render('HIGH SCORE :  ' + str(hscore), True, (0,0,0), None),(100,400))
    if (pipe[0] < 164 and pipe[0] > 14) and (ypos+100 > pipe[1]+300 or ypos < pipe[1]):
        ypos = 528
        caption = font2.render('GAMEOVER', True, (0,0,0), None)
        start = False
        tscore = 0
        pipe[0] = 720
        died = True
    elif ypos < 0:
        ypos = 0
        vel = -abs(vel)
    clock.tick(fps)
    if time.time() - int(time.time()) < 0.02 and int(time.time()) % 5 == 0:
        print("FPS: " + str(int(clock.get_fps())))

    pygame.display.update()
    pygame.display.flip()