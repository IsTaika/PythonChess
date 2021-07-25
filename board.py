from figure import Pawn
from figure import King
from figure import Bishop
from figure import Knight
from figure import Rook
from figure import Queen
import time
import pygame


class Board:
    def __init__(self, rows, lines):
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
