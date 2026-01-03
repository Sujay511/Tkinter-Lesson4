import pygame
pygame.init()

screen=pygame.display.set_mode((500,500))

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    

    pygame.draw.rect(screen,"#ff0000",pygame.Rect(70,70,50,50),0)
    pygame.draw.line(screen,"#d0efff",(100,5),(400,5),10)
    pygame.draw.circle(screen,"#fdf500",(200,300),60,0)


    pygame.display.update()

pygame.quit()