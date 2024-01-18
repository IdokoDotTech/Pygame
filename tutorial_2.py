import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,450))
pygame.display.set_caption("Runner Man")
font = pygame.font.SysFont("comicsans",30,True)

#variable definition
backgroud_surf = pygame.image.load("back.png")
font = font.render("SCORE",True,"black")
goblin_surf = pygame.image.load("L2E.png")
gob_width = 700


#draw funtion
def draw_func():
    screen.blit(backgroud_surf,(0,0))
    screen.blit(font,(350,50))
    screen.blit(goblin_surf, (gob_width,320))

#while loop
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_func()
    gob_width -= 5
    if gob_width < -100:
        gob_width = 700
    pygame.display.update()

pygame.quit()
