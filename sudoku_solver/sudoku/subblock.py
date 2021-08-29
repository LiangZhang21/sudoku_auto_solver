import pygame

class SubBlock:
    def __init__(self, block, sub_block, color, selected):
        self.block = block
        self.sub_block = sub_block
        self.color = color
        self.selected = selected
    
    def select(self):
        self.selected = True

    def de_select(self):
        self.selected = False