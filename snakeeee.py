import random
import pygame
import sys

pygame.init()
pygame.display.set_caption("Jogo da Cobrinha")
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

# cores dos elementos, cobrinha, comida e fundo
preta = (0, 0, 0)
verde = (0, 255, 0)

# medidas da cobrinha
tamanho_quadrado = 10
velocidade = 15 

# início do código do jogo
def jogar_jogo():
    fim_do_jogo = False

    while not fim_do_jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_do_jogo = True

        # preenche a tela com a cor de fundo
        tela.fill(preta)

        # desenha a cobrinha na tela
        # aqui você pode adicionar mais lógica para desenhar outros elementos do jogo

        # atualiza a tela
        pygame.display.update()

        # define a taxa de atualização
        relogio.tick(velocidade)

# chama a função para iniciar o jogo
jogar_jogo()

# fecha o programa corretamente
pygame.quit()
sys.exit()
