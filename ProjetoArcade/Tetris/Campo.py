import Figura as fg
import random
from copy import deepcopy
import Uteis as u

class Campo(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y
        blocos1 = [[-1,-1], [0,-1], [-1,0], [0,0]]
        blocos2 = [[0,1], [0,0], [0,-1], [1,-1]]
        blocos3 = [[-1,1], [-1,0], [0,0], [0,-1]]
        blocos4 = [[0,-1], [0,0], [0,1], [0,2]]
        blocos5 = [[-1,0], [0,0], [1,0], [0,1]]
        self._setFiguras([None for linha in range(int(y*x/4))])
        figura1 = fg.Figura(blocos1, 0, [2, y/2])
        figura2 = fg.Figura(blocos2, 0, [2, y/2])
        figura3 = fg.Figura(blocos3, 0, [2, y/2])
        figura4 = fg.Figura(blocos4, 0, [2, y/2])
        figura5 = fg.Figura(blocos5, 0, [2, y/2])

        self._ocupados = []

        self._desenhos = [figura1, figura2, figura3, figura4, figura5]
        self._figuraAtual = deepcopy(random.choice(self._desenhos))
    
    def _getFiguras(self):
        return self._figuras
    
    def _setFiguras(self, figuras):
        if(len(figuras) < 0):
            Exception("A field of figures cannot have no space")
        self._figuras = figuras

    def __novaFigura(self, figura = fg.Figura([[0,0]], 0)):
        if(figura == fg.Figura([[0,0]], 0)):
            figura = deepcopy(random.choice(self._desenhos))
        self._figuraAtual = figura

    def executarRodada(self):
        sobreposicoes = u.intersecao(self._ocupados, self.proxima())
        if(not sobreposicoes):
            self._figuraAtual.mover()
            return False
        else:
            linhasMudadas = []
            for posicao in self._figuraAtual.getBlocos():
                linha = posicao[1]+self._figuraAtual.getPosicao()[1]
                self._ocupados.append([posicao[0]+self._figuraAtual.getPosicao()[0], linha])
                linhasMudadas.append(linha)
            self._figuraAtual = deepcopy(random.choice(self._desenhos))
            quantosNaLinha = []
            for posicao in self._ocupados:
                linha = posicao[1]
                if(linha in linhasMudadas):
                    quantosNaLinha[linhasMudadas.index(linha)] += 1
            for quantos in quantosNaLinha:
                if (quantos >= self._y):
                    self.deletarLinha(linhasMudadas[quantosNaLinha.index(quantos)])
            return True

    def deletarLinha(self, qualLinha):
        for figura in self._getFiguras():
            acima = False
            naLinha = False
            for bloco in figura.getBlocos():
                if(bloco[1]+figura.getPosicao()[1] == qualLinha):
                    naLinha = True
                if(bloco[1]+figura.getPosicao()[1] < qualLinha):
                    acima = True
            if(naLinha):
                figura.deletarLinha()
            else:
                if(acima):
                    figura.mover()

    def moverAtual(self, deslocamento):
        self._figuraAtual.mover(deslocamento)

    def girarAtual(self):
        self._figuraAtual.girar()

    def proxima(self):
        proximo = []
        for bloco in self._figuraAtual.getBlocos():
            proximo.append([bloco[0], bloco[1]+1])
        return proximo


    def __eq__(self, other):
        return self._figuras == other._figuras

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other): 
        return len(self._figuras) < len(other._figuras)

    def __gt__(self, other): 
        return len(self._figuras) > len(other._figuras)

    def __str__(self):
        string = "The field has the figures: \n"+ self._figuras
        return string

    def __hash__(self):
        hashcode = 666
        hashcode += 13 * hash(str(self._figuras))

        return hashcode
        
    def __copy__(self):
        return self

    def __deepcopy__(self, memo):
        figuras = deepcopy(self._figuras, memo)
        campo = Campo(len(self._figuras[0]), len(self._figuras))
        campo._setFiguras(figuras)
        return campo