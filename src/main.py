import pygame
import sys
import tictactoe as ttt

pygame.init()

# screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic Tac Toe")

# font
retry_font = pygame.font.Font('font/OpenSans-Regular.ttf', 30)
game_font = pygame.font.Font('font/OpenSans-Regular.ttf', 60)

# colors
black = (0, 0, 0)
white = (255, 255, 255)

# game settings
go = True
board = ttt.initial_board()


def draw(d_board, d_tile):
    if d_board != ttt.EMPTY:
        move = game_font.render(d_board, True, white)
        moveRect = move.get_rect()
        moveRect.center = d_tile.center
        screen.blit(move, moveRect)


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

            # draw player moves
            if board[i][j] != ttt.EMPTY:
                draw(board[i][j], tile)

            row.append(tile)
        tiles.append(row)

    game_over = ttt.game_over(board)

    # players move
    player = ttt.player(board)
    pressed, _, _ = pygame.mouse.get_pressed()
    if pressed and not game_over:
        pos = pygame.mouse.get_pos()
        for i in range(3):
            for j in range(3):
                if board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(pos):
                    if player == ttt.X:
                        board[i][j] = ttt.X
                    else:
                        board[i][j] = ttt.O

    # reset game state
    if game_over:
        retryButton = pygame.Rect(screen_width / 3, tile_size * 4 + (tile_size - 50) / 2, screen_width / 3, 50)
        pygame.draw.rect(screen, white, retryButton)

        retry = retry_font.render("Retry", True, black)
        retryRect = retry.get_rect()
        retryRect.center = retryButton.center
        screen.blit(retry, retryRect)

        pressed, _, _ = pygame.mouse.get_pressed()
        if pressed:
            pos = pygame.mouse.get_pos()
            if retryButton.collidepoint(pos):
                board = ttt.initial_board()

    pygame.display.flip()
