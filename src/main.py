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

    # draw board
    board_size = 360
    tile_size = board_size / 3
    tiles = []
    for i in range(3):
        row = []
        for j in range(3):
            tile = pygame.Rect((screen_width - board_size) / 2 + i * tile_size,
                               (screen_height - board_size) / 2 + j * tile_size, tile_size, tile_size)
            pygame.draw.rect(screen, white, tile, 3)
            row.append(tile)
        tiles.append(row)

    pygame.display.flip()
