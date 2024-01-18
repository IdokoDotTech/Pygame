import pygame
from random import randint

#collision
def collision(enemy,player):
    if enemy:
        for enemy_rect in enemy:
            if enemy_rect.colliderect(player):
                return False
    return True
            

#enemy spawn
def enemy_spawn(enemy_list):
    if enemy_list:
        for enemy_rect in enemy_list:
            enemy_rect.x -= 5

            screen.blit(goblin_surf,enemy_rect)

        enemy_list = [enemy for enemy in enemy_list if enemy.x > -100]

        return enemy_list
    else: return []

#goblin animation
def goblin_animation():
    global goblin_surf, goblin_index

    goblin_index += 0.1
    if goblin_index >= len(goblin_list): goblin_index = 0
    goblin_surf = goblin_list[int(goblin_index)]

#player animation
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
game_active = True

#variable definition
player_gravity = -22
backgroud_surf = pygame.image.load("back.png").convert()
font = font.render("SCORE",True,"black")

goblin_1 = pygame.image.load("L2E.png").convert_alpha()
goblin_2 = pygame.image.load("L1E.png").convert_alpha()
goblin_list = [goblin_1,goblin_2]
goblin_index = 0
goblin_surf = goblin_list[goblin_index]
#goblin_rect = goblin_surf.get_rect(midbottom = (780,385))

enemy_rect_list = []

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
    #screen.blit(goblin_surf, goblin_rect)
    screen.blit(player_surf,player_rect)

#timer
enemy_event = pygame.USEREVENT +1
pygame.time.set_timer(enemy_event,1300)    

#while loop
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == enemy_event:
            enemy_rect_list.append(goblin_surf.get_rect(midbottom = (randint(780,1000),385)))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and player_rect.bottom == 380:
        player_gravity = -22

    if game_active:
        draw_func()
        player_rect.bottom += player_gravity
        player_gravity += 1
        if player_rect.bottom > 380:
            player_rect.bottom = 380
        
        #goblin_rect.left -= 5
        #if goblin_rect.left < -100:
        #   goblin_rect.left = 700
        player_animation()
        enemy_rect_list = enemy_spawn(enemy_rect_list)
        goblin_animation()
        game_active = collision(enemy_rect_list,player_rect)
    else:
        screen.fill("blue")

    pygame.display.update()
pygame.quit()
