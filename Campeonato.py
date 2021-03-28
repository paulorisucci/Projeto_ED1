from Pilha import Pilha
from Fila import Fila
from Lista import Lista
from Surfista import Surfista


class CampeonatoException(Exception):
  def __init__(self, mensagem):
    super().__init__(mensagem)

class Campeonato:
  def __init__(self, nome_do_campeonato):
    self._nome_do_campeonato = nome_do_campeonato
    self._surfistasP = Pilha()
    self._surfistasF = Fila()
    self._surfistasL = Lista()


  @property
  def nome(self):
   return self._nome_do_campeonato
  @nome.setter
  def nome(self, novo_nome):
    self._nome_do_campeonato = novo_nome

  @property
  def surfistasL(self):
    return self._surfistasL
  @surfistasL.setter
  def surfistasL(self, novo):
    self._surfistasL = novo

  @property
  def surfistasP(self):
    return self._surfistasP
  @surfistasP.setter
  def surfistasP(self, novo):
    self._surfistasP = novo

  @property
  def surfistasF(self):
    return self._surfistasF
  @surfistasF.setter
  def surfistasF(self, novo):
    self._surfistasF = novo


  def menor_idade(self):

    if(self._surfistasL.Tamanho() == 0):
      raise CampeonatoException('Não há surfistas na lista do campeonato.')

    aux = self._surfistasL.Inicio
    nome = aux.nome
    menor = aux.idade

    while(aux != None):
      if aux.idade < menor:
        menor = aux.idade
        nome = aux.nome
      aux = aux.prox

    return nome


  def maior_idade(self):
    
    if(self._surfistasL.Tamanho() == 0):
      raise CampeonatoException('Não há surfistas na lista do campeonato.')

    aux = self._surfistasL.Inicio
    maior = aux.idade
    nome = aux.nome

    while(aux != None):
      if aux.idade > maior:
        maior = aux.idade
        nome = aux.nome
      aux = aux.prox

    return nome


  def incrementa_titulo_surfista(self, cpf):

    if(self._surfistasL.Tamanho() == 0):
      raise CampeonatoException('Não há surfistas na lista do campeonato.')

    surfista = self._surfistasL.Buscar(cpf)
    surfista.incrementa_titulo()


  def adicionar_surfistas_P(self, novo_surfista):
    self._surfistasP.Adicionar(novo_surfista)

  def remover_surfista_P(self):
    self._surfistasP.Remover()

  def mostrar_tam_surfistasP(self):
    return self._surfistasP.Tamanho()

  def busca_surfista_P(self):
    return self.surfistasP.MostrarElemento()


  def adicionar_surfistas_F(self, novo_surfista):
    self._surfistasF.Adicionar(novo_surfista)

  def remover_surfista_F(self):
    self._surfistasF.Remover()

  def mostrar_tam_surfistasF(self):
    return self.surfistasF.Tamanho()

  def busca_surfista_F(self):
    return self.surfistasF.MostrarElemento()


  def adicionar_surfistas_L(self, novo_surfista, posicao=-1):
    self._surfistasL.Adicionar(novo_surfista, posicao)

  def remover_surfista_L(self, posicao):
    self._surfistasL.Remover(posicao)

  def mostrar_tam_surfistasL(self):
    return self._surfistasL.Tamanho()


  def mostrar_tam_total(self):
    return self.mostrar_tam_surfistasL() + self.mostrar_tam_surfistasF() + self.mostrar_tam_surfistasP()


  def busca_surfista(self, cpf):
    return self._surfistasL.Buscar(cpf)


  def ordena_surfistas(self):
    self._surfistasL.Ordenar()


  def imprimir_surfistas(self): #imprimir_surfistas() - imprime na tela os surfistas em surfistasL: “nome –titulos”;
    return self._surfistasL.Imprimir()


  def __str__(self):
    return f'Nome do Campeonato: {self._nome_do_campeonato}'