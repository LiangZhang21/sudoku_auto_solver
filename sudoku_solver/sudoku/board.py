import pygame
from .constants import *
from .block import Block


class Board:
    def __init__(self):
        self.board = []
        self.subblocks = []
        self.selected_block = None
        self.create_board()
        self.myfont = pygame.font.SysFont("comicsansms", 15)

    def draw_squares(self, win):
        for row in range(ROWS):
            for col in range(ROWS):
                pygame.draw.rect(win, WHITE, (row*SQUARE_SIZE,
                                              col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        # grid
        for row in range(ROWS+1):
            pygame.draw.line(win, BLACK, (0, row*SQUARE_SIZE),
                             (9*SQUARE_SIZE, row*SQUARE_SIZE))
            # box
            if (row % 3 == 0):
                pygame.draw.line(win, BLACK, (0, row*SQUARE_SIZE),
                                 (9*SQUARE_SIZE, row*SQUARE_SIZE), 4)

        for col in range(COLS+1):
            pygame.draw.line(win, BLACK, (col*SQUARE_SIZE, 0),
                             (col*SQUARE_SIZE, 9*SQUARE_SIZE))
            # box
            if (col % 3 == 0):
                pygame.draw.line(win, BLACK, (col*SQUARE_SIZE, 0),
                                 (col*SQUARE_SIZE, 9*SQUARE_SIZE), 4)

    def num_input(self, block, num):
        self.board[block.row][block.col].num = num

    def get_block(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(Block(row, col, WHITE, 0, False))

    def draw_block(self, row, col, color, win):
        pygame.draw.rect(
            win, color, (self.board[row][col].x + 5, self.board[row][col].y + 5, SQUARE_SIZE - 10, SQUARE_SIZE - 10))

    def draw_num(self, row, col, num, win):
        value = self.myfont.render(str(num), True, (0, 0, 0))
        win.blit(value, (col * SQUARE_SIZE + 40, row * SQUARE_SIZE + 40))

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                if getattr(self.board[row][col], 'color') == WHITE:
                    self.draw_block(row, col, WHITE, win)
                else:
                    self.draw_block(row, col, GREY, win)
                if self.board[row][col].num != 0:
                    self.draw_num(row, col, self.board[row][col].num, win)

    def __getitem__(self, win):
        return f"Value {win}"
