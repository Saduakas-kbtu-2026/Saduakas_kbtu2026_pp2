import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 5
    color = (0, 0, 255)
    tool = "brush"

    drawing = False
    start_pos = None
    points = []

    canvas = pygame.Surface(screen.get_size())
    canvas.fill((0, 0, 0))

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

                # Tools
                if event.key == pygame.K_b:
                    tool = "brush"
                elif event.key == pygame.K_r:
                    tool = "rect"
                elif event.key == pygame.K_c:
                    tool = "circle"
                elif event.key == pygame.K_e:
                    tool = "eraser"

                # Colors
                elif event.key == pygame.K_1:
                    color = (255, 0, 0)  # red
                elif event.key == pygame.K_2:
                    color = (0, 255, 0)  # green
                elif event.key == pygame.K_3:
                    color = (0, 0, 255)  # blue
                elif event.key == pygame.K_4:
                    color = (255, 255, 255)  # white
                elif event.key == pygame.K_5:
                    color = (255, 255, 0)  # yellow

            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = event.pos
                points = [event.pos]

            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                end_pos = event.pos

                if tool == "rect":
                    rect = pygame.Rect(start_pos, 
                        (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    pygame.draw.rect(canvas, color, rect, 2)

                elif tool == "circle":
                    dx = end_pos[0] - start_pos[0]
                    dy = end_pos[1] - start_pos[1]
                    radius_circle = int((dx**2 + dy**2) ** 0.5)
                    pygame.draw.circle(canvas, color, start_pos, radius_circle, 2)

            if event.type == pygame.MOUSEMOTION and drawing:
                if tool == "brush" or tool == "eraser":
                    points.append(event.pos)

        # Drawing
        if drawing and (tool == "brush" or tool == "eraser"):
            for i in range(len(points) - 1):
                drawLine(canvas, points[i], points[i + 1], radius,
                         (0, 0, 0) if tool == "eraser" else color)

        screen.blit(canvas, (0, 0))
        pygame.display.flip()
        clock.tick(60)


def drawLine(screen, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    steps = max(abs(dx), abs(dy))

    for i in range(steps):
        t = i / steps
        x = int(start[0] * (1 - t) + end[0] * t)
        y = int(start[1] * (1 - t) + end[1] * t)
        pygame.draw.circle(screen, color, (x, y), width)


main()
