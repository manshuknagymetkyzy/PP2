import pygame
from math import cos, sin, pi

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

size = (1000, 600)

screen = pygame.display.set_mode(size)
font = pygame.font.SysFont('times-new-roman', 20 , False, True)

nums = ['1.00', '0.75' , '0.50', '0.25', '0.00', '-0.25', '-0.50', '-0.75', '-1.00']
degrees =  ['-3п', ' 5п', '-2п', ' 3п', '-п ', ' п ', ' 0 ', ' п ', ' п ', ' 3п', ' 2п', ' 5п', ' 3п']
lines = ['', '_ __', '', '_ __', '', '  __', '', '  __', '', '  ___', '', '  ___', '']
divby2 = ['', '2','','2','','2','','2','','2','','2','']

surface = pygame.Surface(size)
clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK,(58, 10, 884, 522), 3)

    for y in range(0, 522, 58):
        pygame.draw.line(screen, BLACK, [58, 39 + y], [942,39 + y], 1)
    for y in range(0, 884, 136):
        pygame.draw.line(screen, BLACK, [90 + y, 10], [90 + y, 532], 1)
    
    pygame.draw.line(screen, BLACK, [58, 271], [942, 271], 3)   
    pygame.draw.line(screen, BLACK, [500, 10], [500, 532], 3)   
    
    for y in range(0, 464, 58):
        pygame.draw.line(screen, BLACK, [58,68+y], [74, 68+y], 1) 
    for y in range(0, 816, 136):
        pygame.draw.line(screen, BLACK, [158+y,10], [158+y, 24], 1)
    for y in range(0, 816, 136):
        pygame.draw.line(screen, BLACK, [158+y,518], [158+y, 532], 1)
    for y in range(0, 464, 58):
        pygame.draw.line(screen, BLACK, [926,68+y], [942, 68+y], 1) 

        cnt = 0
    for i in range(19, 291, 58):                      
        text = font.render(nums[cnt], True, BLACK)
        screen.blit(text, (15, i))
        cnt += 1
    cnt1 = 5
    for i in range(309, 503, 58):                     
        text = font.render(nums[cnt1], True, BLACK)
        screen.blit(text, (8, i))
        cnt1 += 1    

    cnt2 = 0
    for i in range(80,902,68):
        text = font.render(degrees[cnt2], True, BLACK)
        screen.blit(text, (i, 535))
        cnt2 += 1    
    cnt3 = 0
    for i in range(70,892,68):
        text = font.render(lines[cnt3], True, BLACK)
        screen.blit(text, (i, 535))
        cnt3 += 1
         
    cnt4 = 0
    for i in range(80,902,68):
        text = font.render(divby2[cnt4], True, BLACK)
        screen.blit(text, (i+7, 555))
        cnt4 += 1    
 
    for i in range(90, 905):
        y1 = 232 * sin((i - 90) / 135 * pi)
        y2 = 232* sin((i - 89) / 135 * pi)
        pygame.draw.aalines(screen, RED, True, [(i, 271 + y1), ((i + 1), 271 + y2)])
    for i in range(90, 905 , 3):
        y1 = 232 * cos((i - 90) / 135 * pi)
        y2 = 232* cos((i - 89) / 135 * pi)
        pygame.draw.aalines(screen, BLUE, True, [(i, 271 + y1), ((i + 1), 271 + y2)])            

    pygame.draw.line(screen, RED, (700, 60), (730, 60))
    for x in range(700, 730, 7):
        pygame.draw.line(screen, BLUE, (x, 80), (x + 3, 80))
    
    text = font.render('sin x', True, BLACK)
    screen.blit(text,(650,50)) 
    text1 = font.render('cos x', True, BLACK)
    screen.blit(text1,(650,70))    
    
    pygame.display.flip()


pygame.quit()