import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

snake = [(100, 100)]
dx, dy = CELL_SIZE, 0
foods = []
food_timer = 0
score = 0

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dy == 0:
        dx, dy = 0, -CELL_SIZE
    elif keys[pygame.K_DOWN] and dy == 0:
        dx, dy = 0, CELL_SIZE
    elif keys[pygame.K_LEFT] and dx == 0:
        dx, dy = -CELL_SIZE, 0
    elif keys[pygame.K_RIGHT] and dx == 0:
        dx, dy = CELL_SIZE, 0

    new_head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, new_head)

    eaten = False
    for food in foods[:]:
        if pygame.Rect(food["pos"], (CELL_SIZE, CELL_SIZE)).collidepoint(new_head):
            score += food["weight"]
            foods.remove(food)
            eaten = True
            break
    if not eaten:
        snake.pop()

    if food_timer == 0:
        foods.append({
            "pos": (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                     random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE),
            "weight": random.randint(1, 3),
            "time": 200
        })
        food_timer = 100
    else:
        food_timer -= 1

    for food in foods[:]:
        food["time"] -= 1
        if food["time"] <= 0:
            foods.remove(food)

    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(segment, (CELL_SIZE, CELL_SIZE)))
    for food in foods:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food["pos"], (CELL_SIZE, CELL_SIZE)))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
