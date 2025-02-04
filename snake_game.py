import pygame
import random

pygame.init()
width,height = 400,400
grid_size = 20
grid_width = width // grid_size
grid_height = height // grid_size
snake_speed = 5

white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)

up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)

score = 0

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")

snake = [(grid_width//2,grid_height//2)]
snake_direction = right

food = (random.randint(0,grid_width-1),random.randint(0,grid_height-1))

running = True
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
start_text = font.render("Press any key to start", True, green)

screen.fill(black)
screen.blit(start_text, (width//2 - start_text.get_width()//2, height//2 - start_text.get_height()//2))
pygame.display.flip()

start = False
while not start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            start = True 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != down:
                snake_direction = up
            elif event.key == pygame.K_DOWN and snake_direction != up:
                snake_direction = down
            elif event.key == pygame.K_LEFT and snake_direction != right:
                snake_direction = left
            elif event.key == pygame.K_RIGHT and snake_direction != left:
                snake_direction = right
    
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0,new_head)

    if snake[0] == food:
        score += 1
        food = (random.randint(0,grid_width-1),random.randint(0,grid_height-1))
    else:
        snake.pop()
    
    if (snake[0] in snake[1:] or 
        snake[0][0] < 0 or snake[0][0] >= grid_width or 
        snake[0][1] < 0 or snake[0][1] >= grid_height):
        running = False

    screen.fill(black)
    for segment in snake:
        pygame.draw.rect(screen, green, (segment[0]*grid_size, segment[1]*grid_size, grid_size, grid_size))
    pygame.draw.rect(screen, red, (food[0]*grid_size, food[1]*grid_size, grid_size, grid_size))

    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10,10))
    pygame.display.flip()

    clock.tick(snake_speed)

end_text = font.render(f"Game Over! Score: {score}", True, red)
screen.fill(white)
screen.blit(end_text, (width//2 - end_text.get_width()//2, height//2 - end_text.get_height()//2))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()