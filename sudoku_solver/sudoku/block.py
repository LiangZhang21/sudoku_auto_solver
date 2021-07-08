from .constants import *
import pygame

class Block:
    def __init__(self, row, col, num):
        self.row = row
        self.col = col
        self.num = num

        self.x = 0
        self.y = 0
        self. calc_pos()
    
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col
        self.y = SQUARE_SIZE * self.row

    def draw(self, win):
        #pygame.draw.rect(win, RED, (self.x, self.y, SQUARE_SIZE-10, SQUARE_SIZE-10,))
        pass

    def __repr__(self):
        return str(self.row) + " " + str(self.col)