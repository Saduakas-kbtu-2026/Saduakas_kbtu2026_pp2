import pygame

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball properties
radius = 25
x = WIDTH // 2
y = HEIGHT // 2
step = 20

clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            # Move UP
            if event.key == pygame.K_UP:
                if y - step - radius >= 0:
                    y -= step

            # Move DOWN
            elif event.key == pygame.K_DOWN:
                if y + step + radius <= HEIGHT:
                    y += step

            # Move LEFT
            elif event.key == pygame.K_LEFT:
                if x - step - radius >= 0:
                    x -= step

            # Move RIGHT
            elif event.key == pygame.K_RIGHT:
                if x + step + radius <= WIDTH:
                    x += step

    # Draw
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
