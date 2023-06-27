import time
import pygame
import sys
import tictactoe as ttt

pygame.init()

# screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic Tac Toe")

# fonts
button_font = pygame.font.Font('font/OpenSans-Regular.ttf', 30)
game_font = pygame.font.Font('font/OpenSans-Regular.ttf', 40)
move_font = pygame.font.Font('font/OpenSans-Regular.ttf', 60)
menu_font = pygame.font.Font('font/OpenSans-Regular.ttf', 70)

# colors
black = (0, 0, 0)
white = (255, 255, 255)

# game settings
go = True
board = ttt.initial_board()
user = None
ai_turn = False


# game loop
while go:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    if user is None:

        # menu title
        menu_title = menu_font.render("Tic Tac Toe", True, white)
        menuRect = menu_title.get_rect()
        menuRect.center = ((screen_width / 2), 100)
        screen.blit(menu_title, menuRect)

        # buttons
        x_button = pygame.Rect((screen_width / 8), (screen_height / 2), screen_width / 3, 50)
        x_txt = button_font.render("Play as X", True, black)
        x_txt_rect = x_txt.get_rect()
        x_txt_rect.center = x_button.center

        o_button = pygame.Rect(13/24 * screen_width, (screen_height / 2), screen_width / 3, 50)
        o_txt = button_font.render("Play as O", True, black)
        o_txt_rect = o_txt.get_rect()
        o_txt_rect.center = o_button.center

        pygame.draw.rect(screen, white, x_button)
        pygame.draw.rect(screen, white, o_button)
        screen.blit(x_txt, x_txt_rect)
        screen.blit(o_txt, o_txt_rect)

        # choose a user
        menu_pressed, _, _ = pygame.mouse.get_pressed()
        if menu_pressed:
            pos = pygame.mouse.get_pos()
            if x_button.collidepoint(pos):
                time.sleep(0.1)
                user = ttt.X
            elif o_button.collidepoint(pos):
                time.sleep(0.1)
                user = ttt.O

    else:

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
                    move = move_font.render(board[i][j], True, white)
                    moveRect = move.get_rect()
                    moveRect.center = tile.center
                    screen.blit(move, moveRect)

                row.append(tile)
            tiles.append(row)

        player = ttt.player(board)
        game_over = ttt.game_over(board)

        # game ongoing
        if not game_over:

            # title text
            if player != user:
                player_text = game_font.render(f"AI calculating next move...", True, white)
            else:
                player_text = game_font.render(f"Turn: Player {player}", True, white)

            playerRect = player_text.get_rect()
            playerRect.center = (screen_width / 2, tile_size / 2)
            screen.blit(player_text, playerRect)

            # ai turn
            if player != user:
                if ai_turn:
                    time.sleep(1)
                    move = ttt.minimax(board)
                    board[move[0]][move[1]] = player
                    ai_turn = False
                else:
                    ai_turn = True

            # player's turn
            else:
                pressed, _, _ = pygame.mouse.get_pressed()
                if pressed and not game_over:
                    pos = pygame.mouse.get_pos()
                    for i in range(3):
                        for j in range(3):
                            if board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(pos):
                                board[i][j] = player

        # reset game state
        if game_over:

            retryButton = pygame.Rect(screen_width / 3, tile_size * 4 + (tile_size - 50) / 2, screen_width / 3, 50)
            pygame.draw.rect(screen, white, retryButton)

            winner = ttt.winner(board)

            # reset button
            retry = button_font.render("Retry", True, black)
            retryRect = retry.get_rect()
            retryRect.center = retryButton.center
            screen.blit(retry, retryRect)

            # title: game over and game result
            if winner is not None:
                gameover_text = game_font.render(f"Game Over: Player {winner} wins", True, white)
            else:
                gameover_text = game_font.render(f"Game Over: Tie", True, white)

            gameoverRect = gameover_text.get_rect()
            gameoverRect.center = (screen_width / 2, tile_size / 2)
            screen.blit(gameover_text, gameoverRect)

            # reset board
            pressed, _, _ = pygame.mouse.get_pressed()
            if pressed:
                pos = pygame.mouse.get_pos()
                if retryButton.collidepoint(pos):
                    board = ttt.initial_board()
                    user = None

    pygame.display.flip()
