from Surfista import Surfista

class PilhaException(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)

class Pilha:
    def __init__(self):
        self._topo = None
        self._tamanho = 0

    @property
    def Topo(self):
        assert self._tamanho > 0, 'A pilha está vazia.'
        return self._topo

    def Vazio(self):
        return self._tamanho == 0
    
    def Tamanho(self):
        return self._tamanho


    def Adicionar(self, novo_d):
        no = novo_d
        no.prox = self._topo
        self._topo = no
        self._tamanho += 1


    def Remover(self):
        if self.Vazio(): #Verificar se está vazia 
            raise PilhaException('Pilha vazia')

        self._topo = self._topo.prox
        self._tamanho -= 1


    def MostrarElemento(self):
        assert self._tamanho > 0, 'A pilha está vazia'
        return f'Surfista: {self.Topo}'


    def __str__(self):
        assert self._tamanho > 0, 'A pilha está vazia'

        string = ''
        aux = self._topo
        while(aux != None):
            string += f' {aux.__str__()}\n'
            aux = aux.prox

        return string


    def Imprimir(self):
        print(self.__str__())