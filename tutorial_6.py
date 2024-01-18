import pygame
from random import randint

#score
def score():
    global enemy_rect_list
    score = 0

    for enemy in enemy_rect_list:
        if enemy.right < 0:
            score += 1

    font = pygame.font.SysFont("comicsans",30,True)
    font = font.render(f"SCORE: {score}",True,"black")
    font_rect = font.get_rect(center = (400,70))
    screen.blit(font,font_rect)
    return

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
game_active = False
myscore = 0
music = pygame.mixer.Sound("music.mp3")
music.play(loops = -1)

#variable definition
player_gravity = -22
backgroud_surf = pygame.image.load("back.png").convert()

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

        if game_active:
            if event.type == enemy_event:
                enemy_rect_list.append(goblin_surf.get_rect(midbottom = (randint(780,1000),385)))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and player_rect.bottom == 380:
                player_gravity = -22
                
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] or event.type == pygame.MOUSEBUTTONDOWN:
                game_active = True
                enemy_rect_list = [enemy for enemy in enemy_rect_list if enemy.x == -100]

    if game_active:
        draw_func()
        myscore = score()
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
        screen.fill((0,100,200))
        myscore = score()

        player_font = pygame.font.SysFont("comicsans",40,True)
        player_font = player_font.render("Runner Man",True,"yellow")
        player_font_rect = player_font.get_rect(center = (400,30))
        screen.blit(player_font,player_font_rect)

        player_image = pygame.image.load("standing.png").convert_alpha()
        player_image = pygame.transform.rotozoom(player_image,0,3)
        player_image_rect = player_image.get_rect(center = (400,200))
        screen.blit(player_image,player_image_rect)

        mot_font = pygame.font.SysFont("comicsans",30,True,True)
        mot_font = mot_font.render("Run as fast as your legs can carry you",True,"yellow")
        mot_font_rect = mot_font.get_rect(midbottom = (400,400))
        screen.blit(mot_font,mot_font_rect)

    pygame.display.update()
pygame.quit()
