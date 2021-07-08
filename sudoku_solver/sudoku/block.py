from .constants import *
import pygame

class Block:
    def __init__(self, row, col, color, num):
        self.row = row
        self.col = col
        self.color = color
        self.num = num

        self.x = 0
        self.y = 0
        self. calc_pos()
    
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col
        self.y = SQUARE_SIZE * self.row


    def __repr__(self):
        return str(self.row) + " " + str(self.col)