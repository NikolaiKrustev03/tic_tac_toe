import random

import pygame

pygame.init()

screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic-Tac-Toe")

line_width = 4
markers_list = []
clicked = False
mouse_pos = []
player = 1
winner = 0
game_over = False

blue = (0, 0, 255)
red = (255, 0, 0)

font = pygame.font.SysFont(None, 40)

again_rect = pygame.Rect((screen_width // 2 - 80, screen_height // 2, 160, 50))


def draw_grid():
    bg_color = (255, 255, 255)
    screen.fill(bg_color)
    grid = (0, 0, 0)
    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, x * 100), (screen_width, x * 100), line_width)
        pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, screen_height), line_width)


for i in range(3):
    row = [0] * 3
    markers_list.append(row)


def draw_markers():
    x_pos = 0
    for x in markers_list:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, red, (x_pos * 100 + 15, y_pos * 100 + 15),
                                 (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                pygame.draw.line(screen, red, (x_pos * 100 + 15, y_pos * 100 + 85),
                                 (x_pos * 100 + 85, y_pos * 100 + 15), line_width)
            if y == -1:
                pygame.draw.circle(screen, blue, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
            y_pos += 1
        x_pos += 1


def check_winner():
    global winner
    global game_over
    y_pos = 0
    for x in markers_list:
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True
        if markers_list[0][y_pos] + markers_list[1][y_pos] + markers_list[2][y_pos] == 3:
            winner = 1
            game_over = True
        if markers_list[0][y_pos] + markers_list[1][y_pos] + markers_list[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1

        if markers_list[0][0] + markers_list[1][1] + markers_list[2][2] == 3 or \
                markers_list[2][0] + markers_list[1][1] + markers_list[0][2] == 3:
            winner = 1
            game_over = True
        if markers_list[0][0] + markers_list[1][1] + markers_list[2][2] == -3 or \
                markers_list[2][0] + markers_list[1][1] + markers_list[0][2] == -3:
            winner = 2
            game_over = True


def draw_winner():
    win_text = f"Player {str(winner)} wins!"
    win_img = font.render(win_text, True, (0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50))
    screen.blit(win_img, (screen_width // 2 - 100, screen_height // 2 - 50))

    again_text = "Play again?"
    again_img = font.render(again_text, True, (0, 255, 0))
    pygame.draw.rect(screen, blue, again_rect)
    screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 + 10))


def full_board():
    for x in markers_list:
        if 0 in x:
            return False
    return True


run = True
while run:
    draw_grid()
    draw_markers()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if not game_over:
            if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked:
                clicked = False
                mouse_pos = pygame.mouse.get_pos()
                cell_x = mouse_pos[0] // 100
                cell_y = mouse_pos[1] // 100
                if markers_list[cell_x][cell_y] == 0:
                    markers_list[cell_x][cell_y] = player
                    player *= -1
                    check_winner()
                    if full_board():
                        # Reset the game if the board is full
                        markers_list = [[0] * 3 for _ in range(3)]
                        player = random.choice([-1, 1])
                        winner = 0
                        game_over = False

    if game_over:
        draw_winner()
        if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked:
            clicked = False
            mouse_pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(mouse_pos):
                markers_list = [[0] * 3 for _ in range(3)]
                mouse_pos = []
                player = random.choice([-1, 1])
                winner = 0
                game_over = False

    pygame.display.update()

pygame.quit()
