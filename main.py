import pygame
import random

# Initialize pygame
pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Aeroplane Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()

# Plane
plane_img = pygame.image.load("plane.png")
plane_x = 370
plane_y = 500
plane_speed = 5

# Obstacles
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacles = []

# Score
score = 0
font = pygame.font.SysFont(None, 35)

def show_score():
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Plane movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and plane_x > 0:
        plane_x -= plane_speed
    if keys[pygame.K_RIGHT] and plane_x < 800 - plane_img.get_width():
        plane_x += plane_speed
    
    # Obstacles
    if random.randint(1, 50) == 1:
        obstacles.append([random.randint(0, 750), -50])
    
    for obs in obstacles:
        obs[1] += obstacle_speed
        pygame.draw.rect(screen, RED, (obs[0], obs[1], obstacle_width, obstacle_height))
        
        # Collision
        if (plane_y <
