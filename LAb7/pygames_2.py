import pygame 
pygame.init()
screen = pygame.display.set_mode((1920, 1000))
done  = True
image = pygame.image.load("mickeyclock.jpeg")
angle = 180

while done:
    image = pygame.image.load("mickeyclock.jpeg")
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    rotate = pygame.transform.rotate(image, angle)
    screen.blit(rotate, (0, 0))
    pygame.display.flip()