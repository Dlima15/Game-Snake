import random
import pygame
import sys

pygame.init()

#Parte do jogo feira pelo VINI ( INCOMPLETO )

# Configurações da tela
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")
relogio = pygame.time.Clock()

# Cores
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

# Medidas da cobrinha
tamanho_quadrado = 10
velocidade = 15

# Posição inicial da cobrinha
x_cobra, y_cobra = largura / 2, altura / 2

# Velocidade inicial da cobrinha
velocidade_x = 10
velocidade_y = 0

# Função para desenhar a cobrinha
def desenhar_cobra(x, y):
    pygame.draw.rect(tela, verde, [x, y, tamanho_quadrado, tamanho_quadrado])

# Início do código do jogo
def jogar_jogo():
    fim_do_jogo = False

    while not fim_do_jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_do_jogo = True
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    velocidade_x = -tamanho_quadrado
                    velocidade_y = 0
                elif evento.key == pygame.K_RIGHT:
                    velocidade_x = tamanho_quadrado
                    velocidade_y = 0
                elif evento.key == pygame.K_UP:
                    velocidade_x = 0
                    velocidade_y = -tamanho_quadrado
                elif evento.key == pygame.K_DOWN:
                    velocidade_x = 0
                    velocidade_y = tamanho_quadrado

        # Atualiza a posição da cobrinha
        x_cobra += velocidade_x
        y_cobra += velocidade_y

        # Preenche a tela com a cor de fundo
        tela.fill(preta)

        # Desenha a cobrinha na tela
        desenhar_cobra(x_cobra, y_cobra)

        # Atualiza a tela
        pygame.display.update()

        # Define a taxa de atualização
        relogio.tick(velocidade)

# Chama a função para iniciar o jogo
jogar_jogo()
