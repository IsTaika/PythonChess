import pygame
import os

b_pawn = pygame.image.load(os.path.join('img', 'black_pawn.png'))
b_king = pygame.image.load(os.path.join('img', 'black_king.png'))
b_queen = pygame.image.load(os.path.join('img', 'black_queen.png'))
b_bishop = pygame.image.load(os.path.join('img', 'black_bishop.png'))
b_rook = pygame.image.load(os.path.join('img', 'black_rook.png'))
b_knight = pygame.image.load(os.path.join('img', 'black_knight.png'))

w_pawn = pygame.image.load(os.path.join('img', 'white_pawn.png'))
w_king = pygame.image.load(os.path.join('img', 'white_king.png'))
w_queen = pygame.image.load(os.path.join('img', 'white_queen.png'))
w_bishop = pygame.image.load(os.path.join('img', 'white_bishop.png'))
w_rook = pygame.image.load(os.path.join('img', 'white_rook.png'))
w_knight = pygame.image.load(os.path.join('img', 'white_knight.png'))

b = [b_bishop, b_king, b_queen, b_knight, b_rook, b_pawn]
w = [w_bishop, w_king, w_queen, w_knight, w_rook, w_pawn]

B = []
W = []

for img in b:
    B.append(pygame.transform.scale(img, (90, 90)))

for img in w:
    W.append(pygame.transform.scale(img, (90, 90)))


class Figure:
    img = -1
    rez = [94, 94, 752, 752]
    startX = rez[0]
    startY = rez[1]

    def __init__(self, color, tip, line, row):
        self.row = row
        self.line = line
        self.selected = False
        self.color = color
        self.tip = tip
        self.move_l = []
        self.moved = False

    def isselected(self):
        return self.selected

    def change_position(self, pos):
        self.line = pos[0]
        self.row = pos[1]

    def update_possible_moves(self, board):
        self.move_l = self.possible_moves(board)

    def icon(self, window, turn):
        if self.color == 'white':
            icon = W[self.img]
        else:
            icon = B[self.img]

        x = round(self.row * self.rez[2] / 8)
        y = round(self.line * self.rez[3] / 8)
        window.blit(icon, (x, y))


class Pawn(Figure):
    img = 5

    def possible_moves(self, board):
        i = self.line
        j = self.row
        moves = []
        # BLACK
        if self.color == 'black':
            # ход вперёд
            if i < 7:
                mov = board[i + 1][j]
                if mov == 0:
                    moves.append((i + 1, j))

            # съедание вправо
            if j < 7 and i < 7:
                mov = board[i + 1][j + 1]
                if mov != 0:
                    if mov.color != self.color:
                        moves.append((i + 1, j + 1))

            # съедание влево
            if j > 0:
                mov = board[i + 1][j - 1]
                if (mov != 0):
                    if mov.color != self.color:
                        moves.append((i + 1, j - 1))

            # первый ход
            if i == 1:
                mov = board[i + 1][j]
                mov2 = board[i + 2][j]
                if (mov == 0) and (mov2 == 0):
                    moves.append((i + 2, j))

            # взятие на проходе справа
            if (i == 4) and (j < 7):
                mov = board[i + 1][j + 1]
                mov2 = board[i][j + 1]
                if mov == 0:
                    if mov2 != 0:
                        if (mov2.color != self.color) and (mov2.tip == self.tip):
                            moves.append((i + 1, j + 1))
                            board[i][j + 1] = 0

            # взятие на проходе слева
            if (i == 4) and (j > 0):
                mov = board[i + 1][j - 1]
                mov2 = board[i][j - 1]
                if mov == 0:
                    if mov2 != 0:
                        if (mov2.color != self.color) and (mov2.tip == self.tip):
                            moves.append((i + 1, j - 1))
                            board[i][j - 1] = 0
            # WHITE
        else:
            # ход вперёд
            if i > 0:
                mov = board[i - 1][j]
                if mov == 0:
                    moves.append((i - 1, j))

            # съедание вправо
            if j < 7:
                mov = board[i - 1][j + 1]
                if (mov != 0) and (mov.color != self.color):
                    moves.append((i - 1, j - 1))

            # съедание влево
            if j > 0:
                mov = board[i - 1][j - 1]
                if (mov != 0) and (mov.color != self.color):
                    moves.append((i - 1, j - 1))

            # первый ход
            if i == 6:
                mov = board[i - 2][j]
                mov2 = board[i - 1][j]
                if (mov == 0) and (mov2 == 0):
                    moves.append((i - 2, j))

            # взятие на проходе справа
            if (i == 3) and (j < 7):
                mov = board[i - 1][j + 1]
                mov2 = board[i][j + 1]
                if mov == 0:
                    if mov2 != 0:
                        if (mov2.color != self.color) and (mov2.tip == self.tip):
                            moves.append((i - 1, j + 1))

            # взятие на проходе слева
            if (i == 3) and (j > 0):
                mov = board[i - 1][j - 1]
                mov2 = board[i][j - 1]
                if mov == 0:
                    if mov2 != 0:
                        if (mov2.color != self.color) and (mov2.tip == self.tip):
                            moves.append((i + 1, j - 1))

        return moves


class King(Figure):
    img = 1

    def possible_moves(self, board):
        i = self.line
        j = self.row
        moves = []
        if i > 0:
            # назад
            mov = board[i - 1][j]
            if mov == 0:
                moves.append((i - 1, j))
            elif mov.color != self.color:
                moves.append((i - 1, j))

            # назад влево
            if j > 0:
                mov = board[i - 1][j - 1]
                if mov == 0:
                    moves.append((i - 1, j - 1))
                elif mov.color != self.color:
                    moves.append((i - 1, j - 1))

            # назад вправо
            if j < 7:
                mov = board[i - 1][j + 1]
                if mov == 0:
                    moves.append((i - 1, j + 1))
                elif mov.color != self.color:
                    moves.append((i - 1, j + 1))

        if i < 7:
            # вперёд
            mov = board[i + 1][j]
            if mov == 0:
                moves.append((i + 1, j))
            elif mov.color != self.color:
                moves.append((i + 1, j))

            # вперёд влево
            if j > 0:
                mov = board[i + 1][j - 1]
                if mov == 0:
                    moves.append((i + 1, j - 1))
                elif mov.color != self.color:
                    moves.append((i + 1, j - 1))

            # вперёд вправо
            if j < 7:
                mov = board[i + 1][j + 1]
                if mov == 0:
                    moves.append((i + 1, j + 1))
                elif mov.color != self.color:
                    moves.append((i + 1, j + 1))

        # влево
        if j > 0:
            mov = board[i][j - 1]
            if mov == 0:
                moves.append((i, j - 1))
            elif mov.color != self.color:
                moves.append((i, j - 1))

        # враво
        if j < 7:
            mov = board[i][j + 1]
            if mov == 0:
                moves.append((i, j + 1))
            elif mov.color != self.color:
                moves.append((i, j + 1))

        return moves


class Knight(Figure):
    img = 3

    def possible_moves(self, board):
        i = self.line
        j = self.row
        moves = []
        # вниз влево
        if (i < 6) and (j > 0):
            mov = board[i + 2][j - 1]
            if mov == 0:
                moves.append((i + 2, j - 1))
            elif mov.color != self.color:
                moves.append((i + 2, j - 1))

        # вниз вправо
        if (i < 6) and (j < 7):
            mov = board[i + 2][j + 1]
            if mov == 0:
                moves.append((i + 2, j + 1))
            elif mov.color != self.color:
                moves.append((i + 2, j + 1))

        # вверх влево
        if (i > 1) and (j > 0):
            mov = board[i - 2][j - 1]
            if mov == 0:
                moves.append((i - 2, j - 1))
            elif mov.color != self.color:
                moves.append((i - 2, j - 1))

        # вверх вправо
        if (i > 1) and (j < 7):
            mov = board[i - 2][j + 1]
            if mov == 0:
                moves.append((i - 2, j + 1))
            elif mov.color != self.color:
                moves.append((i - 2, j + 1))

        return moves


class Bishop(Figure):
    img = 0

    def possible_moves(self, board):
        i = self.line
        j = self.row
        moves = []
        tjL = j + 1
        tjR = j - 1
        for ti in range(i - 1, -1, -1):
            if tjL < 8:
                mov = board[ti][tjL]
                if mov == 0:
                    moves.append((ti, tjL))
                elif mov.color != self.color:
                    moves.append((ti, tjL))
                    break

                else:
                    break
            else:
                break
            tjL += 1

        # вверх влево
        for ti in range(i - 1, -1, -1):
            if tjR > -1:
                mov = board[ti][tjR]
                if mov == 0:
                    moves.append((ti, tjR))
                elif mov.color != self.color:
                    moves.append((ti, tjR))
                    break

                else:
                    break
            else:
                break

            tjR -= 1

        # вниз вправо
        tjL = j + 1
        tjR = j - 1
        for ti in range(i + 1, 8):
            if tjL < 8:
                mov = board[ti][tjL]
                if mov == 0:
                    moves.append((ti, tjL))
                elif mov.color != self.color:
                    moves.append((ti, tjL))
                    break

                else:
                    break
            else:
                break
            tjL += 1
        # вверх влево
        for ti in range(i + 1, 8):
            if tjR < 8:
                mov = board[ti][tjR]
                if mov == 0:
                    moves.append((ti, tjR))
                elif mov.color != self.color:
                    moves.append((ti, tjR))
                    break

                else:
                    break
            else:
                break
            tjR -= 1

        return moves


class Rook(Figure):
    img = 4

    def possible_moves(self, board):
        i = self.line
        j = self.row
        moves = []

        # вверх
        for ix in range(i - 1, -1, -1):
            mov = board[ix][j]
            if mov == 0:
                moves.append((ix, j))
            elif mov.color != self.color:
                moves.append((ix, j))
                break

            else:
                break

        # вниз:
        for ix in range(i + 1, 8, 1):
            mov = board[ix][j]
            if mov == 0:
                moves.append((ix, j))
            elif mov.color != self.color:
                moves.append((ix, j))
                break

            else:
                break
        # влево
        for jx in range(j - 1, -1, -1):
            mov = board[i][jx]
            if mov == 0:
                moves.append((i, jx))
            elif mov.color != self.color:
                moves.append((i, jx))
                break

            else:
                break
        # враво
        for jx in range(j + 1, 8, 1):
            mov = board[i][jx]
            if mov == 0:
                moves.append((i, jx))
            elif mov.color != self.color:
                moves.append((i, jx))
                break

            else:
                break
        return moves


class Queen(Figure):
    img = 2

    def possible_moves(self, board):
        i = self.line
        j = self.row
        moves = []

        # вверх
        for ix in range(i - 1, -1, -1):
            mov = board[ix][j]
            if mov == 0:
                moves.append((ix, j))
            elif mov.color != self.color:
                moves.append((ix, j))
                break

            else:
                break

        # вниз:
        for ix in range(i + 1, 8, 1):
            mov = board[ix][j]
            if mov == 0:
                moves.append((ix, j))
            elif mov.color != self.color:
                moves.append((ix, j))
                break

            else:
                break
        # влево
        for jx in range(j - 1, -1, -1):
            mov = board[i][jx]
            if mov == 0:
                moves.append((i, jx))
            elif mov.color != self.color:
                moves.append((i, jx))
                break

            else:
                break
        # враво
        for jx in range(j + 1, 8, 1):
            mov = board[i][jx]
            if mov == 0:
                moves.append((i, jx))
            elif mov.color != self.color:
                moves.append((i, jx))
                break

            else:
                break
        tjL = j + 1
        tjR = j - 1
        for ti in range(i - 1, -1, -1):
            if tjL < 8:
                mov = board[ti][tjL]
                if mov == 0:
                    moves.append((ti, tjL))
                elif mov.color != self.color:
                    moves.append((ti, tjL))
                    break

                else:
                    break
            else:
                break
            tjL += 1

        # вверх влево
        for ti in range(i - 1, -1, -1):
            if tjR > -1:
                mov = board[ti][tjR]
                if mov == 0:
                    moves.append((ti, tjR))
                elif mov.color != self.color:
                    moves.append((ti, tjR))
                    break

                else:
                    break
            else:
                break

            tjR -= 1

        # вниз вправо
        tjL = j + 1
        tjR = j - 1
        for ti in range(i + 1, 8):
            if tjL < 8:
                mov = board[ti][tjL]
                if mov == 0:
                    moves.append((ti, tjL))
                elif mov.color != self.color:
                    moves.append((ti, tjL))
                    break

                else:
                    tjL = 9
            tjL += 1
        # вверх влево
        for ti in range(i + 1, 8):
            if tjR > -1:
                mov = board[ti][tjR]
                if mov == 0:
                    moves.append((ti, tjR))
                elif mov.color != self.color:
                    moves.append((ti, tjR))
                    break

                else:
                    tjR = -1
            tjR -= 1

        return moves

        return moves
