import pygame
pygame.display.set_caption("Music")
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False

li = ["1mp.mp3", "2mp.mp3", "3mp.mp3"]
i = 0
pygame.mixer.music.load(li[i])
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)

while not done:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            done = True
    if key[pygame.K_d]:
        i += 1
        pygame.mixer.music.load(li[i % 3])
        pygame.mixer.music.play()
    if key[pygame.K_a]:
        i -= 1
        pygame.mixer.music.load(li[i % 3])
        pygame.mixer.music.play()
    if key[pygame.K_s]:
        pygame.mixer.music.pause()
    if key[pygame.K_w]:
        pygame.mixer.music.unpause()
    pygame.display.flip()
    clock.tick(60)