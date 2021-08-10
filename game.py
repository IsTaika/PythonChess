import board
import pygame
import os
import time
import interface


def menu(window):
    run = True

    clock = pygame.time.Clock()
    while run:
        fps = clock.tick(30)
        menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("img", "background.jpg")), (752, 752))
        window.blit(menu_bg, (0, 0))
        button1 = interface.Button(
            "Start game",
            (50, 100),
            font=30,
            bg='navy',
            feedback='you clicked me'
        )
        button1.show(window, button1)
        button2 = interface.Button(
            "Registration",
            (50, 200),
            font=30,
            bg='navy',
            feedback='you clicked me'
        )
        button2.show(window, button2)
        inputbox = interface.InputBox(50, 300, 10, 100, text='login')
        inputbox.draw(window)
        inputbox.update()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()
                    if button1.rect.collidepoint(x, y):
                        main(window)


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
    print(j, ' ', i)
    if -1 < i < 8:
        if -1 < j < 9:
            return j, i


def window_update(window, bo):
    boardimg = pygame.transform.scale(pygame.image.load(os.path.join("img", "board.png")), (752, 752))
    window.blit(boardimg, (0, 0))
    bo.icon(window)
    pygame.display.update()


def main(window):
    run = True
    bo = board.Board(8, 8)
    bo.update_moves()
    clock = pygame.time.Clock()
    while run:
        clock.tick(30)
        window_update(window, bo)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                color = bo.turn
                pos = pygame.mouse.get_pos()
                i, j = click(pos)
                print("TEST", i, " ", j, " ", color)
                bo.select(i, j, color)


rez = [94, 94, 752, 752]
width = 752
height = 752
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Python chess")
menu(window)
