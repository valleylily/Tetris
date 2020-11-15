import pygame as pg
from copy import deepcopy
import Campo as cp
import _thread as tr
import Figura as fg

pg.init()

tamanhoHorizontal = 400
tamanhoVertical = tamanhoHorizontal * 3

janela = pg.display.set_mode((tamanhoHorizontal, tamanhoVertical))

clock = pg.time.Clock()

tempo = 5000
tempoTela = 60

programaEncerrado = False

campo = cp.Campo(int(tamanhoHorizontal/20), int(tamanhoVertical/20))

ultimaPosicao = fg.Figura([[0,0]], 0)

def atualizarTela(ultimaPosicao, tempoTela):
    janela.fill((0, 0, 0))
    for bloco in ultimaPosicao.getBlocos():
        posicao = ultimaPosicao.getPosicao()
        pg.draw.rect(janela, ultimaPosicao.getCor(), pg.Rect(bloco[0]+posicao[0]+10, bloco[1]+posicao[1]+10, 20, 20))

    for bloco in campo._figuraAtual.getBlocos():
        posicao = campo._figuraAtual.getPosicao()
        pg.draw.rect(janela, campo._figuraAtual.getCor(), pg.Rect(bloco[0]+posicao[0]+10, bloco[1]+posicao[1]+10, 20, 20))

    pg.display.flip()
    clock.tick(tempoTela)

def descer(ultimaPosicao, tempo):
    ultimaPosicao = deepcopy(campo._figuraAtual)
    if(campo.executarRodada()):
        atualizarOcupados()
    clock.tick(tempo)
    tempo -= 5

def atualizarOcupados():
    for bloco in campo._ocupados:
        pg.draw.rect(janela, campo._figuraAtual.getCor(), pg.Rect(bloco[0]+10, bloco[1]+10, 20, 20))

tr.start_new_thread(descer, (ultimaPosicao, tempo))
tr.start_new_thread(atualizarTela, (ultimaPosicao, tempoTela))

while not programaEncerrado:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            programaEncerrado = True
    
    teclaPressionada = pg.key.get_pressed()
    if teclaPressionada[pg.K_UP]:
        campo.girarAtual()
    if teclaPressionada[pg.K_DOWN]:
        campo.moverAtual([0,1])
    if teclaPressionada[pg.K_LEFT]:
        campo.moverAtual([1,0])
    if teclaPressionada[pg.K_RIGHT]:
        campo.moverAtual([0,-1])