# pygame template

import pygame
from pygame.locals import KEYDOWN, K_SPACE, K_RETURN, K_0, K_LEFT, K_RIGHT
import random

pygame.init()
pygame.font.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

font = pygame.font.SysFont('Aller', 18) # font, not sure if every computer has this by default so feel free to change it
showText = 1

# position variables (static)
house_x = 200
house_y = 210
trees_x = 20
trees_y = 275

# position variables (non-static)
moon_x = -30 # the moon rises in the east but this feels more correct from a viewer's perspective
moon_y = 60
sun_x = -30
sun_y = 60
smoke_x = 380
smoke_y = 120

# misc variables
night = 1 # script starts at night since i'm too lazy to change it to day
smokeOnScreen = 0 # if this is 1 then new smoke won't be created until the existing one floats off screen
smokeCounters = 60 # was originally going to do something else with this (which is why it exists instead of just when y is 0) but ran out of time
starsGenerated = 0
cloudsGenerated = 0
cloudAmount = 0

animationSpeed = 2 # speed of moon

# star generation setup (code won't work if this isn't generated before the actual loop starts)
stars_x = []
stars_y = []
for i in range(15):
    stars_x.append(random.randint(0, 640))
    stars_y.append(random.randint(20, 100))
starsGenerated = 1
# print(stars_x)
# print(stars_y)

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                showText = 0
            if event.key== K_0:
                if night == 1:
                    moon_x += 800
                else:
                    sun_x += 800
            elif event.key == K_RETURN:
                night = 1
                showText = 0
                moon_x = -20
                animationSpeed = 2
                stars_x = []
                stars_y = []
                for i in range(15):
                    stars_x.append(random.randint(0, 640))
                    stars_y.append(random.randint(20, 100))
                smokeCounters = 60
                smokeOnScreen = 0
            elif event.key == K_LEFT and animationSpeed > 0:
                animationSpeed -= 1
            elif event.key == K_RIGHT and animationSpeed < 20:
                animationSpeed += 1

                #reset animation here. wip
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    if sun_x > 680:
        night = 1
        cloudsGenerated = 0
    elif moon_x > 680:
        night = 0
        starsGenerated = 0

    # print(moon_x) # test

    if night == 1:
        moon_x += animationSpeed
    else:
        sun_x += animationSpeed

    if night == 1: # color stuff, if night
        sun_x = -30
        backgroundColor = (20, 25, 100)
        groundColor = (25, 90, 0)
        hillColor = (15, 60, 0)
        houseColor = (130, 60, 15)
        houseRoofColor = (120, 0, 10)
        windowColor = (255, 230, 0)
        bushColor = (25, 100, 0)
        berryColor = (125, 30, 30)
        doorColor = (115, 50, 0)
        treeTrunkColor = (90, 35, 0)
        chimneyColor = (70, 70, 70)
    else: # if day
        moon_x = -30
        backgroundColor = (75, 170, 250)
        groundColor = (50, 180, 0)
        hillColor = (30, 90, 0)
        houseColor = (210, 100, 25)
        houseRoofColor = (215, 0, 20)
        windowColor = (150, 250, 250)
        bushColor = (45, 150, 0)
        berryColor = (200, 30, 30)
        doorColor = (190, 80, 0)
        treeTrunkColor = (135, 50, 0)
        chimneyColor = (100, 100, 100)

    # DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command

    pygame.draw.rect(screen, backgroundColor, (0, 0, 640, 480)) # background
    pygame.draw.circle(screen, hillColor, (145, 380), 100) # "hills"
    pygame.draw.circle(screen, hillColor, (560, 380), 100)
    pygame.draw.rect(screen, groundColor, (0, 360, 640, 120)) # ground
    
    if night == 1:
        pygame.draw.circle(screen, (235, 235, 235), (moon_x, moon_y), 30) # moon
        pygame.draw.circle(screen, (20, 25, 100), (moon_x + 6, moon_y + 3), 25) # crescent
    else:
        pygame.draw.circle(screen, (255, 230, 40), (sun_x, sun_y), 30)
        pygame.draw.circle(screen, (255, 60, 40), (sun_x, sun_y), 20)

    # house code
    pygame.draw.rect(screen, houseColor, (house_x, house_y, 240, 150)) # house body
    pygame.draw.polygon(screen, chimneyColor, ((house_x + 160, house_y - 70), (house_x + 160, house_y - 90), (house_x + 200, house_y - 90), (house_x + 200, house_y - 30))) # chimney thing
    pygame.draw.polygon(screen, houseRoofColor, ((house_x, house_y), (house_x + 240, house_y), (house_x + 120, house_y - 110))) # house roof
    pygame.draw.rect(screen, windowColor, (house_x + 30, house_y + 50, 25, 25)) # window stuff
    pygame.draw.rect(screen, windowColor, (house_x + 60, house_y + 50, 25, 25))
    pygame.draw.rect(screen, windowColor, (house_x + 30, house_y + 20, 25, 25))
    pygame.draw.rect(screen, windowColor, (house_x + 60, house_y + 20, 25, 25))
    pygame.draw.rect(screen, doorColor, (house_x + 180, house_y + 80, 40, 70)) # door
    pygame.draw.circle(screen, (20, 20, 20), (house_x + 190, house_y + 120), 5) # doorknob

    # other stuff
    pygame.draw.circle(screen, bushColor, (100, 370), 30) # bush
    pygame.draw.circle(screen, berryColor, (104, 356), 5) # berry 1
    pygame.draw.circle(screen, berryColor, (87, 367), 5) # berry 2
    pygame.draw.circle(screen, berryColor, (107, 382), 5) # berry 3
    pygame.draw.circle(screen, bushColor, (550, 370), 30) # bush 2
    pygame.draw.circle(screen, berryColor, (554, 356), 5) # berry 4
    pygame.draw.circle(screen, berryColor, (537, 367), 5) # berry 5
    pygame.draw.circle(screen, berryColor, (557, 382), 5) # berry 6

    pygame.draw.rect(screen, treeTrunkColor, (trees_x, trees_y + 30, 20, 55)) # tree trunk 1 (default position)
    pygame.draw.polygon(screen, bushColor, ((trees_x - 10, trees_y + 40), (trees_x + 30, trees_y + 40), (trees_x + 10, trees_y + 20))) # tree leaves 1
    pygame.draw.polygon(screen, bushColor, ((trees_x - 10, trees_y + 50), (trees_x + 30, trees_y + 50), (trees_x + 10, trees_y + 30))) # tree leaves 2
    pygame.draw.polygon(screen, bushColor, ((trees_x - 10, trees_y + 60), (trees_x + 30, trees_y + 60), (trees_x + 10, trees_y + 40))) # tree leaves 3
    pygame.draw.rect(screen, treeTrunkColor, (trees_x + 120, trees_y + 30, 20, 55)) # tree trunk 2 (+120)
    pygame.draw.polygon(screen, bushColor, ((trees_x + 110, trees_y + 40), (trees_x + 150, trees_y + 40), (trees_x + 130, trees_y + 20))) # tree leaves 4
    pygame.draw.polygon(screen, bushColor, ((trees_x + 110, trees_y + 50), (trees_x + 150, trees_y + 50), (trees_x + 130, trees_y + 30))) # tree leaves 5
    pygame.draw.polygon(screen, bushColor, ((trees_x + 110, trees_y + 60), (trees_x + 150, trees_y + 60), (trees_x + 130, trees_y + 40))) # tree leaves 6
    pygame.draw.rect(screen, treeTrunkColor, (trees_x + 580, trees_y + 30, 20, 55)) # tree trunk 3 (+580)
    pygame.draw.polygon(screen, bushColor, ((trees_x + 570, trees_y + 40), (trees_x + 610, trees_y + 40), (trees_x + 590, trees_y + 20))) # tree leaves 7
    pygame.draw.polygon(screen, bushColor, ((trees_x + 570, trees_y + 50), (trees_x + 610, trees_y + 50), (trees_x + 590, trees_y + 30))) # tree leaves 8
    pygame.draw.polygon(screen, bushColor, ((trees_x + 570, trees_y + 60), (trees_x + 610, trees_y + 60), (trees_x + 590, trees_y + 40))) # tree leaves 9

    if night == 1: # clouds code (generation before showing them later), displaying stars on screen
        for i in range(15):
            pygame.draw.circle(screen, (255, 255, 255), (stars_x[i], stars_y[i]), 3)

        if cloudsGenerated == 0:
            clouds_x = []
            clouds_y = []
            for i in range(random.randint(1, 6)): # generate a random # of clouds between 1 and 5 (might not show any clouds)
                cloudAmount = i
                clouds_x.append(random.randint(20, 600))
                clouds_y.append(random.randint(20, 101))
    else: # stars code (generation), displaying clouds on screen
        for i in range(cloudAmount):
            pygame.draw.circle(screen, (250, 250, 250), (clouds_x[i], clouds_y[i]), 13)
            pygame.draw.circle(screen, (250, 250, 250), (clouds_x[i] + 10, clouds_y[i]), 13)
            pygame.draw.circle(screen, (250, 250, 250), (clouds_x[i] - 10, clouds_y[i]), 13)
            pygame.draw.circle(screen, (250, 250, 250), (clouds_x[i] - 5, clouds_y[i] - 10), 13)
            pygame.draw.circle(screen, (250, 250, 250), (clouds_x[i] + 6, clouds_y[i] - 6), 13)

        if starsGenerated == 0:
            stars_x = []
            stars_y = []
            for i in range(15):
                stars_x.append(random.randint(0, 641))
                stars_y.append(random.randint(20, 101))
            starsGenerated = 1

    if smokeOnScreen == 0: # smoke code
        smoke_x = 380
        smoke_y = 120
        smokeCounters = 60
        if random.randint(1,50) == 1:
            smokeOnScreen = 1
    elif smokeOnScreen == 1:
        pygame.draw.circle(screen, (50, 50, 50), (smoke_x, smoke_y), 13) # smoke outline
        pygame.draw.circle(screen, (70, 70, 70), (smoke_x, smoke_y), 12) # smoke
        smoke_x += random.randrange(-1,3)
        if smokeCounters <= 0:
            smokeOnScreen = 0
        else:
            smoke_y -= 2
            smokeCounters -= 1

    if showText == 1:
        introText = font.render("Press enter/return to reset animation, use left and right arrows to speed up/slow down sun/moon (space to hide)", False, (255, 255, 255))
        screen.blit(introText, (0, 0))

    #print(time) # time was originally going to be handled with the user pressing spacebar but it got scrapped

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()