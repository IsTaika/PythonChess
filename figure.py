import pygame

b_pawn = pygame.image.load('/img', 'black_pawn.png')
b_king = pygame.image.load('/img', ' black_king.png')
b_queen = pygame.image.load('/img', 'black_queen.png')
b_bishop = pygame.image.load('/img', 'black_bishop.png')
b_rook = pygame.image.load('/img', 'black_rook.png')
b_knight = pygame.image.load('/img', 'black_knight.png')

w_pawn = pygame.image.load('/img', 'white_pawn.png')
w_king = pygame.image.load('/img', ' white_king.png')
w_queen = pygame.image.load('/img', 'white_queen.png')
w_bishop = pygame.image.load('/img', 'white_bishop.png')
w_rook = pygame.image.load('/img', 'white_rook.png')
w_knight = pygame.image.load('/img', 'white_knight.png')

b = [b_bishop, b_king, b_queen, b_knight, b_rook, b_pawn]
w = [w_bishop, w_king, w_queen, w_knight, w_rook, w_pawn]

B = []
W = []

for img in b:
    B.append(pygame.transform.scale(img, (50, 50)))

for img in w:
    W.append(pygame.transform.scale(img, (50, 50)))


class Figure:
    img = -1

    def __init__(self, color, type, line, row):
        self.row = row
        self.line = line
        self.selected = False
        self.color = color
        self.type = type
        self.move_l = []

    def isselected(self):
        return self.selected

    def change_position(self, pos):
        self.line = pos[0]
        self.row = pos[1]


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
            if j < 7:
                mov = board[i + 1][j + 1]
                if (mov != 0) and (mov.color != self.color):
                    moves.append((i + 1, j - 1))

            # съедание влево
            if j > 0:
                mov = board[i + 1][j - 1]
                if (mov != 0) and (mov.color != self.color):
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
                    if (mov2.color != self.color) and (mov2.type == self.type):
                        moves.append((i + 1, j + 1))

            # взятие на проходе слева
            if (i == 4) and (j > 0):
                mov = board[i + 1][j - 1]
                mov2 = board[i][j - 1]
                if mov == 0:
                    if (mov2.color != self.color) and (mov2.type == self.type):
                        moves.append((i + 1, j - 1))
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
                        if (mov2.color != self.color) and (mov2.type == self.type):
                            moves.append((i - 1, j + 1))

                # взятие на проходе слева
                if (i == 3) and (j > 0):
                    mov = board[i - 1][j - 1]
                    mov2 = board[i][j - 1]
                    if mov == 0:
                        if (mov2.color != self.color) and (mov2.type == self.type):
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
            # назад влево
            if j > 0:
                mov = board[i - 1][j - 1]
                if mov == 0:
                    moves.append((i - 1, j - 1))
            # назад вправо
            if j < 7:
                mov = board[i - 1]
                if mov == 0:
                    moves.append((i - 1, j + 1))
        if i < 7:
            # вперёд
            mov = board[i + 1][j]
            if mov == 0:
                moves.append((i + 1, j))
            # вперёд влево
            if j > 0:
                mov = board[i + 1][j - 1]
                if mov == 0:
                    moves.append((i + 1, j - 1))
            # вперёд вправо
            if j < 7:
                mov = board[i + 1][j + 1]
                if mov == 0:
                    moves.append((i + 1, j + 1))
        # влево
        if j > 0:
            mov = board[i][j - 1]
            if mov == 0:
                moves.append((i, j - 1))
        # враво
        if j < 7:
            mov = board[i][j + 1]
            if mov == 0:
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
        # вниз вправо
        if (i < 6) and (j < 7):
            mov = board[i + 2][j + 1]
            if mov == 0:
                moves.append((i + 2, j + 1))
        # вверх влево
        if (i > 1) and (j > 0):
            mov = board[i - 2][j - 1]
            if mov == 0:
                moves.append((i - 2, j - 1))
        # вверх вправо
        if (i > 1) and (j < 7):
            mov = board[i - 2][j + 1]
            if mov == 0:
                moves.append((i - 2, j + 1))

        return moves


class Bishop(Figure):
    img = 0

    def possible_moves(self, board):
        i = self.line
        j = self.row
        moves = []
        # вверх вправо
        tjr = j + 1
        tjl = j - 1
        for ti in range(i - 1, -1, -1):
            if tjr < 8:
                mov = board[ti, tjr]
                if mov == 0:
                    moves.append((ti, tjr))
                else:
                    break
            else:
                break
            tjr += 1

        # вверх влево
        for ti in range(i - 1, -1, -1):
            if tjl > -1:
                mov = board[ti][tjl]
                if mov == 0:
                    moves.append((ti, tjl))
                else:
                    break
            else:
                break

            tjl += 1

        # вниз вправо
        tjr = j + 1
        tjl = j - 1
        for ti in range(i + 1, 8):
            if tjr < 8:
                mov = board[ti, tjr]
                if mov == 0:
                    moves.append((ti, tjr))
                else:
                    break
            else:
                break
            tjr += 1
        # вверх влево
        for ti in range(i + 1, 8):
            if tjl < 8:
                mov = board[ti, tjl]
                if mov == 0:
                    moves.append((ti, tjl))
                else:
                    break
            else:
                break
            tjl += 1

        return moves

class Rook(Figure):
    img = 4

    def possible_moves(self, board):
        i = self.line
        j = self.row
        moves = []

        # вверх
        for ix in range(i -1, -1, -1):
            mov = board[ix][j]
            if mov == 0:
                moves.append((ix, j))
            else:
                break

        # вниз:
        for ix in range(i + 1, 8, 1):
            mov = board[ix][j]
            if mov == 0:
                moves.append((ix, j))
            else:
                break
        # влево
        for jx in range(j-1, -1, -1):
            mov = board[i][jx]
            if mov == 0:
                moves.append((i, jx))
            else:
                break
        #враво
        for jx in range(j+1, 8, 1):
            mov = board[i][jx]
            if mov == 0:
                moves.append((i, jx))
            else:
                break
        return moves


