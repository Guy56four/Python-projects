#Settings are coming
Width = 300
Height = 600
Block = 30
Columns = Width //Block
Rows = Height // Block

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255) 
GREY  = (128,128,128)


#Tetris pieces
SHAPES = [
    [[1,1,1,1]],
    [[1,1],[1,1]],
    [[1,1,1],[0,1,0]],
    [[1,1,1],[1,0,0]],
    [[1,1,1],[0,0,1]],
    [[1,1,0],[0,1,1]],
    [[0,1,1],[1,1,0]],
]
#Each color per shape
COLORS=[
    (0, 255, 255),
    (255, 255, 0),
    (128, 0, 128),
    (255, 165, 0),
    (0, 0, 255),
    (0, 255, 0),
    (255, 0, 0),
]