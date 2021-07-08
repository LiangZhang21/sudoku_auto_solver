import pygame
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
        self.board = Board()
        self.valid_num = {}

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            block = self.board.get_block(row, col)

        else:
             block = self.board.get_block(row, col)
             self.selected = block
             return True
        return False