import pygame
from sudoku.game import Game

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 9, 9
SQUARE_SIZE = WIDTH//COLS

WHITE = (255, 255, 255)
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku Solver')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    pygame.init()
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    selected_box = None

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col, game.win)
                selected_box = game.board.get_block(row, col)
            if event.type == pygame.KEYDOWN:
                row = selected_box.row
                col = selected_box.col
                if (selected_box.select):
                    if (event.key == 48): #checking if the key is 0
                        game.board.get_block(row, col).num = event.key - 48       
                    if (0 < event.key - 48 < 10): #checking for valid input
                        game.board.get_block(row, col).num = event.key - 48
                        #print(str(game.board.get_block(row, col).num))   
                        
        game.update()

    pygame.quit()


main()