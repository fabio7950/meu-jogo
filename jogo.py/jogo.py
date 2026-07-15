import sys
import pygame
import random

pygame.init()

TAMANHO_BLOCO = 20
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Cobrinha - Começo Lento")

COR_FUNDO = (30, 30, 30)       
COR_COBRA = (51, 204, 51)      
COR_COMIDA = (255, 51, 51)     

clock = pygame.time.Clock()

cobra = [
    pygame.Rect(400, 300, TAMANHO_BLOCO, TAMANHO_BLOCO),
    pygame.Rect(380, 300, TAMANHO_BLOCO, TAMANHO_BLOCO),
    pygame.Rect(360, 300, TAMANHO_BLOCO, TAMANHO_BLOCO)
]

direcao_x = 0
direcao_y = 0
jogo_iniciado = False

def gerar_comida():
    x = random.randint(0, (LARGURA - TAMANHO_BLOCO) // TAMANHO_BLOCO) * TAMANHO_BLOCO
    y = random.randint(0, (ALTURA - TAMANHO_BLOCO) // TAMANHO_BLOCO) * TAMANHO_BLOCO
    return pygame.Rect(x, y, TAMANHO_BLOCO, TAMANHO_BLOCO)

comida = gerar_comida()
pontos = 0
velocidade_atual = 5  

running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT and direcao_x == 0:
                direcao_x = -TAMANHO_BLOCO
                direcao_y = 0
                jogo_iniciado = True
            elif evento.key == pygame.K_RIGHT and direcao_x == 0:
                direcao_x = TAMANHO_BLOCO
                direcao_y = 0
                jogo_iniciado = True
            elif evento.key == pygame.K_UP and direcao_y == 0:
                direcao_x = 0
                direcao_y = -TAMANHO_BLOCO
                jogo_iniciado = True
            elif evento.key == pygame.K_DOWN and direcao_y == 0:
                direcao_x = 0
                direcao_y = TAMANHO_BLOCO
                jogo_iniciado = True

    if jogo_iniciado:
        nova_cabeca = pygame.Rect(cobra[0].x + direcao_x, cobra[0].y + direcao_y, TAMANHO_BLOCO, TAMANHO_BLOCO)
        
        if nova_cabeca.left < 0:
            nova_cabeca.x = LARGURA - TAMANHO_BLOCO
        elif nova_cabeca.right > LARGURA:
            nova_cabeca.x = 0
        elif nova_cabeca.top < 0:
            nova_cabeca.y = ALTURA - TAMANHO_BLOCO
        elif nova_cabeca.bottom > ALTURA:
            nova_cabeca.y = 0

        cobra.insert(0, nova_cabeca)

        if cobra[0].colliderect(comida):
            pontos += 1
            if pontos % 2 == 0 and velocidade_atual < 15:
                velocidade_atual += 1
            pygame.display.set_caption(f"Jogo da Cobrinha | Pontos: {pontos} | Velocidade: {velocidade_atual}")
            comida = gerar_comida()
        else:
            cobra.pop()

        for parte in cobra[3:]:
            if cobra[0].colliderect(parte):
                running = False

    tela.fill(COR_FUNDO)
    pygame.draw.rect(tela, COR_COMIDA, comida)
    for parte in cobra:
        pygame.draw.rect(tela, COR_COBRA, parte)

    pygame.display.flip()
    clock.tick(velocidade_atual)

pygame.quit()
sys.exit()
