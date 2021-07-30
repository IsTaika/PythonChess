import board
import pygame
import os


def click(position):
    x = position[0]
    y = position[1]
    if rez[0] < x < rez[0] + rez[2]:
        if rez[0] < y < rez[0] + rez[2]:
            x2 = x - rez[0]
            y2 = y - rez[0]
            i = round(x2 / (rez[2] / 8))
            j = round(y2 / (rez[2] / 8))
            return i, j
    else:
        return -1, -1


def main(window):
    run = True
    bo = board.Board(8, 8)
    boardimg = pygame.transform.scale(pygame.image.load(os.path.join("img", "board.png")), (752, 752))
    window.blit(boardimg, (0, 0))
    color = bo.turn
    bo.icon(window)
    pygame.display.update()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                i, j = click(pos)
                bo.select(i, j, color)


rez = [94, 94, 752, 752]
turn = 'w'
width = 752
height = 752
window = pygame.display.set_mode((width, height))
main(window)
