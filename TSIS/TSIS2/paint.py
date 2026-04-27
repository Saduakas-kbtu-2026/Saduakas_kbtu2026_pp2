import pygame
import math
from datetime import datetime


#✅ Ctrl+S saves canvas as timestamped .png


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius_sizes = [2,5,10]
    radius = radius_sizes[1]
    color = (0, 0, 255)
    tool = "brush"

    drawing = False
    start_pos = None
    points = []

    canvas = pygame.Surface(screen.get_size())
    canvas.fill((0, 0, 0))

    text_mode = False
    text_buffer = ''
    text_pos = []

    line_preview = False
    line_start = []
    line_end = []
    

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_s) and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    filename = f"canvas_{timestamp}.png"
                    pygame.image.save(canvas, filename)
                    print("Saved:", filename)

                # TEXT TOOL HANDLING
                if text_mode:
                    if event.key == pygame.K_RETURN:
                        rendered = font.render(text_buffer, True, color)
                        canvas.blit(rendered, text_pos)
                        text_mode = False
                        text_buffer = ""

                    elif event.key == pygame.K_ESCAPE:
                        text_mode = False
                        text_buffer = ""

                    elif event.key == pygame.K_BACKSPACE:
                        text_buffer = text_buffer[:-1]

                    else:
                        text_buffer += event.unicode

                    continue

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
                    tool = "bucket"
                elif event.key == pygame.K_c:
                    tool = "circle"
                elif event.key == pygame.K_z:
                    tool = "pencil"
                elif event.key == pygame.K_t:
                    tool = "text"
                elif event.key == pygame.K_x:
                    tool = "str_line"
                    line_preview = True
                
                elif event.key == pygame.K_7:
                    radius = radius_sizes[0]
                elif event.key == pygame.K_8:
                    radius = radius_sizes[1]
                elif event.key == pygame.K_9:
                    radius = radius_sizes[2]


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
                line_start = start_pos
                line_preview = True


            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                end_pos = event.pos
                line_start = []
                line_end = []
            

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
                
                elif tool == "bucket":
                    target = canvas.get_at(end_pos)
                    flood_fill(canvas, (end_pos), target, color)
                
                elif tool == "text":
                    text_mode = True
                    text_pos = end_pos
                    text_buffer = ""
                
                # FINAL LINE DRAW
                elif tool == "str_line":
                    if not drawing:
                        pygame.draw.line(canvas, color, start_pos, end_pos, radius)
                        line_preview = False
                

            #brush and eraser
            if event.type == pygame.MOUSEMOTION and drawing:
                if tool == "brush" or tool == "eraser" or tool == "pencil":
                    points.append(event.pos)
                # LIVE LINE PREVIEW
                if tool == "str_line" and line_preview:
                    line_end = event.pos
        # Drawing
        if drawing and (tool == "brush" or tool == "eraser"):
            for i in range(len(points) - 1):
                drawLine(canvas, points[i], points[i + 1], radius,
                         (0, 0, 0) if tool == "eraser" else color)
        if drawing and tool == "pencil":
            for i in range(len(points) - 1):
                drawPencil(canvas, points[i], points[i+1], radius, color)

        font = pygame.font.SysFont(None, 20)
        text_color = font.render("1 - red, 2 - green, 3 - blue, 4 - white, 5 - yellow   | 7 - small brush, 8 - medium brush, 9 - large brush", True, (255,255,255))
        text = font.render("q - eq. triangle | w - rectangle | e - eraser         | r - rhombus | t - text   | x - line | Ctrl+S - Save", True, (255, 255, 0))
        text1 = font.render("a - ri. triangle   | s - square      | d - draw/brush | f - bucket  | c - circle | z - pencil", True, (255, 255, 0))
        text_c_rect = text.get_rect(topleft=(0, 10))
        text_rect = text.get_rect(topleft=(0, 30))
        text_rect1 = text1.get_rect(topleft=(0, 50))
        
        #text rendering
        if text_mode and text_pos:
            preview = font.render(text_buffer, True, color)
            screen.blit(preview, text_pos)

        screen.blit(canvas, (0, 0))

        #line preview
        if tool == "str_line" and line_preview and line_start and line_end:
            temp_surface = canvas.copy()
            pygame.draw.line(temp_surface, color, line_start, line_end, radius)
            screen.blit(temp_surface, (0, 0))
        else:
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

def drawPencil(screen, start,end, width, color):
    pygame.draw.lines(screen, color, False, (start, end), width)

def flood_fill(surface, pos, target_color, replacement_color):
    if target_color == replacement_color:
        return

    width, height = surface.get_size() #get size of canvas
    stack = [(pos)]

    while stack:
        cx, cy = stack.pop()

        if cx < 0 or cy < 0 or cx >= width or cy >= height: #loops through coord
            continue
        #if pixel at these point is not target color
        if surface.get_at((cx, cy)) != target_color: 
            continue

        surface.set_at((cx, cy), replacement_color) #replace them at point

        stack.append((cx + 1, cy))
        stack.append((cx - 1, cy))
        stack.append((cx, cy + 1))
        stack.append((cx, cy - 1))


main()
