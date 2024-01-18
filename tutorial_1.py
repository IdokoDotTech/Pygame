import pygame

pygame.init()

screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Runner Man")
x = 60
y = 0
weidth = 40
height = 40
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(screen, "red",(x,y,weidth,height))
    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_DOWN]:
        y += 5
    if keys[pygame.K_UP]:
        y -= 5

    screen.fill("black")

pygame.quit()