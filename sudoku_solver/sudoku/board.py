import pygame
from .constants import *
from .block import Block

class Board:
    def __init__(self):
        self.board = []
        self.selected_block = None
        self.create_board()

    def draw_squares(self, win):
        for row in range(ROWS):
            for col in range(ROWS):
                pygame.draw.rect(win, WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        
        #grid
        for row in range(ROWS+1):
            pygame.draw.line(win, BLACK, (0, row*SQUARE_SIZE), (9*SQUARE_SIZE, row*SQUARE_SIZE))

        for col in range(COLS+1):
            pygame.draw.line(win, BLACK, (col*SQUARE_SIZE, 0), (col*SQUARE_SIZE, 9*SQUARE_SIZE))

        #box
        for row in range(ROWS+1):
            if (row % 3 == 0):
                pygame.draw.line(win, BLACK, (0, row*SQUARE_SIZE), (9*SQUARE_SIZE, row*SQUARE_SIZE), 4)
        
        for col in range(COLS+1):
            if (col % 3 == 0):
                pygame.draw.line(win, BLACK, (col*SQUARE_SIZE, 0), (col*SQUARE_SIZE, 9*SQUARE_SIZE), 4)

    def num_input(self, block, num):
        self.board[block.row][block.col].num = num
        

    def get_block(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS): 
                self.board[row].append(Block(row, col, 0))
    
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                block = self.board[row][col]
                block.draw(win)