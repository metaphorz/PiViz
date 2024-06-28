import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pi Spiral Visualization")

# Colors for digits 0-9
colors = [
    (255, 0, 0),    # Red
    (255, 127, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (75, 0, 130),   # Indigo
    (143, 0, 255),  # Violet
    (255, 192, 203),# Pink
    (255, 255, 255),# White
    (128, 128, 128) # Gray
]

# Highlight color for the start of Pi
highlight_color = (255, 0, 255)  # Magenta

# Generate Pi digits
def generate_pi_digits(num_digits):
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    decimal_digits = []
    while len(decimal_digits) < num_digits:
        if 4 * q + r - t < n * t:
            decimal_digits.append(n)
            q, r, t, k, n, l = (10*q, 10*(r-n*t), t, k, (10*(3*q+r))//t - 10*n, l)
        else:
            q, r, t, k, n, l = (q*k, (2*q+r)*l, t*l, k+1, (q*(7*k+2)+r*l)//(t*l), l+2)
    return decimal_digits

# Generate 1000 digits of Pi
pi_digits = generate_pi_digits(1000)

# Set up the spiral
center_x, center_y = width // 2, height // 2
max_radius = min(width, height) // 2 - 10
spiral_constant = 0.1

# Font setup
font = pygame.font.Font(None, 36)

# Main loop
running = True
clock = pygame.time.Clock()
digit_index = 0
circle_positions = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Black background

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Draw the spiral and store circle positions
    circle_positions = []
    for i in range(digit_index):
        angle = i * spiral_constant
        radius = max_radius * (1 - i / 1000)
        x = int(center_x + radius * math.cos(angle))
        y = int(center_y + radius * math.sin(angle))
        color = highlight_color if i == 1 else colors[pi_digits[i]]  # Highlight the second digit (first after decimal)
        circle_radius = int(5 * (1 - i / 1000)) + 1
        pygame.draw.circle(screen, color, (x, y), circle_radius)
        circle_positions.append((x, y, circle_radius, pi_digits[i]))

    # Check for hover and display digit
    for x, y, radius, digit in circle_positions:
        if math.sqrt((mouse_x - x)**2 + (mouse_y - y)**2) <= radius:
            text = font.render(str(digit), True, (255, 255, 255))
            text_rect = text.get_rect(center=(x, y - 20))
            screen.blit(text, text_rect)
            break  # Display only for the topmost circle

    pygame.display.flip()

    # Increment the number of digits shown
    if digit_index < 1000:
        digit_index += 1

    clock.tick(60)  # Limit to 60 FPS

pygame.quit()