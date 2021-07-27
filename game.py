import board
import pygame

boardimg = pygame.transform.scale(pygame.image.load(('/img', 'board.png'))(1668, 1668))
rez = [146, 146, 1168, 1168]
turn = 'w'
width = "1280"
height = "720"
window = pygame.display.set_mode(width, height)
