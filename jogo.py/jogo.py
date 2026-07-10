import pygame
import sys

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Meu Primeiro Jogo")

quadrado_x = 350
quadrado_y = 250
velocidade = 7

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:  
        quadrado_x -= velocidade
    if teclas[pygame.K_RIGHT]: 
        quadrado_x += velocidade
    if teclas[pygame.K_UP]:    
        quadrado_y -= velocidade
    if teclas[pygame.K_DOWN]:  
        quadrado_y += velocidade

    tela.fill((0, 102, 204))
    pygame.draw.rect(tela, (255, 51, 51), (quadrado_x, quadrado_y, 100, 100))
    pygame.display.update()
    pygame.time.Clock().tick(60)
