import pygame
import random
from settings import *



#Picking  a random shape and matching colors
class Tetromino:
    def __init__(self):
        index = random.randint(0, 6)
        self.shape = SHAPES[index]
        self.color = COLORS[index]
        #Starts at the top center of the board
        self.x = Columns //2 - 1
        self.y = 0

    
    def draw(self, screen):
        #Draw each block of the piece
        for row in range(len(self.shape)):
            for col in range(len(self.shape[row])):
                if self.shape[row][col]==1:
                    pygame.draw.rect(screen,self.color,(
                        (self.x + col) * Block,
                        (self.y + row) * Block,
                        Block - 1, Block -1
                    ))
    #Transpose and reverse to rotate 90 degress
    def rotate (self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]
        #Create first piece

    #Cheking if moving  by dx, dy is valid (no walls, no collisions)
    def valid_move(self, board, dx=0, dy=0):
        for row in range(len(self.shape)):
            for col in range(len(self.shape[row])):
                
                if self.shape[row][col] ==1:
                    new_x = self.x + col + dx
                    new_y = self.y + row + dy
                    #Cheking left and right walls
                    if new_x < 0 or new_x >= Columns:
                        return False
                        #cheking floor
                    if new_y >= Rows:
                        return False
                    if new_y >= 0 and board [new_y][new_x] !=0:
                      return False

        return True
