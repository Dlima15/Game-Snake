import random
import pygame

pygame.init()
pygame.display.set_caption("Jogo da Cobrinha")
largura, altura = 600, 400
pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

#cores dos elementos, cobrinha, comida e fundo

preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

#medidas da cobrinha

tamanho_quadrado = 10
velocidade = 15 

#inicio do código do jogo

def jogar_jogo():
    fim_do_jogo = False


    while not fim_do_jogo:
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_do_jogo = True


















jogar_jogo()