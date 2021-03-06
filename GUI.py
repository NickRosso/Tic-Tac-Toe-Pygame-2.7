#GUI module
import pygame
from pygame.locals import *

TEAL =  (193, 254, 212)
BLACK = (  0,   0,   0)
line_thickness = 2
X = "X"
O = "O"

Ximg = pygame.image.load("X.png")
Oimg = pygame.image.load("O.png")

def template(DISPLAY, board, Ximg, Oimg, coords):
    DISPLAY.fill(TEAL)
    pygame.draw.line(DISPLAY, BLACK, (100, 0),(100, 300), line_thickness)
    pygame.draw.line(DISPLAY, BLACK, (200, 0),(200, 300), line_thickness)
    pygame.draw.line(DISPLAY, BLACK, (0, 100),(300, 100), line_thickness)
    pygame.draw.line(DISPLAY, BLACK, (0, 200),(300, 200), line_thickness)

    for n in range(0,9):
        if board[n] == X:
            DISPLAY.blit(Ximg, (coords[n]))

        if board[n] == O:
            DISPLAY.blit(Oimg, (coords[n]))