import pickle

from figure import Pawn
from figure import King
from figure import Bishop
from figure import Knight
from figure import Rook
from figure import Queen
import pygame


class Board:
    rez = [94, 94, 752, 752]
    startX = rez[0]
    startY = rez[1]

    def __init__(self, lines, rows):
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

        self.turn = 'white'
        self.winner = None
        self.last = None

    def update_moves(self):
        for i in range(self.lines):
            for j in range(self.rows):
                if self.board[i][j] != 0:
                    self.board[i][j].update_possible_moves(self.board)

    def danger_moves(self, color):
        danger_moves = []
        for i in range(self.lines):
            for j in range(self.rows):
                if self.board[i][j] != 0:
                    if self.board[i][j].color != color:
                        movelist = self.board[i][j].move_l
                        for moves in movelist:
                            if self.board[moves[0]][moves[1]] != 0:
                                danger_moves.append(moves)

        return danger_moves

    def check(self, color):
        self.update_moves()
        d_moves = self.danger_moves(color)
        king = (-1, -1)
        for i in range(self.lines):
            for j in range(self.rows):
                if self.board[i][j] != 0:
                    if (self.board[i][j].tip == 'king') and (self.board[i][j].color == color):
                        king = (i, j)
        if king in d_moves:
            print("CHEKED", color)
            return True
        else:
            return False

    def checkmate(self, color):
        if self.check(color):
            pos = (-1, -1)
            for i in range(self.lines):
                for j in range(self.rows):
                    if self.board[i][j] != 0:
                        if self.board[i][j].tip == 'king' and self.board[i][j].color == color:
                            pos = (i, j)
                            movelist = self.board[i][j].move_l

            d_moves = self.danger_moves(color)
            dpos = (-1, -1)
            for i in range(self.lines):
                for j in range(self.rows):
                    if self.board[i][j] != 0:
                        if self.board[i][j].color != color:
                            movel = self.board[i][j].move_l
                            if movel:
                                for moves in movel:
                                    if moves in d_moves:
                                        if moves == pos:
                                            dpos = (i, j)
            dmoves = []
            for i in range(self.lines):
                for j in range(self.rows):
                    if self.board[i][j] != 0:
                        if self.board[i][j].color != color:
                            amove = self.board[i][j].move_l
                            dmoves.append(amove)
                            if self.board[i][j].tip == 'rook':
                                for moves in amove:
                                    if j == dpos[1]:
                                        if moves == (dpos[0] + 1, dpos[1]) or moves == (dpos[0] - 1, dpos[1]):
                                            dmoves.append(dpos)
                                    if i == dpos[0]:
                                        if moves == (dpos[0], dpos[1] + 1) or moves == (dpos[0], dpos[1] - 1):
                                            dmoves.append(dpos)
                            if self.board[i][j].tip == 'bishop':
                                for moves in amove:
                                    if i < dpos[0]:
                                        if moves == (dpos[0] - 1, dpos[1] + 1) or moves == (dpos[0] - 1, dpos[1] + 1):
                                            dmoves.append(dpos)
                                    if i > dpos[0]:
                                        if moves == (dpos[0] + 1, dpos[1] + 1) or moves == (dpos[0] + 1, dpos[1] + 1):
                                            dmoves.append(dpos)
                            if self.board[i][j].tip == 'queen':
                                for moves in amove:
                                    if i < dpos[0]:
                                        if moves == (dpos[0] - 1, dpos[1] + 1) or moves == (dpos[0] - 1, dpos[1] + 1):
                                            dmoves.append(dpos)
                                    if i > dpos[0]:
                                        if moves == (dpos[0] + 1, dpos[1] + 1) or moves == (dpos[0] + 1, dpos[1] + 1):
                                            dmoves.append(dpos)
                                    if j == dpos[1]:
                                        if moves == (dpos[0] + 1, dpos[1]) or moves == (dpos[0] - 1, dpos[1]):
                                            dmoves.append(dpos)
                                    if i == dpos[0]:
                                        if moves == (dpos[0], dpos[1] + 1) or moves == (dpos[0], dpos[1] - 1):
                                            dmoves.append(dpos)
                            if self.board[i][j].tip == 'pawn':
                                if color == 'white':
                                    if i == dpos[0] - 1 and ((j == dpos[1] + 1) or (j == dpos[1] - 1)):
                                        dmoves.append(dpos)
                                if color == 'black':
                                    if i == dpos[0] + 1 and ((j == dpos[1] + 1) or (j == dpos[1] - 1)):
                                        dmoves.append(dpos)
                            if self.board[i][j].tip == 'knight':
                                if (i, j) == (dpos[0] + 2, dpos[1] - 1):
                                    dmoves.append(dpos)
                                if (i, j) == (dpos[0] + 2, dpos[1] + 1):
                                    dmoves.append(dpos)
                                if (i, j) == (dpos[0] - 2, dpos[1] - 1):
                                    dmoves.append(dpos)
                                if (i, j) == (dpos[0] - 2, dpos[1] + 1):
                                    dmoves.append(dpos)
                                if (i, j) == (dpos[0] + 1, dpos[1] - 2):
                                    dmoves.append(dpos)
                                if (i, j) == (dpos[0] + 1, dpos[1] + 2):
                                    dmoves.append(dpos)
                                if (i, j) == (dpos[0] - 1, dpos[1] - 2):
                                    dmoves.append(dpos)
                                if (i, j) == (dpos[0] - 1, dpos[1] + 2):
                                    dmoves.append(dpos)

            for i in range(self.lines):
                for j in range(self.rows):
                    if self.board[i][j] != 0:
                        if self.board[i][j].color == color and (i, j) != pos:
                            movel = self.board[i][j].move_l
                            if dpos in movel:
                                return False

                            for move in movel:
                                if self.board[dpos[0]][dpos[1]].tip == 'rook':
                                    if pos[0] == dpos[0]:
                                        if move[0] == dpos[0]:
                                            return False
                                    if pos[1] == dpos[1]:
                                        if move[1] == dpos[1]:
                                            return False
                                if self.board[dpos[0]][dpos[1]].tip == 'bishop':
                                    if dpos[0] > pos[0]:
                                        if dpos[1] > pos[0]:
                                            if move[0] == pos[0] + 1:
                                                if move[1] == pos[1] + 1:
                                                    return False
                                        if dpos[1] < pos[0]:
                                            if move[0] == pos[0] + 1:
                                                if move[1] == pos[1] - 1:
                                                    return False
                                    else:
                                        if dpos[1] > pos[0]:
                                            if move[0] == pos[0] - 1:
                                                if move[1] == pos[1] + 1:
                                                    return False
                                        if dpos[1] < pos[0]:
                                            if move[0] == pos[0] - 1:
                                                if move[1] == pos[1] - 1:
                                                    return False
                                if self.board[dpos[0]][dpos[1]].tip == 'queen':
                                    if pos[0] == dpos[0]:
                                        if move[0] == dpos[0]:
                                            return False
                                    if pos[1] == dpos[1]:
                                        if move[1] == dpos[1]:
                                            return False
                                    if dpos[0] > pos[0]:
                                        if dpos[1] > pos[0]:
                                            if move[0] == pos[0] + 1:
                                                if move[1] == pos[1] + 1:
                                                    return False
                                        if dpos[1] < pos[0]:
                                            if move[0] == pos[0] + 1:
                                                if move[1] == pos[1] - 1:
                                                    return False
                                    else:
                                        if dpos[1] > pos[0]:
                                            if move[0] == pos[0] - 1:
                                                if move[1] == pos[1] + 1:
                                                    return False
                                        if dpos[1] < pos[0]:
                                            if move[0] == pos[0] - 1:
                                                if move[1] == pos[1] - 1:
                                                    return False

            if color == 'white':
                print("BLACK WIN")
            else:
                print("WHITE WIN")
            return True

    def select(self, line, row, color):
        change = False
        pos = (-1, -1)
        for i in range(self.lines):
            for j in range(self.rows):
                if self.board[i][j] != 0 and self.board[i][j].color == color:
                    if self.board[i][j].selected:
                        pos = (i, j)

        if (self.board[line][row] == 0 or self.board[line][row].color != color) and pos != (-1, -1):
            moves = self.board[pos[0]][pos[1]].move_l
            print(moves)
            if (line, row) in moves:
                change = self.move(pos, (line, row), color)
                if self.board[line][row] != 0:
                    self.board[line][row].selected = False
                # съедание на проходе справа для чёрных
                if pos[0] == 3 and color == 'black':
                    if (line, row) == (pos[0] + 1, pos[1] + 1) and self.board[line][row] != 0 and self.board[line][
                        row].tip == 'pawn':
                        self.board[pos[0]][pos[1] + 1] = 0
                    # съедание на проходе слева для чёрных
                    if (line, row) == (pos[0] + 1, pos[1] - 1) and self.board[line][row] != 0 and self.board[line][
                        row].tip == 'pawn':
                        self.board[pos[0]][pos[1] - 1] = 0
                # Для белых:
                if pos[0] == 4 and color == 'white':
                    if (line, row) == (pos[0] - 1, pos[1] + 1) and self.board[line][row] != 0 and self.board[line][
                        row].tip == 'pawn':
                        self.board[pos[0]][pos[1] + 1] = 0
                    if (line, row) == (pos[0] - 1, pos[1] - 1) and self.board[line][row] != 0 and self.board[line][
                        row].tip == 'pawn':
                        self.board[pos[0]][pos[1] - 1] = 0

                # превращение пешки в ферзя
                if color == 'black':
                    if pos != (-1, -1) and self.board[pos[0]][pos[1]] != 0:
                        if self.board[pos[0]][pos[1]].tip == 'pawn':
                            if pos[0] == 1:
                                if line == 0:
                                    self.board[line][row] = 0
                                    self.board[line][row] = Queen('black', 'queen', line, row)
                else:
                    if pos != (-1, -1) and self.board[pos[0]][pos[1]] != 0:
                        if self.board[pos[0]][pos[1]].tip == 'pawn':
                            if pos[0] == 1:
                                if line == 0:
                                    self.board[line][row] = 0
                                    self.board[line][row] = Queen('white', 'queen', line, row)

            if not moves:
                self.board[pos[0]][pos[1]].selected = False
                self.reset_select()
            print("moves = ", moves)
            if (line, row) not in moves:
                self.board[pos[0]][pos[1]].selected = False
                self.reset_select()



        else:
            if pos == (-1, -1):
                self.reset_select()
                if self.board[line][row] != 0:
                    self.board[line][row].selected = True
            else:
                if self.board[pos[0]][pos[1]].color != self.board[line][row].color:
                    moves = self.board[pos[0]][pos[1]].move_l
                    if (line, row) in moves:
                        change = self.move(pos, (line, row), color)

                    if self.board[line][row].color == color:
                        self.board[line][row].selected = True

                else:
                    # Рокировка
                    if self.board[line][row].color == color:
                        self.reset_select()
                        if self.board[pos[0]][pos[1]].moved == False and self.board[pos[0]][pos[1]].tip == 'king' and \
                                self.board[line][row].tip == 'rook' and pos != (-1, -1) and row != pos[1]:
                            castle = True
                            if pos[1] > row:
                                for j in range(row + 1, pos[1]):
                                    if self.board[line][j] != 0:
                                        castle = False
                                if castle:
                                    change = self.move(pos, (line, 2), color)
                                    change = self.move((line, row), (line, 3), color)
                                if not change:
                                    self.board[line][row].selected = True

                            else:
                                for j in range(row - 1, pos[1], -1):
                                    if self.board[line][j] != 0:
                                        castle = False
                                    if castle:
                                        change = self.move(pos, (line, 6), color)
                                        change = self.move((line, row), (line, 5), color)
                                    if not change:
                                        self.board[line][row].selected = True

        print("Pos = ", pos, " line = ", line, " row = ", row)
        print("Change= ", change)

        if change:
            if self.turn == 'white':
                self.checkmate("black")
                self.turn = 'black'
                self.reset_select()
            else:
                self.checkmate("white")
                self.turn = 'white'
                self.reset_select()

        print(self.turn)

    def reset_select(self):
        for i in range(self.lines):
            for j in range(self.rows):
                if self.board[i][j] != 0:
                    self.board[i][j].seleted = False

    def move(self, start, end, color):
        checked = self.check(color)
        if self.board[start[0]][start[1]].color != color:
            change = False
            self.board[start[0]][start[1]].selected = False
            self.reset_select()
            return change
        change = True
        newBoard = self.board
        newBoard[start[0]][start[1]].change_position((end[0], end[1]))
        newBoard[end[0]][end[1]] = newBoard[start[0]][start[1]]
        newBoard[start[0]][start[1]] = 0
        self.board = newBoard

        if self.check(color) or (checked and self.check(color)):
            change = False
            newBoard = self.board
            newBoard[end[0]][end[1]].change_position((start[0], start[1]))
            newBoard[start[0]][start[1]] = newBoard[end[0]][end[1]]
            newBoard[end[0]][end[1]] = 0
            self.board = newBoard
            self.reset_select()
        else:
            self.reset_select()
        self.update_moves()
        if change:
            if self.board[end[0]][end[1]] != 0:
                self.board[end[0]][end[1]].moved = True

        return change

    def icon(self, window):

        for i in range(self.lines):
            for j in range(self.rows):
                if self.board[i][j] != 0:
                    self.board[i][j].icon(window, self.turn)
