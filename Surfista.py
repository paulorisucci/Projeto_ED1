class Surfista:
  def __init__(self, nome, titulos, idade, cpf):
    self._nome = nome
    self._titulos = titulos
    self._idade = idade
    self._cpf = cpf
    self._prox = None
  
  @property
  def nome(self):
    return self._nome
  @nome.setter
  def nome(self, novo):
    self._nome = novo

  @property
  def titulos(self):
    return self._titulos
  @titulos.setter
  def titulos(self, novo):
    self._titulos = novo

  @property
  def idade(self):
    return self._idade
  @idade.setter
  def idade(self, novo):
    self._idade = novo

  @property
  def cpf(self):
    return self._cpf
  @cpf.setter
  def cpf(self, novo):
    self._cpf = novo

  @property
  def prox(self):
    return self._prox
  @prox.setter
  def prox(self, novo):
    self._prox = novo

  def incrementa_titulo(self):
    self._titulos +=1

  def __str__(self):
    return 'Nome: {}, Quant. de Títulos: {}, Idade: {} Anos, CPF: {}'.format(self._nome,self._titulos, self._idade, self._cpf)