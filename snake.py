import random
import pygame
#initialize pygame 
pygame.init()

#Game settings
Width  = 600
Height = 600
Block = 20 
screen = pygame.display.set_mode((Width,Height))
clock=pygame.time.Clock()
score = 0 
pygame.display.set_caption('Snake game')

#Snake start  in the middle
snake = [( 300,300), (280,300),(260,300)]
direction = (Block,0)

#Place apple at random position
apple = ( random.randrange(0, Width, Block),
         random.randrange(0,Height, Block))

running = True

#Handle user input 
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        if event.type ==  pygame.KEYDOWN:
            if event.key ==pygame.K_RIGHT:
                direction =(Block,0)
            elif event.key ==pygame.K_LEFT:
                direction =(-Block,0)
            elif event.key ==pygame.K_UP:
                direction =(0,-Block)
            elif event.key ==pygame.K_DOWN:
                direction =(0,Block)
    
    #Calculate new  head position 
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    
    #Check wall collition 
    if new_head [0] < 0 or new_head[0] >= Width or new_head[1] < 0  or new_head[1] >=  Height:
        running = False
    
    #Check selfcolision
    if new_head in snake[1:]:
        running = False
    
    #Move snak forward
    snake.insert(0,new_head)
    
    #Draw background
    screen.fill((0,128,0))
    pygame.draw.rect(screen,(100, 100, 100),(0, 0, Width, Height),10)

    font = pygame.font.SysFont('Arial',30)
    score_text = font.render (f'Score:{score}', True, (255,255,255))
    screen.blit(score_text,(10,10))
    
    if snake[0] ==apple:
        apple=(random.randrange(0,Width, Block), random.randrange(0,Height, Block))
        score +=1
    else:
        snake.pop()
    
    #Draw snake border    
    pygame.draw.rect(screen,(255, 0, 0), (apple[0],apple[1], Block, Block))
  
    #Draw snake
    for block in snake:
        pygame.draw.rect(screen, (255, 255, 255), (block[0], block[1], Block, Block))
  
    #Reflesh screen at 10 frames per second
    pygame.display.update()
    clock.tick(10)

#Game over screen
screen.fill((0,0,0))
font = pygame.font.SysFont('Arial', 50 )
game_over_text = font.render('GAME OVER!', True, (250,0,0))
score_text = font.render(f'Final Score:{score}', True, (255,255,255))
screen.blit(game_over_text, (Width//2-150, Height//2 - 50))
screen.blit(score_text,(Width//2-120,  Height//2+ 20))
pygame.display.update()

#Waiting for player to press any key to close window
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False
        if event.type ==pygame.KEYDOWN:#
            waiting = False
pygame.quit()