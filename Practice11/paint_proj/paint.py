
import pygame
import math



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
                #q, w ,e ,a ,s, d
                # Tools
                if event.key == pygame.K_q:
                    tool = "eq_triangle"
                elif event.key == pygame.K_w:
                    tool = "rect"
                elif event.key == pygame.K_e:
                    tool = "eraser"
                elif event.key == pygame.K_r:
                    tool = "rhombus"
                elif event.key == pygame.K_a:
                    tool = "ri_triangle"
                elif event.key == pygame.K_s:
                    tool = "square"
                elif event.key == pygame.K_d:
                    tool = "brush"
                elif event.key == pygame.K_f:
                    tool = "circle"
                

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
                
                if tool == "eq_triangle":
                    drawEqTriangle(canvas, color, start_pos,end_pos,radius)
    
                elif tool == "rect":
                    rect = pygame.Rect(start_pos, 
                        (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    pygame.draw.rect(canvas, color, rect, 2)

                elif tool == "rhombus":
                    drawRhombus(canvas, color, start_pos, end_pos, radius)

                elif tool == "ri_triangle":
                    drawRiTriangle(canvas, color,start_pos,end_pos, radius)

                elif tool == "square":
                    drawSquare(canvas, color,start_pos,end_pos, radius)

                elif tool == "circle":
                    dx = end_pos[0] - start_pos[0]
                    dy = end_pos[1] - start_pos[1]
                    radius_circle = int((dx**2 + dy**2) ** 0.5)
                    pygame.draw.circle(canvas, color, start_pos, radius_circle, 2)
                
            #brush and eraser
            if event.type == pygame.MOUSEMOTION and drawing:
                if tool == "brush" or tool == "eraser":
                    points.append(event.pos)
        # Drawing
        if drawing and (tool == "brush" or tool == "eraser"):
            for i in range(len(points) - 1):
                drawLine(canvas, points[i], points[i + 1], radius,
                         (0, 0, 0) if tool == "eraser" else color)

        font = pygame.font.SysFont(None, 20)
        text_color = font.render("1 - red, 2 - green, 3 - blue, 4 - white, 5 - yellow ", True, (255,255,255))
        text = font.render("q - eq. triangle | w - rectangle | e - eraser         | r - rhombus", True, (255, 255, 0))
        text1 = font.render("a - ri. triangle   | s - square      | d - draw/brush | f - circle", True, (255, 255, 0))
        text_c_rect = text.get_rect(topleft=(0, 10))
        text_rect = text.get_rect(topleft=(0, 30))
        text_rect1 = text1.get_rect(topleft=(0, 50))
        

        screen.blit(canvas, (0, 0))
        screen.blit(text_color, text_c_rect)
        screen.blit(text, text_rect)
        screen.blit(text1, text_rect1)
        pygame.display.flip()
        clock.tick(60)

def drawSquare(screen, color, start, end, width):
    dx =end[0] - start[0]
    dy = end[0] - start[0]
    radius = int((dx**2 + dy**2)**0.5)
    pygame.draw.rect(screen,color, (start, (radius, radius)),width)

def drawRhombus(screen, color, start, end, width):
    dx =end[0] - start[0]
    dy = end[0] - start[0]
    radius = int((dx**2 + dy**2)**0.5)
    (x1, y1) = (start[0]+radius, start[1])#first coord
    (x2, y2) = (start[0], start[1]+radius)#nd coord
    (x3, y3) = (start[0]-radius, start[1])#rd coord
    (x4, y4) = (start[0], start[1]-radius)#th coord
    points = ((x1,y1),(x2,y2),(x3,y3),(x4,y4))
    pygame.draw.lines(screen, color,True, points, width)
    
def drawEqTriangle(screen, color, start, end, width):
    dx =end[0] - start[0]
    dy = end[0] - start[0]
    radius = int((dx**2 + dy**2)**0.5)
    pi = math.pi
    angle = pi/6
    (x1, y1) = (start[0], start[1]-radius)#st coord
    (x2, y2) = (start[0]+radius*math.cos(angle), start[1]+radius*math.sin(angle))#nd coord
    (x3, y3) = (start[0]-radius*math.cos(angle), start[1]+radius*math.sin(angle))#rd coord
    points = ((x1,y1),(x2,y2),(x3,y3))
    pygame.draw.lines(screen, color,True, points, width)

def drawRiTriangle(screen, color, start, end, width):
    dx =end[0] - start[0]
    dy = end[0] - start[0]
    radius = int((dx**2 + dy**2)**0.5)
    side_length = int((radius**2+radius**2)**0.5)
    (x1, y1) = (start[0], start[1]-radius/2)#st coord | half radius so it apears on center of triangle
    (x2, y2) = (start[0]+side_length, start[1]+radius/2)#nd coord
    (x3, y3) = (start[0]-side_length, start[1]+radius/2)#rd coord
    points = ((x1,y1),(x2,y2),(x3,y3))
    pygame.draw.lines(screen, color,True, points, width)

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
