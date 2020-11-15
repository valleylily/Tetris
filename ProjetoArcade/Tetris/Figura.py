from copy import deepcopy
import Uteis as u

class Figura(object):
    _coresPossiveis = ((0,0,255), (0,255,0), (255,0,0), (255,0,255), (255,255,0), (255,127,0))

    def __init__(self, blocos, numeroDaCor, posicaoInicial = [0,0]):
        self.setBlocos(blocos)
        self.setCor(numeroDaCor)
        self.setPosicao(posicaoInicial)
    

    def setBlocos(self, posicoes):
        quantosBlocos = len(posicoes)
        if quantosBlocos == 0:
            Exception ('You cannot create an empty figure.')
        if quantosBlocos != 1:
            for bloco in posicoes:
                direcoes = [(bloco[0]+1, bloco[1]), (bloco[0], bloco[1]+1), (bloco[0]-1, bloco[1]), (bloco[0], bloco[1]-1)]
                if (len(u.intersecao(posicoes, direcoes)) != 0):
                    Exception('A figure cannot have blocks that are not directly conected.')
        
        self._blocos = posicoes

    def setCor(self, numeroDaCor):
        if numeroDaCor > 5:
            Exception('There are only six colour options!')
        self._cor = self._coresPossiveis[numeroDaCor]

    def setPosicao(self, posicao):
        if posicao[0] < 0 or posicao[1] < 0:
            Exception('A figure cannot be in a negative position.')
        self._posicao = [posicao[0], posicao[1]]

    def getBlocos(self):
        return self._blocos

    def getCor(self):
        return self._cor

    def getPosicao(self):
        return self._posicao

    def mover(self, deslocamento = (0, 1)):
        self.setPosicao([self._posicao[0]+deslocamento[0], self._posicao[1]+deslocamento[1]])

    def girar(self):
        for coordenada in self._blocos:
            multiplicacao = coordenada[0] * coordenada[1]
            if(multiplicacao > 0):
                coordenada[1] = -coordenada[1]
            else:
                if(multiplicacao < 0):
                    coordenada[0] = -coordenada[0]
                else:
                    if(coordenada[0] == 0):
                        coordenada[0] = coordenada[1]
                        coordenada[1] = 0
                    else:                            
                        coordenada[1] = -coordenada[0]
                        coordenada[0] = 0
    
    def deletarLinha(self, qualLinha):
        for coordenada in self._blocos:
            if(coordenada[1] == qualLinha):
                self._blocos.remove(coordenada)
        for coordenada in self._blocos:
            if(coordenada[1] < qualLinha):
                self._blocos.add([coordenada[0],coordenada[1]+1])
                self._blocos.remove(coordenada)

    def vazia(self):
        if(not self._blocos):
            return True
        else:
            return False
    
    def __eq__(self, other):
        return self._blocos == other._blocos and self._cor == other._cor

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other): 
        return len(self._blocos) < len(other._blocos)

    def __gt__(self, other): 
        return len(self._blocos) > len(other._blocos)

    def __str__(self):
        string  = "The figure is in the position: "+self._posicao+". \n"
        string += "Its format is defined by this coordenates: "+self._blocos+". \n" 
        string += "And its colour is "+self._cor+". \n\n"
        return string

    def __hash__(self):
        hashcode = 666
        hashcode += 13 * hash(str(self._blocos))
        hashcode += 13 * hash(self._cor)
        hashcode += 13 * hash(str(self._posicao))

        return hashcode
        
    def __copy__(self):
        return self

    def __deepcopy__(self, memo):
        blocos = deepcopy(self._blocos, memo)
        posicao = deepcopy(self._posicao, memo)
        return Figura(blocos, self._coresPossiveis.index(self._cor), posicao)