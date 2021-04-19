import pygame

pygame.init()
all_rects = []

NAME_TO_RGBA = pygame.color.THECOLORS
RGBA_TO_NAME = {}
for name, rgb in NAME_TO_RGBA.items():
    if rgb in RGBA_TO_NAME:
        RGBA_TO_NAME[rgb].append(name)
    else:
        RGBA_TO_NAME[rgb] = [name]

font = pygame.font.SysFont("monospace", 20)


blue = (0,0,255)

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))

class Rect():
    def __init__(self,name, color, x, y):
        self.rect = pygame.Rect(10,10,10,10)
        self.rect.x = x
        self.rect.y = y
        self.name = name
        self.color = color
        all_rects.append(self)
    def Draw(self):
        pygame.draw.rect(screen, (self.color), self.rect)

class ColorPicker():
    def __init__(self):
        self.colors = RGBA_TO_NAME
        self.MakeGrid()
    def MakeGrid(self):
        x, y = 600, 200
        i = 0
        for col, name in self.colors.items():
            rect = Rect(name, col, x, y)
            x += 10
            i += 1
            if i == 25:
                i = 0
                y += 10
                x = 600

isPressed = False


name_label = font.render("", 1, (255,255,255))
color_label = font.render("", 1, (255,255,255))


currentTool = 0
toolCount = 3
curColor=blue
def drawRectangle(surface, x,y, w, h):
    pygame.draw.rect(surface, curColor, [x, y, w, h],5)

def drawCircle(surface, x,y):
    pygame.draw.circle(surface, curColor, (x, y), 50, 5)

def drawLine(surface, startPos, endPos):
    pygame.draw.line(surface, curColor, startPos, endPos, 5)

def saved():
    global isPressed, currentTool,toolCount,curColor

    with open('save.txt', mode='r') as f:
        data = f.read().splitlines()

    name_label = font.render("", 1, (255,255,255))
    color_label = font.render("", 1, (255,255,255))
    isPressed = False
    currentTool = 0
    toolCount = 3
    curColor=blue
    ColorPicker()
    screen.fill((255,255,255))
    for i in eval(data[0]):
        drawLine(screen, i[0], i[1])

    for i in eval(data[1]):
        drawRectangle(screen, i[0],i[1], 100, 100)
    for i in eval(data[2]):
        drawCircle(screen, i[0],i[1])
    saves={0:eval(data[0]),1:eval(data[1]),2:eval(data[2])}
    go=True
    while go:

        mx,my = pygame.mouse.get_pos()
        prevPoint = pygame.mouse.get_pos()
        curPoint = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    currentTool = (currentTool + 1) % toolCount
                if event.key == pygame.K_SPACE:
                    screen.fill((255,255,255))
                if event.key == pygame.K_s:
                    with open('save.txt', mode='w') as f:
                        for k,v in saves.items():
                            f.write("%s \n" % (v))
                        f.close()
                    go=False
            if event.type == pygame.MOUSEBUTTONDOWN and mx <500:
                isPressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                isPressed = False
                prevPoint =pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEMOTION and isPressed == True and mx<500:
                prevPoint = curPoint
                curPoint = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and mx>500:
                if event.button == 1:
                    for rect in all_rects:
                        if rect.rect.collidepoint((mx,my)):
                            name_label = font.render(str(rect.name), 1, (0,0,0))
                            color_label = font.render(str(rect.color), 1, (0,0,0))
                            curColor=rect.color

        if currentTool == 0 and isPressed:
            drawLine(screen, prevPoint, curPoint)
            saves[currentTool % toolCount].append((prevPoint, curPoint))
        elif currentTool == 1 and isPressed:
            drawRectangle(screen, curPoint[0],curPoint[1],100,100)
            saves[currentTool % toolCount].append((curPoint[0],curPoint[1]))
        elif currentTool == 2 and isPressed:
            drawCircle(screen,curPoint[0],curPoint[1])
            saves[currentTool  % toolCount].append((curPoint[0],curPoint[1]))


        background = pygame.Surface((500, 500))
        background.fill((255, 255, 255))
        screen.blit(background, (500, 0))
        screen.blit(name_label, (600, 50))
        screen.blit(color_label, (600, 100))
        for rect in all_rects:
            rect.Draw()

        pygame.draw.rect(screen, (0,0,0), [500, 0, 500, 500],5)

        pygame.display.flip()

def single():
    global isPressed, currentTool,toolCount,curColor
    name_label = font.render("", 1, (255,255,255))
    color_label = font.render("", 1, (255,255,255))
    isPressed = False
    currentTool = 0
    toolCount = 3
    curColor=blue
    ColorPicker()
    screen.fill((255,255,255))
    saves={0:[],1:[],2:[]}
    go=True
    while go:

        mx,my = pygame.mouse.get_pos()
        prevPoint = pygame.mouse.get_pos()
        curPoint = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    currentTool = (currentTool + 1) % toolCount
                if event.key == pygame.K_SPACE:
                    saves={0:[],1:[],2:[]}
                    screen.fill((255,255,255))
                if event.key == pygame.K_s:
                    with open('save.txt', mode='w') as f:
                        for k,v in saves.items():
                            f.write("%s \n" % (v))
                        f.close()
                        go=False
            if event.type == pygame.MOUSEBUTTONDOWN and mx <500:
                isPressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                isPressed = False
                prevPoint =pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEMOTION and isPressed == True and mx<500:
                prevPoint = curPoint
                curPoint = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and mx>500:
                if event.button == 1:
                    for rect in all_rects:
                        if rect.rect.collidepoint((mx,my)):
                            name_label = font.render(str(rect.name), 1, (0,0,0))
                            color_label = font.render(str(rect.color), 1, (0,0,0))
                            curColor=rect.color

        if currentTool == 0 and isPressed:
            drawLine(screen, prevPoint, curPoint)
            saves[currentTool  % toolCount].append([prevPoint, curPoint])
        elif currentTool == 1 and isPressed:
            drawRectangle(screen, curPoint[0],curPoint[1],100,100)
            saves[currentTool  % toolCount].append(curPoint)
        elif currentTool == 2 and isPressed:
            drawCircle(screen,curPoint[0],curPoint[1])
            saves[currentTool % toolCount].append(curPoint)


        background = pygame.Surface((500, 500))
        background.fill((255, 255, 255))
        screen.blit(background, (500, 0))
        screen.blit(name_label, (600, 50))
        screen.blit(color_label, (600, 100))
        for rect in all_rects:
            rect.Draw()

        pygame.draw.rect(screen, (0,0,0), [500, 0, 500, 500],5)

        pygame.display.flip()

click=False
def draw_text(text,font1,color,surface,x,y):
    textobj = font1.render(text,1,color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj,textrect)
font1 = pygame.font.SysFont('TimesNewRoman',50)
def MainMenu():
    global click
    click = False
    while True:
        screen.fill((240,230,140))

        mx,my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(150,200,400,50)
        button_2 = pygame.Rect(150,300,400,50)
        pygame.draw.rect(screen,(220,20,60),button_1)
        pygame.draw.rect(screen,(220,20,60),button_2)
        draw_text('New Picture',font1,(0,0,0),screen,150,200)
        draw_text('Saved Picture',font1,(0,0,0),screen,150,300)
        draw_text('Paint',pygame.font.SysFont('Lucida Handwriting',75),(220,20,60),screen,150,50)

        if button_1.collidepoint((mx,my)):
            draw_text('New Picture',font1,(255,255,255),screen,150,200)
            if click :
                single()
        if button_2.collidepoint((mx,my)):
            draw_text('Saved Picture',font1,(255,255,255),screen,150,300)
            if click:
               saved()

        click=False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        pygame.time.Clock().tick(30)

MainMenu()
