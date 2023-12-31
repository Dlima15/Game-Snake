import os
import random
import pygame
import sys

#Parte do jogo feira pelo DANILO ( 100% e perfeito)

pygame.init()
pygame.display.set_caption("Jogo da Cobrinha")
largura, altura = 1000, 600
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

# cores dos elementos, cobrinha, comida e fundo
preta = (0, 0, 0)
verde = (0, 255, 0)
branca = (255, 255, 255)
Azul = (0, 0, 255)

# medidas da cobrinha
tamanho_quadrado = 15
velocidade_de_atualizacao = 15

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 15.0) * 15.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 15.0) * 15.0
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Arial", 25)
    texto = fonte.render(f"Pontos: {pontuacao}", True, Azul)
    tela.blit(texto, [1, 1])

def mostrar_mensagem_final(pontuacao):
    print("Como quer salvar seu nome Campeão?")
    nome = input()
    salvar_pontuacao(nome, pontuacao)
    print("Pontuação salva com sucesso!")

def salvar_pontuacao(nome, pontuacao):
    arquivo_path = os.path.join(os.path.dirname(__file__), "pontuacoes.txt")
    with open(arquivo_path, "a") as arquivo:
        arquivo.write(f"{nome}: {pontuacao}\n")

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

# início do código do jogo
def jogar_jogo():
    fim_do_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_comida()

    while not fim_do_jogo:
        tela.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_do_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        # desenho da comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        # atualização da posição da cobra
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_do_jogo = True

        x += velocidade_x
        y += velocidade_y

        # desenho da cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        # regra da cobrinha bater no próprio corpo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_do_jogo = True

        desenhar_cobra(tamanho_quadrado, pixels)

        desenhar_pontuacao(tamanho_cobra - 1)

        # atualização da tela
        pygame.display.update()

        # criação da nova comida após a cobrinha já ter papado
        if comida_x - tamanho_quadrado < x < comida_x + tamanho_quadrado and comida_y - tamanho_quadrado < y < comida_y + tamanho_quadrado:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()

        # controle de velocidade
        relogio.tick(velocidade_de_atualizacao)

    # mostrar mensagem final e salvar pontuação
    mostrar_mensagem_final(tamanho_cobra - 1)

# chama a função para iniciar o jogo
jogar_jogo()

# fecha o programa corretamente
pygame.quit()
sys.exit()
