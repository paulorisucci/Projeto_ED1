from Fila import *
from Lista import *
from Pilha import *
from Surfista import *
from Campeonato import *


s1 = Surfista('Paulo Lindo', 3, 20, '1')
s2 = Surfista('Thiago Perfeito', 10, 40, '3')
s3 = Surfista('Pedro Maravilhoso', 3, 19,'2')
s4 = Surfista('Goku', 9, 50, '4')
s5 = Surfista('Vegeta', 9, 55, '5')
s6 = Surfista('Bills', 13, 10000, '6')

c1 = Campeonato('THE GREAT CHAMPIONSHIP OF SURF 2.0')

c1.adicionar_surfistas_L(s1)
c1.adicionar_surfistas_L(s2)
c1.adicionar_surfistas_L(s3)
c1.adicionar_surfistas_F(s4)
c1.adicionar_surfistas_F(s5)
c1.adicionar_surfistas_P(s6)
evento = True

while(evento):

  print(f'\nBEM-VINDO AO CAMPEONATO {c1.nome}!!!')
  print(f'''Digite a opção que deseja executar:
0 - Sair do campeonato;
1 - Menu de PILHA;
2 - Menu de FILA;
3 - Menu de LISTA;
4 - Quantidade de surfistas''')
  menu = input()
  menu_pilha = ''
  menu_fila = ''
  menu_lista = ''


  if(menu == '0'):
    evento = False
    break


  elif(menu == '1'):
    
    while(menu_pilha != '0'):
      print('\n===MANIPULAÇÃO DA PILHA DE SURFISTAS===')
      print(f'''Digite a opção deseja executar:
0 - Sair da pilha;
1 - Mostrar quantidade de surfistas na pilha;
2 - Registrar novo surfista na pilha;
3 - Remover surfista da pilha;
4 - Ver o surfista no topo da pilha''')
      
      menu_pilha = input()
    
      if(menu_pilha == '0'):
        break
    
      elif(menu_pilha == '1'):
        print(f'Quantidade de surfistas na pilha:',c1.mostrar_tam_surfistasP())
    
      elif(menu_pilha == '2'):
        
        try:
          print(f'===Registro de surfista===')
          nome = input('Digite o nome do surfista:')
          idade = int(input('Digite a idade: '))
          cpf = input('Digite o CPF: ')
          titulos = int(input('Quantidade de títulos: '))
          surfista = Surfista(nome, titulos, idade, cpf)
          c1.adicionar_surfistas_P(surfista)
          print('Surfista adicionado com sucesso.')
        
        except ValueError:
          print('Erro! Digite um valor válido.')
        
        except:
          print('Algo deu errado. Tente novamente.')


      elif(menu_pilha == '3'):
        
        try:
          c1.remover_surfista_P()
          print('Surfista removido com sucesso.')
        
        except PilhaException as PE:
          print(PE)
        

      elif(menu_pilha == '4'):
        
        try:
          print(c1.busca_surfista_P())
        
        except AssertionError as AE:
          print(AE)

      else:
        print('Dado inválido.')
        
        
  elif(menu == '2'):

    while(menu_fila != '0'):
      print('\n===MANIPULAÇÃO DA FILA DE SURFISTAS===')
      print(f'''Digite a opção deseja executar:
0 - Sair da FILA;    
1 - Mostrar quantidade de surfistas na fila;
2 - Registrar novo surfista na fila;
3 - Remover surfista da fila;
4 - Mostrar surfista no início da FILA;''')
      menu_fila = input()

      if(menu_fila == '1'):
        print(f'Quantidade de surfista na fila:', c1.mostrar_tam_surfistasF())

      elif(menu_fila == '2'):
        
        try:
          print(f'===Registro de surfista===')
          nome = input('Digite o nome do surfista:')
          idade = int(input('Digite a idade: '))
          cpf = input('Digite o CPF: ')
          titulos = int(input('Quantidade de títulos: '))
          surfista = Surfista(nome, titulos, idade, cpf)
          c1.adicionar_surfistas_F(surfista)
          print('Surfista adicionado com sucesso!')

        except ValueError:
          print('Erro na digitação dos tipos, tente novamente.')
          
        except:
          print('Algo deu errado. Tente novamente.')
      
      
      elif(menu_fila == '3'):

        try:
          c1.remover_surfista_F()
          print('Surfista removido com sucesso.')
          
        except FilaException as FE:
          print(FE)

      elif(menu_fila == '4'):
        
        try:
          print(c1.busca_surfista_F())

        except AssertionError as AE:
          print(AE)
          
      else: 
        print('Dado inválido!')


  elif(menu == '3'):

    while(menu_lista != '0'):
      print('\n===MANIPULAÇÃO DA LISTA DE SURFISTAS===') 
      print(f'''Digite a opção deseja executar:
0 - Sair da LISTA;    
1 - Mostrar quantidade de surfistas na LISTA;
2 - Registrar novo surfista na LISTA;
3 - Remover surfista da LISTA;
4 - Busca Surfista;
5 - Imprimir surfistas na Lista
6 - Maior e Menor idade;
7 - Ordenar lista de surfistas
8 - Incrementa título''')
      menu_lista = input()

      if(menu_lista == '1'):
        print('Quantidade de surfistas na lista:',c1.mostrar_tam_surfistasL())

      elif(menu_lista == '2'):
        
        try:
          print(f'\n===Registro de surfista===')
          nome = input('Digite o nome do surfista:')
          idade = int(input('Digite a idade: '))
          cpf = input('Digite o CPF: ')
          titulos = int(input('Quantidade de títulos: '))
          posicao = int(input('Posição na lista: '))
          surfista = Surfista(nome, titulos, idade, cpf)
          
          c1.adicionar_surfistas_L(surfista, posicao)
          print('Surfista adicionado com sucesso.')

        except ValueError:
          print('Erro na digitação dos dados. Tente novamente.')
        
        except ListaException as LE:
          print(LE)

        except:
          print('Algo deu errado. Tente novamente;')

      elif(menu_lista == '3'):
        
        try:
          print('Remover Surfista')
          posicao = int(input('Digite a posição que deseja remover: '))
          c1.remover_surfista_L(posicao)
          print('Surfista removido com suceso.')
        
        except ValueError:
          print('Erro na digitação dos dados. Tente novamente.')
        
        except ListaException as LE:
            print(LE)
        
        except:
          print('Algo deu errado. Tente novamente')

      elif(menu_lista == '4'): #busca
        try:
          cpf = input('Digite o CPF do surfista:')
          sx = c1.busca_surfista(cpf)
          print(sx)

        except ListaException as LE:
          print(LE)

        except:
          print('Algo deu errado, tente novamente.')

      elif(menu_lista == '5'): #imprimir LISTA
        if(c1.mostrar_tam_surfistasL() > 0): 
          c1.imprimir_surfistas()
        
        else:
          print('Não há nenhum surfista na lista.\n')

      elif(menu_lista == '6'): #maior e menor
      
        try:
          print('Surfista com a maior idade na lista: '+ c1.maior_idade())
          print('Surfista com a maior idade na lista: ' + c1.menor_idade())
        
        except CampeonatoException as CE:
          print(CE)


      elif(menu_lista == '7'):

        try: 
          print(f'Lista de surfistas:')
          c1.imprimir_surfistas()

          c1.ordena_surfistas()
          
          print(f'Lista de surfistas ordenada:')
          c1.imprimir_surfistas()
        
        except AssertionError as AE:
          print(AE)
        
        except ListaException as LE:
          print(LE)


      elif(menu_lista == '8'): #fim do campeonato
        
        try:
          print('O CAMPEONATO FOI REALIZADO!')
          cpf = input('Digite o CPF do vencedor: ')
          c1.incrementa_titulo_surfista(cpf)
          print('VENCEDOR:',c1.busca_surfista(cpf))

        except ListaException as LE:
          print(LE)
        
        except CampeonatoException as CE:
          print(CE)


  elif(menu == '4'):
    print('Os surfistas estão armazenados em Listas, Pilhas e Filas.')
    print('Tamanho da pilha: ',c1.mostrar_tam_surfistasP())
    print('Tamanho da fila: ',c1.mostrar_tam_surfistasF())
    print('Tamanho da lista: ',c1.mostrar_tam_surfistasL())
    print('Número total de surfistas no campeonato: ',c1.mostrar_tam_total())

  else:
    print('Opção inválida. Tente novamente.')

print('Fim do programa.')