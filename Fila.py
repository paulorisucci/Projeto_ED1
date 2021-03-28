from Surfista import Surfista

class FilaException(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)

class Fila:
    def __init__(self):
        self._inicio = None
        self._tamanho = 0

    @property
    def Inicio(self):
        assert self._inicio != None, 'Lista está vazia.'
        return self._inicio


    def MostrarElemento(self):
        return f'Surfista: {self.Inicio}'

    def Tamanho(self):
        return self._tamanho

    def Vazia(self):
        return self._tamanho == 0

    def Adicionar(self, novo_elemento):
        aux = self._inicio

        if(aux != None):
            while(aux.prox != None):
                aux = aux.prox
            aux.prox = novo_elemento

        else:
            self._inicio = novo_elemento
        self._tamanho += 1


    def Remover(self):

        if self.Vazia(): #Verificar se está vazia
            raise FilaException('Lista vazia')

        self._inicio = self._inicio.prox
        self._tamanho -= 1


    def __str__(self):
        string = ''
        aux = self._inicio
        while(aux != None):
            string += f' {aux.__str__()}\n'
            aux = aux.prox

        return string


    def Imprimir(self):
        print(self.__str__())