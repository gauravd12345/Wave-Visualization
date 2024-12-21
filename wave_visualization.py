"""

UP ARROW KEY: zoom in
DOWN ARROW KEY: zoom out
LEFT ARROW KEY: decrease amplitude
RIGHT ARROW KEY: increase amplitude

"""



import pygame
import math
import time
import numpy as np

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

width = 1000
height = 800

pygame.init()
screen_size = (width, height)
start = int(time.time())

# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")
 
# clock is used to set a max fps
clock = pygame.time.Clock()
running = True


xPos = 50
draw_speed = 1


# Tweak these values to change the wave
amplitude = 100
frequency = 10
omega = frequency * 2 * 3.14
draw_speed_constant = 5

"""

Sign wave: (height / 2) + amplitude * math.sin(omega * xPos + end)
Square wave: (height / 2 + 40) + amplitude * math.copysign(1, math.sin(omega * xPos + end))

"""

font = pygame.font.Font('freesansbold.ttf', 32)
 
# create a text surface object,
# on which text is drawn on it.
text_ampl = font.render(("Amplitude: " + str(amplitude)), True, RED, WHITE)
text_om = font.render(("Omega: " + str(round(omega, 2))), True, RED, WHITE)

# create a rectangular object for the
# text surface object
textRect_ampl = text_ampl.get_rect()
textRect_om = text_om.get_rect()

# set the center of the rectangular object.
textRect_ampl.center = (width // 2, height // 8)
textRect_om.center = (width // 2, height // 6)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if(omega - 0.001 > 62.76):
            omega -= 0.001

    elif keys[pygame.K_RIGHT]:
        if(omega + 0.001 < 62.82):
            omega += 0.001
    
    elif keys[pygame.K_UP]:
        if(amplitude + 5 <= 200):
            amplitude += 5

    elif keys[pygame.K_DOWN]:
        if(amplitude - 5 >= 20):
            amplitude -= 5

    end = (time.time() - start) * draw_speed_constant
    screen.fill(BLACK)


    rectX = 50
    rectY = height / 4
    borderWidth = 5
    rX_size = 900
    rY_size = 500

    # Drawing the border
    pygame.draw.rect(screen, WHITE, pygame.Rect(rectX, rectY, rX_size, rY_size))
    pygame.draw.rect(screen, BLACK, pygame.Rect(rectX + borderWidth, rectY + borderWidth, rX_size - 10, rY_size - 10))


    # Rendering the texts
    text_ampl = font.render(("Amplitude: " + str(amplitude)), True, WHITE, RED)
    screen.blit(text_ampl, textRect_ampl)

    text_om = font.render(("Omega: " + str(round(omega, 2))), True, WHITE, RED)
    screen.blit(text_om, textRect_om)


    # Drawing the waves
    while(xPos < (width - 55)):
        # Sine Wave
        pygame.draw.rect(screen, WHITE, pygame.Rect(xPos, (height / 2 + 40) + amplitude * math.sin(omega * xPos + end), 5, 5))

        # Square Wave
        pygame.draw.rect(screen, WHITE, pygame.Rect(xPos, (height / 2 + 40) + amplitude * math.copysign(1, math.sin(omega * xPos + end)), 5, 5))
        
        # Triangle Wave
        #pygame.draw.rect(screen, WHITE, pygame.Rect(xPos, ((height / 2) - abs(amplitude * math.copysign(1, math.sin(omega + end)) - xPos)), 5, 5))

        xPos += draw_speed
    
    xPos = 50

    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(60)
 
pygame.quit()


