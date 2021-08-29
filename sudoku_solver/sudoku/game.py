import pygame
from .constants import *
from sudoku.board import Board


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.pre_selected = None
        self.board = Board()
        self.valid_num = {}

    def reset(self):
        self._init()

    def select(self, row, col, win):
        if self.selected:
            clicked_block = self.board.get_block(row, col)

            # if user select a different block
            if not (self.selected == clicked_block):
                setattr(self.board.get_block(self.pre_selected.row,
                                             self.pre_selected.col), 'color', WHITE)
                self.selected = None
                self.pre_selected.select = False
                self.select(row, col, win)

        else:
            clicked_block = self.board.get_block(row, col)
            self.selected = clicked_block
            self.pre_selected = self.selected
            setattr(self.board.get_block(row, col), 'color', GREY)
            self.board.get_block(row, col).select = True
            #print(str(self.selected.row) + " " + str(self.selected.col))
            return True
        return False
