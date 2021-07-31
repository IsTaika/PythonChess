import board
import pygame
import os


def click(position):
    print(position)
    rez = [94, 94, 752, 752]
    x = position[0]
    y = position[1]
    i, j = 0, 0
    if rez[0] < x < rez[0] + rez[2]:
        i = int(x // (rez[2] / 8))
    if rez[0] < y < rez[0] + rez[3]:
        j = int(y // (rez[3] / 8))
    print(i, ' ', j)
    return i, j


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
