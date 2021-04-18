import pygame
import random
import time

pygame.init()

WIDTH = 600
HEIGHT = 600

RED = (255, 0, 0)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
FPS = 30
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

class Snake:
    def __init__(self, color):
        self.size = 3
        self.elements = [[300, 300], [120, 100], [140, 100]]
        self.radius = 10
        self.speed = 5
        self.dx = self.speed
        self.dy = 0
        self.is_add = False
        self.color = color
        self.score = 0

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, self.color, element, self.radius)

    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False
        self.score +=1

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

class Food:
    def __init__(self):
        self.x = random.randint(100, WIDTH - 70)
        self.y = random.randint(100, HEIGHT - 70)
        self.image = pygame.transform.scale(pygame.image.load("food.png"), [30, 30])

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

def show_score(x, y, score, color):
    show = font.render("Score: " + str(score), True, color)
    screen.blit(show, (x, y))

def collision():
    if food.x < snake.elements[0][0]+snake.radius and food.x+35 > snake.elements[0][0] - snake.radius and food.y  < snake.elements[0][1] + snake.radius  and food.y+35> snake.elements[0][1] - snake.radius:
        snake.is_add = True
        food.x = random.randint(50, WIDTH - 70)
        food.y = random.randint(50, HEIGHT - 70)
    if food.x <snake2.elements[0][0]+snake2.radius and food.x+35 >snake2.elements[0][0] - snake2.radius and food.y  < snake2.elements[0][1] + snake2.radius  and food.y+35> snake2.elements[0][1] - snake2.radius:
        snake2.is_add = True
        food.x = random.randint(50, WIDTH - 70)
        food.y = random.randint(50, HEIGHT - 70)

def create_map(level_num):
    global gm
    with open(f'lvl/{level_num}.txt', mode='r') as file:
        row_num = 0  # row number
        for row in file:
            for block_num in range(len(row)):
                if row[block_num] == '1':
                    screen.blit(wall_image, (block_num*30,row_num*40))
                    if snake.elements[0][0]>block_num*30 and snake.elements[0][0]<block_num*30 +29 and snake.elements[0][1]>row_num*40 and snake.elements[0][1]<row_num*40 + 44:
                        gm = True
                    if snake2.elements[0][0]>block_num*30 and snake2.elements[0][0]<block_num*30 +29 and snake2.elements[0][1]>row_num*40 and snake2.elements[0][1]<row_num*40 + 44:
                        gm = True

            row_num += 1

def game_over():
    screen.fill((255, 0, 0))
    txt = font.render('GAME OVER!', True, (255, 255, 255))
    if snake.score >snake2.score:
        my_score = font.render('Snake 1 win Total score: ' + str(snake.score)+'-' + str(snake2.score) , True, (255, 255, 255))
    elif snake2.score > snake.score:
        my_score = font.render('Snake 2 win Total score: ' + str(snake2.score)+'-' + str(snake.score) , True, (255, 255, 255))
    else:
        my_score = font.render('Draw Total score: ' + str(snake.score)+' ' + str(snake2.score) , True, (255, 255, 255))

    screen.blit(txt, (200, 200))
    screen.blit(my_score, (100, 300))
    pygame.display.flip()
    time.sleep(3)
    gm = False

snake = Snake(RED)
snake2 = Snake(YELLOW)
food = Food()

wall_image = pygame.transform.scale(pygame.image.load("wall.png"), [30, 45])
gm = False
go = True
def single():
    global gm, go, snake, snake2, food
    gm = False
    snake = Snake(RED)
    snake2 = Snake(YELLOW)
    food = Food()
    stop=True
    while go:
        collision()
        screen.fill((165, 206, 216))
        sc=snake.score//5
        sc2=snake2.score//5
        if sc>sc2:
            snake.speed+=1
            snake2.speed+=1
        elif sc2>sc:
            snake.speed+=1
            snake2.speed+=1
        create_map(max(sc2,sc)+1)
        mil = clock.tick(FPS)
        if gm:
            game_over()
            go = False
        snake.move()
        snake.draw()
        snake2.move()
        snake2.draw()
        food.draw()
        show_score(35, 45, snake.score, RED)
        show_score(435, 45, snake2.score, YELLOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                go = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.dx = snake.speed
                    snake.dy = 0
                if event.key == pygame.K_LEFT:
                    snake.dx = -snake.speed
                    snake.dy = 0
                if event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -snake.speed
                if event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = snake.speed
                if event.key == pygame.K_d:
                    snake2.dx = snake2.speed
                    snake2.dy = 0
                if event.key == pygame.K_a:
                    snake2.dx = -snake2.speed
                    snake2.dy = 0
                if event.key == pygame.K_w:
                    snake2.dx = 0
                    snake2.dy = -snake2.speed
                if event.key == pygame.K_s:
                    snake2.dx = 0
                    snake2.dy = snake2.speed
                if event.key == pygame.K_k:
                    saves=[snake.elements,snake2.elements,snake.score,snake2.score,food.x,food.y,snake.dx,snake.dy,
                    snake2.dx,snake2.dy,snake.size,snake2.size]
                    with open('lvl/save.txt', mode='w') as f:
                        for i in saves:
                            f.write("%s \n" % (i))
                        f.close()
                    go=False
                if event.key == pygame.K_SPACE:
                    stop = True
            while stop:
                    screen.fill((165, 206, 216))
                    create_map(1)
                    mil = clock.tick(FPS)
                    snake.draw()
                    snake2.draw()
                    food.draw()
                    show_score(35, 45, snake.score,RED)
                    show_score(435, 45, snake2.score,YELLOW)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            stop=False
                            go = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                stop = False
        pygame.display.flip()
    go=True

def saved_game():
    global gm,go,snake,snake2,food

    with open('lvl/save.txt', mode='r') as f:
        data = f.read().splitlines()
    gm=False
    snake = Snake(RED)
    snake2 = Snake(BLUE)
    food = Food()
    stop=True
    snake.elements=eval(data[0])
    snake2.elements=eval(data[1])
    snake.score=eval(data[2])
    snake2.score=eval(data[3])
    food.x=eval(data[4])
    food.y=eval(data[5])
    snake.dx=eval(data[6])
    snake.dy=eval(data[7])
    snake2.dx=eval(data[8])
    snake2.dy=eval(data[9])
    snake.size=eval(data[10])
    snake2.size=eval(data[11])
    f.close()
    while go:

        collision()
        screen.fill((165, 206, 216))
        sc=snake.score//5
        sc2=snake2.score//5
        create_map(max(sc2,sc)+1)
        mil = clock.tick(FPS)
        if gm:
            game_over()
            go = False
        snake.move()
        snake.draw()
        snake2.move()
        snake2.draw()
        food.draw()
        show_score(35, 45, snake.score,RED)
        show_score(435, 45, snake2.score,YELLOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                go = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.dx = snake.speed
                    snake.dy = 0
                if event.key == pygame.K_LEFT:
                    snake.dx = -snake.speed
                    snake.dy = 0
                if event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -snake.speed
                if event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = snake.speed
                if event.key == pygame.K_d:
                    snake2.dx = snake2.speed
                    snake2.dy = 0
                if event.key == pygame.K_a:
                    snake2.dx = -snake2.speed
                    snake2.dy = 0
                if event.key == pygame.K_w:
                    snake2.dx = 0
                    snake2.dy = -snake2.speed
                if event.key == pygame.K_s:
                    snake2.dx = 0
                    snake2.dy = snake2.speed
                if event.key == pygame.K_k:
                    saves=[snake.elements,snake2.elements,snake.score,snake2.score,food.x,food.y,snake.dx,snake.dy,
                    snake2.dx,snake2.dy,snake.size,snake2.size]
                    with open('lvl/save.txt', mode='w') as f:
                        for i in saves:
                            f.write("%s \n" % (i))
                        f.close()
                    go=False
                if event.key == pygame.K_SPACE:
                    stop = True
            while stop:
                    screen.fill((165, 206, 216))
                    create_map(1)
                    mil = clock.tick(FPS)
                    snake.draw()
                    snake2.draw()
                    food.draw()
                    show_score(35, 45, snake.score,RED)
                    show_score(435, 45, snake2.score,YELLOW)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            stop=False
                            go = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                stop = False
        pygame.display.flip()
    go=True

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
        screen.fill((255,255,255))

        mx,my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(150,200,400,50)
        button_2 = pygame.Rect(150,300,400,50)
        pygame.draw.rect(screen,(192,192,192),button_1)
        pygame.draw.rect(screen,(192,192,192),button_2)
        draw_text('New Game',font1,(0,0,0),screen,150,200)
        draw_text('Saved Game',font1,(0,0,0),screen,150,300)
        draw_text('Snake Game',pygame.font.SysFont('ARIAL',75),(0,0,0),screen,150,50)

        if button_1.collidepoint((mx,my)):
            draw_text('New Game',font1,(255,255,255),screen,150,200)
            if click :
                single()
        if button_2.collidepoint((mx,my)):
            draw_text('Saved Game',font1,(255,255,255),screen,150,300)
            if click:
               saved_game()

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