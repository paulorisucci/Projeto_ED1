from Surfista import Surfista


class ListaException(Exception):
  def __init__(self, mensagem):
    super().__init__(mensagem)

class Lista:
    def __init__(self):
        self._inicio = None
        self._tamanho = 0


    @property
    def Inicio(self):
        assert self._inicio != None, 'Lista está vazia.'
        return self._inicio

    def Tamanho(self):
        return self._tamanho

    def Vazia(self):
        return self._tamanho == 0


    def Adicionar(self, novo_dado, posicao = -1):
        if (posicao < 0):
            posicao += self._tamanho + 1

        if(posicao > self._tamanho or posicao < 0):
          raise ListaException('Posição Inválida.')


        if(posicao != 0):
            aux = self.BuscarPosicao(posicao-1)
            novo_dado.prox = aux.prox
            aux.prox = novo_dado

        else:
            aux = self._inicio
            aux = self._inicio
            novo_dado.prox = aux
            self._inicio = novo_dado

        self._tamanho +=1


    def Remover(self, posicao = -1):
        
        if(self._tamanho == 0):
          raise ListaException('A lista está vazia.')
        elif(posicao >= self._tamanho):
          raise ListaException('Posição Inválida')

        if(posicao != 0 and self._tamanho > 1):
            aux = self.BuscarPosicao(posicao-1)
            aux2 = self.BuscarPosicao(posicao)
            aux.prox = aux2.prox

        else:
            self._inicio = self._inicio.prox

        self._tamanho -= 1


    def BuscarPosicao(self, posicao):

        if (posicao < 0):
            posicao += self._tamanho

        if(self._tamanho == 0):
          raise ListaException('A lista está vazia.')
        if(posicao > self._tamanho):
          raise ListaException('Posição inválida.')

        aux = self._inicio
        aux_pos = 0

        if(posicao > 0) :
            while(aux_pos < posicao):
                aux = aux.prox
                aux_pos += 1

        return aux


    def Buscar(self, cpf):
        if(self._tamanho == 0):
          raise ListaException('A lista está vazia.')

        aux = self._inicio

        while(aux != None):
            if(aux.cpf == cpf):
                return aux
            aux = aux.prox
        else:
          raise ListaException('CPF inválido')


    def MostrarElemento(self, posicao):
        return f'Surfista: {self.BuscarPosicao(posicao)}'
    
    def Ordenar(self):

        if(self._tamanho == 0):
          raise ListaException('''A lista está vazia.''')
        
        assert self._tamanho > 1, '''A lista não precisa ser ordenada com 1 elemento.'''

        ordem = False
        while(not ordem):

            contador = 1
            incrementar_K = False
            k = self._inicio
            j = self._inicio
            i = self._inicio.prox
            while(i != None):

                if (i.nome.upper() < j.nome.upper()):
                    contador -= 1
                    if (j == self._inicio):
                        j.prox = i.prox
                        i.prox = j
                        self._inicio = i
                        j = self._inicio
                        k = self._inicio
                        i = self._inicio.prox
                    else:

                        j.prox = i.prox
                        i.prox = j
                        k.prox = i

                        j = i
                        i = i.prox

                contador += 1
                if(incrementar_K == True):
                    k = k.prox
                incrementar_K = True

                i = i.prox
                j = j.prox

            if(contador == self._tamanho):
                ordem = True
    
    def __str__(self):
        string = ''
        aux = self._inicio
        while(aux != None):
            string += f' {aux.nome} - {aux.titulos}\n'
            aux = aux.prox
        return string
    
    def Imprimir(self):
        print(self.__str__())