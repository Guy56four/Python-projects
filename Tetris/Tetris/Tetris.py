import pygame
from settings  import *
from tetromino import Tetromino

#Initialize pygame
pygame.init()

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()

#Tetris board
#Draw grey grid lines om screen
def draw_grid():
    for x in range(0,Width, Block):
        pygame.draw.line(screen,GREY,(x,0),(x, Height))
    for y in range(0, Height, Block):
        pygame.draw.line(screen, GREY,(0, y), (Width, y))

def lock_piece(piece, board):
    #Lock piece into the board when it lands
    for row in range (len(piece.shape)):
        for col in range(len(piece.shape[row])):
            if piece.shape[row][col] == 1:
                board[piece.y +row][piece.x + col] = piece.color

def draw_board(board):
    #Draw all locked pieces on screen
    for row in range(Rows):
        for col in range (Columns):
            if board[row][col] !=0:
                pygame.draw.rect(screen, board[row][col],(
                    col * Block, row * Block, Block - 1, Block -1 
                ))
def clear_lines(board):
    #Remove full rows and add empty ones at top
    lines_cleared = 0
    new_board = []
    for row in board: 
        if 0  in row: 
            new_board.append(row) #keep incomlpete rows
        else:
            lines_cleared +=1 #skip full rows
            #Add empty rows at top to replce cleared ones
    for _ in range(lines_cleared):
        new_board.insert(0, [0] * Columns) 
    return new_board, lines_cleared

#Geme setup
piece = Tetromino()             #first piece
fall_time = 0                   # tracks time since last fall
fall_speed = 500                #milliseconds between each fall step
score = 0                       #player score
board = [[0] * Columns for _ in range (Rows)]   #empty board
        
#Game Loop
running = True
while running:
    #Handle user  input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if piece.valid_move(board, dx = -1):
                    piece.x -= 1
            elif event.key  == pygame.K_RIGHT:
                if piece.valid_move(board, dx= 1):
                    piece.x += 1
            elif event.key == pygame.K_DOWN:
                if piece.valid_move(board, dy = 1):
                    piece.y += 1
                
            elif event.key ==pygame.K_UP:
                    piece.rotate()

    
    #Move piece down automaticlly 
    fall_time += clock.tick(60)
    
    #Check if the piece hit the bottom
    
    if fall_time >= fall_speed:
        if piece.valid_move(board, dy = 1):
            piece.y +=1
        else:
            lock_piece(piece, board)
            board, cleared = clear_lines(board)
            score += cleared *100
            fall_speed =max(100,500 - score //2 )
            piece  = Tetromino()

            if board[0][Columns //2] != 0:
              running = False
        fall_time = 0 
    #Draw everything
    screen.fill(BLACK)
    draw_board(board)       
    draw_grid()
    piece.draw(screen)
    font = pygame.font.SysFont('Arial', 25 )
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text,(10, 10))
    pygame.display.update()  
    
#Game over screen
screen.fill(BLACK) 
font = pygame.font.SysFont('Arial', 50)
game_over_text = font.render('Game Over!', True, (255, 0, 0))
score_text = font.render(f'Score:{score}', True, (255, 255, 255))
screen.blit(game_over_text, (Width//2 -150, Height //2  - 50))
screen.blit(score_text, (Width//2 -80, Height//2+20))
pygame.display.update()

#Wait until player to press any key
waiting = True
while waiting : 
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            waiting = False
        if event.type == pygame.KEYDOWN:
            waiting = False  
pygame.quit()




