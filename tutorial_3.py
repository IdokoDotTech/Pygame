import pygame

def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 380:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_list): player_index = 0
        player_surf = player_list[int(player_index)]

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,450))
pygame.display.set_caption("Runner Man")
font = pygame.font.SysFont("comicsans",30,True)

#variable definition
player_gravity = -22
backgroud_surf = pygame.image.load("back.png").convert()
font = font.render("SCORE",True,"black")
goblin_surf = pygame.image.load("L2E.png").convert_alpha()
goblin_rect = goblin_surf.get_rect(midbottom = (780,385))
player_1 = pygame.image.load("R2.png").convert_alpha()
player_2 = pygame.image.load("R1.png").convert_alpha()
player_jump = pygame.image.load("standing.png").convert_alpha()
player_list = [player_1,player_2]
player_index = 0
player_surf = player_list[player_index]

player_rect = player_surf.get_rect(midbottom = (20,380))


#draw funtion
def draw_func():
    screen.blit(backgroud_surf,(0,0))
    screen.blit(font,(350,50))
    screen.blit(goblin_surf, goblin_rect)
    screen.blit(player_surf,player_rect)
   

#while loop
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and player_rect.bottom == 380:
        player_gravity = -22

    draw_func()
    player_rect.bottom += player_gravity
    player_gravity += 1
    if player_rect.bottom > 380:
        player_rect.bottom = 380
    
    goblin_rect.left -= 5
    if goblin_rect.left < -100:
        goblin_rect.left = 700
    player_animation()
    pygame.display.update()

pygame.quit()
