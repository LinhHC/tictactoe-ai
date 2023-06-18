import pygame
import sys
import tictactoe as ttt

pygame.init()

# screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic Tac Toe")

# colors
black = (0, 0, 0)
white = (255, 255, 255)

# game settings
go = True

while go:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    pygame.display.flip()
