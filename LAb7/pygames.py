import pygame
pygame.display.set_caption("Ball")
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
x = 350
y = 300

while not done:
    screen.fill((0, 0, 0))
    key = pygame.key.get_pressed()
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            done = True
    if key[pygame.K_UP]: y -= 10
    elif key[pygame.K_DOWN]: y += 10
    elif key[pygame.K_RIGHT]: x += 10
    elif key[pygame.K_LEFT]: x -= 10
    if x > 775: x -= 10
    elif x < 25: x += 10
    if y > 575: y -= 10
    elif y < 25: y += 10
    pygame.draw.circle(screen, "RED", (x, y), 25)
    pygame.display.flip()
    clock.tick(60)