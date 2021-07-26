from figure import Pawn
from figure import King
from figure import Bishop
from figure import Knight
from figure import Rook
from figure import Queen
import time
import pygame


class Board:
    def __init__(self, rows, lines, mode):
        self.rows = rows
        self.lines = lines
        self.board = [[0 for i in range(8)] for _ in range(rows)]

        self.board[0][0] = Rook("black", "rook", 0, 0)
        self.board[0][1] = Knight("black", "knight", 0, 1)
        self.board[0][2] = Bishop("black", "bishop", 0, 2)
        self.board[0][3] = Queen("black", "queen", 0, 3)
        self.board[0][4] = King("black", "king", 0, 4)
        self.board[0][5] = Bishop("black", "bishop", 0, 5)
        self.board[0][6] = Knight("black", "knight", 0, 6)
        self.board[0][7] = Rook("black", "rook", 0, 7)

        self.board[1][0] = Pawn("black", "pawn", 1, 0)
        self.board[1][1] = Pawn("black", "pawn", 1, 1)
        self.board[1][2] = Pawn("black", "pawn", 1, 2)
        self.board[1][3] = Pawn("black", "pawn", 1, 3)
        self.board[1][4] = Pawn("black", "pawn", 1, 4)
        self.board[1][5] = Pawn("black", "pawn", 1, 5)
        self.board[1][6] = Pawn("black", "pawn", 1, 6)
        self.board[1][7] = Pawn("black", "pawn", 1, 7)

        self.board[7][0] = Rook("white", "rook", 7, 0)
        self.board[7][1] = Knight("white", "knight", 7, 1)
        self.board[7][2] = Bishop("white", "bishop", 7, 2)
        self.board[7][3] = Queen("white", "queen", 7, 3)
        self.board[7][4] = King("white", "king", 7, 4)
        self.board[7][5] = Bishop("white", "bishop", 7, 5)
        self.board[7][6] = Knight("white", "knight", 7, 6)
        self.board[7][7] = Rook("white", "rook", 7, 7)

        self.board[6][0] = Pawn("white", "pawn", 6, 0)
        self.board[6][1] = Pawn("white", "pawn", 6, 1)
        self.board[6][2] = Pawn("white", "pawn", 6, 2)
        self.board[6][3] = Pawn("white", "pawn", 6, 3)
        self.board[6][4] = Pawn("white", "pawn", 6, 4)
        self.board[6][5] = Pawn("white", "pawn", 6, 5)
        self.board[6][6] = Pawn("white", "pawn", 6, 6)
        self.board[6][7] = Pawn("white", "pawn", 6, 7)

        self.mode = mode

    def update_moves(self):
        for i in range(self.lines):
            for j in range(self.rows):
                if self.board[i][j] != 0:
                    self.board[i][j].update_possible_moves(self.board)

    def danger_moves(self, color):
        danger_moves = []
        for i in range(self.lines):
            for j in range(self.rows):
                if self.board[i][j].color != color:
                    for danger in self.board.move_l:
                        danger_moves.append(danger)

        return danger_moves

    def check(self, color):
        self.update_moves()
        d_moves = self.danger_moves(color)
        king = (-1, -1)
        for i in range(self.lines):
            for j in range(self.rows):
                if self.board[i][j] != 0:
                    if (self.board[i][j].type == 'king') and (self.board[i][j] == color):
                        king = (i, j)
        if king in d_moves:
            return True
        else:
            return False

    def select(self, line, row, color):
        change = False
        pos = (-1, -1)
        for i in range(self.lines):
            for j in range(self.rows):
                if self.board[i][j] != 0:
                    if self.board[i][j].selected:
                        pos = (i, j)

        if self.board[line][row] == 0 and pos != (-1, -1):
            move = self.board[pos[0]][pos[1]].move_l
            if (line, row) in move:
                change = self.move(pos, (line, row), color)
        else:
            if pos == (-1, -1):
                self.reset_select()

    def reset_select(self):
        for i in range(self.lines):
            for j in range(self.rows):
                if self.board[i][j] != 0:
                    self.board.seleted == False

    def move(self, start, end, color):
        cheked = self.check(color)
        change = True
        newBoard = self.board
        newBoard[start[0]][start[1]].change_position((end[0], end[1]))
        newBoard[end[0]][end[1]] = newBoard[start[0]][start[1]]
        newBoard[start[0]][start[1]] = 0
        self.board = newBoard
        if self.check(color) or (cheked and self.check(color)):
            change = False
            newBoard = self.board
            newBoard[end[0]][end[1]].change_position((start[0], start[1]))
            newBoard[start[0]][start[1]] = newBoard[end[0]][end[1]]
            newBoard[end[0]][end[1]] = 0
            self.board = newBoard
        else:
            self.reset_select()
        self.update_moves()
        return change
