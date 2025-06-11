import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

snake = [(250, 250)]
snake_dir = (0,0)
food = pygame.Rect(random.randrange(0, 560, 40), 
                   random.randrange(0, 560, 40), 40, 40)
score = 0
font = pygame.font.Font(None, 48)

def reset_game():
    global snake, snake_dir, score, food
    snake = [(200, 200)]
    snake_dir = (0, 0)
    food.topleft = (random.randrange(0, 560, 40),
                    random.randrange(0, 560, 40))
    score = 0
def game_over_screen():
    while True:
           screen.fill((0, 0, 0))
           game_over_text = font.render("Game Over!", True, (255, 0, 0))
           score_text = font.render(f"Score: {score}", True, (153, 153, 255))
           play_again_text = font.render("Play Again", True, (255, 255, 255))
           exit_text = font.render("Exit", True, (255, 255, 255))

           #Button
           #pygame.Rect(left, top, width, height) creates rectangle object
           play_again_rect = pygame.Rect(200, 300, 200, 50)
           exit_rect = pygame.Rect(200, 400, 200, 50)

           #function is used to draw a rectangle shape on a surface
           # pygame.draw.rect(surface, color, 
           # rect: the rectangle's position (ex: pygame.Rect or (x, y, width, height)), 
           # width = 0)
           pygame.draw.rect(screen, (160, 160, 160), play_again_rect)
           pygame.draw.rect(screen, (160, 160, 160), exit_rect)

           #screen.blit: block transfer -> display the context into screen in the posion (x, y) 
           screen.blit(game_over_text, (200, 170))
           screen.blit(score_text, (200, 220))
           screen.blit(play_again_text, (play_again_rect.x + 20, play_again_rect.y + 6))
           screen.blit(exit_text, (exit_rect.x + 60, exit_rect.y + 6))

           #update the entire game 
           pygame.display.flip()

           for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                       
                       #collidepoint check if the mouse click at the position of the rectangle block
                       if play_again_rect.collidepoint(event.pos):
                            reset_game()
                            return
                       elif exit_rect.collidepoint(event.pos):
                            pygame.quit()
                            exit()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and snake_dir != (0, 40):
                snake_dir = (0, -40)
    elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and snake_dir != (0, -40):
                snake_dir = (0, 40)
    elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and snake_dir != (40, 0):
                snake_dir = (-40, 0)
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and snake_dir != (-40, 0):
                snake_dir = (40, 0)

    if snake_dir != (0, 0):
        head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
        snake.insert(0, head)

        #Check if 2 rectangle blocks are overlap
        if pygame.Rect(head, (40, 40)).colliderect(food):
            score += 1
            food.topleft = (random.randrange(0, 560, 40),
                            random.randrange(0, 560, 40))
        else:
            snake.pop()

        if (head in snake[1:] or head[0] < 0 or head[0] >= 600 or head[1] < 0 or head[1] >= 600):
                game_over_screen()
        
    screen.fill((127, 255, 212))
    for pos in snake:
        pygame.draw.rect(screen, (255, 153, 204), (pos[0], pos[1], 40, 40))

    pygame.draw.circle(screen, (255, 51, 51), food.center, 20)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (20, 20))
    pygame.display.flip()
    clock.tick(8)

pygame.quit()