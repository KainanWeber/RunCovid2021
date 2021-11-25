import pygame
import time
import random
pygame.init()
largura = 1400
altura = 950
configTela = (largura, altura)
gameDisplay = pygame.display.set_mode(configTela)
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
pygame.display.set_caption("Run Covid - Kainan Weber")
icone = pygame.image.load("assets/Sombra.png")
pygame.display.set_icon(icone)
pessoa1 = pygame.image.load("assets/Jubileu.png")
pessoa = 230
corona = pygame.image.load("assets/corona.png")
def mostraPessoa(x, y):
    gameDisplay.blit(pessoa1, (x, y))
def mostraCorona(x, y):
    gameDisplay.blit(corona, (x, y))
def text_objects(texto, font):
    textSurface = font.render(texto, True, black)
    return textSurface, textSurface.get_rect()
def escreverTela(texto):
    fonte = pygame.font.Font("freesansbold.ttf", 100)
    TextSurf, TextRect = text_objects(texto, fonte)
    TextRect.center = ((largura/2, altura/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(5)
    game()
def escreverPlacar(contador):
    fonte = pygame.font.SysFont(None, 30)
    texto = fonte.render("Dias em quarentena:"+str(contador), True, black)
    gameDisplay.blit(texto, (9, 9))
def dead():
    escreverTela("Foi só uma gripe!")
def game():
    pessoaPosicaoX = largura*0.45
    pessoaPosicaoY = altura*0.72
    movimentoX = 0
    velocidade = 20
    coronaAltura = 109.5
    coronaLargura = 109.5
    coronaVelocidade = 3
    coronaX = random.randrange(0, largura)
    coronaY = -200
    desvios = 0
    while True:
        acoes = pygame.event.get()  
        for acao in acoes:
            if acao.type == pygame.QUIT:
                pygame.quit()
                quit()
            if acao.type == pygame.KEYDOWN:
                if acao.key == pygame.K_LEFT:
                    movimentoX = velocidade*-1
                elif acao.key == pygame.K_RIGHT:
                    movimentoX = velocidade
            if acao.type == pygame.KEYUP:
                movimentoX = 0
        gameDisplay.fill(white)
        escreverPlacar(desvios)
        coronaY = coronaY + coronaVelocidade
        mostraCorona(coronaX, coronaY)
        if coronaY > altura:
            coronaY = -200
            coronaX = random.randrange(0, largura)
            desvios = desvios+1
            coronaVelocidade += 3
        pessoaPosicaoX += movimentoX
        if pessoaPosicaoX < 0:
            pessoaPosicaoX = 0
        elif pessoaPosicaoX > largura - pessoa:
            pessoaPosicaoX = largura - pessoa
        if pessoaPosicaoY < coronaY + coronaAltura:
            if pessoaPosicaoX < coronaX and pessoaPosicaoX+pessoa > coronaX or coronaX+coronaLargura > pessoaPosicaoX and coronaX+coronaLargura < pessoaPosicaoX+pessoa:
                dead()
        mostraPessoa(pessoaPosicaoX, pessoaPosicaoY)
        pygame.display.update()
        clock.tick(60)  
game()
