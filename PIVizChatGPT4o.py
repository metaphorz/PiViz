import pygame
import numpy as np
from mpmath import mp

# Function to generate Pi digits
def get_pi_digits(n):
    mp.dps = n + 1  # set number of decimal places
    pi_str = str(mp.pi)  # get pi as string
    return pi_str.replace('.', '')[:n + 1]  # remove the decimal point and include the '3'

# Initialize Pygame
pygame.init()

# Set the number of digits
num_digits = 500
pi_digits = get_pi_digits(num_digits)

# Define colors for digits 0-9
colors = [
    (255, 0, 0),       # Red
    (255, 165, 0),     # Orange
    (255, 255, 0),     # Yellow
    (0, 128, 0),       # Green
    (0, 0, 255),       # Blue
    (75, 0, 130),      # Indigo
    (238, 130, 238),   # Violet
    (0, 255, 255),     # Cyan
    (255, 0, 255),     # Magenta
    (0, 255, 0),       # Lime
]

# Screen dimensions
width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pi Digits Spiral')

# Spiral parameters
max_radius = min(width, height) // 2 - 20
spacing = 15
max_circle_radius = 20
min_circle_radius = 2

# Store circle positions and radii
circles = []

# Create the spiral of circles
for i, digit in enumerate(pi_digits):
    angle = 0.1 * i
    radius = max_radius - spacing * np.sqrt(i)
    if radius < min_circle_radius:
        break
    x = int(width // 2 + radius * np.cos(angle))
    y = int(height // 2 + radius * np.sin(angle))
    circle_radius = max(min_circle_radius, int(max_circle_radius * (radius / max_radius)))
    circles.append((x, y, circle_radius, digit))

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill((0, 0, 0))

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Draw the circles
    for x, y, circle_radius, digit in circles:
        color = colors[int(digit)]
        pygame.draw.circle(screen, color, (x, y), circle_radius)

        # Check if mouse is hovering over the circle
        if (x - mouse_pos[0]) ** 2 + (y - mouse_pos[1]) ** 2 <= circle_radius ** 2:
            font = pygame.font.Font(None, 36)
            text = font.render(digit, True, (255, 255, 255))
            text_rect = text.get_rect(center=(x, y))
            screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
