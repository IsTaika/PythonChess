import board
import pygame

boardimg = pygame.transform.scale(pygame.image.load(('/img', 'board.png'))(1668, 1668))
rez = [146, 146, 1168, 1168]
turn = 'w'

def game(win):
