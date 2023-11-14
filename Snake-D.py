import random
import pygame
import sys

pygame.init()
pygame.display.set_caption("Jogo da Cobrinha")
largura, altura = 1000, 600
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

#cores dos elementos, cobrinha, comida e fundo

preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

#medidas da cobrinha

tamanho_quadrado = 15
velocidade_de_atualização = 15 

def gerar_comida():
    return comida_x, comida_y


#inicio do código do jogo

def jogar_jogo():
    fim_do_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0 
    velocidade_y = 0

    tamanho_cobra = 1 
    pixels = []

    comida_x, comida_y = gerar_comida


    while not fim_do_jogo:
        tela.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_do_jogo = True  



















jogar_jogo()