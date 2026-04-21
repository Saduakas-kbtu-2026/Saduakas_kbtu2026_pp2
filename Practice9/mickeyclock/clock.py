import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((1400, 1050))
done = False

mickey_img = pygame.image.load("mickeyclock.jpeg")
mickey_right = pygame.image.load("mickeyclock_right_hand.png")
mickey_left = pygame.image.load("mickeyclock_left_hand.png")

# Define the CENTER of the clock (pivot point)
clock_center = (750, 525)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now = datetime.now()
    h_time = int(now.strftime("%H"))
    m_time = int(now.strftime("%M"))

    # Better angles
    hour_angle = -(h_time % 12) * 30 - 45
    minute_angle = -m_time * 6 + 45

    # Rotate images
    rotated_left = pygame.transform.rotate(mickey_left, hour_angle)
    rotated_right = pygame.transform.rotate(mickey_right, minute_angle)

    # Get rects centered at clock center
    left_rect = rotated_left.get_rect(center=clock_center)
    right_rect = rotated_right.get_rect(center=clock_center)

    # Draw everything
    screen.fill((0, 0, 0))
    screen.blit(mickey_img, (0, 0))
    screen.blit(rotated_right, right_rect)
    screen.blit(rotated_left, left_rect)

    pygame.display.flip()
