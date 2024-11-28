import os

def finalizar():
     
    sair = int(input('''press 1 refazer operações
press 2 para sair 
digite aqui: '''))
     
    if sair == 1:
        main()
    elif sair == 2:
        print('''
              ///finalizando programa///
              ''')


def opcao_invalida():
    print('opção invalida \n')
    main()

def soma():
    a = int(input('digite um numero:')) 
    b = int(input('digite um numero:'))
    print('\n sua soma resultou em: ',a + b, '\n' )
    finalizar()



def subtracao(): 
    a = int(input('digite um numero: '))
    b = int(input('digite um numero para subtração: '))
    print(a - b)
    finalizar()

def multiplicacao():
    a = int(input('digite um numero: '))
    b = int(input('digite um numero: '))
    print(a * b)
    finalizar()

def divisao():
    a = int(input('digite um numero: '))
    b = int(input('digite um numero: '))
    print(a / b)
    finalizar()

def exibir_opcoes():
    print('digite 1 para soma')
    print('digite 2 para subtração')
    print('digite 3 para multiplicação')
    print('digite 4 para divisão\n')



def opcao_escolhida():
  
    escolhida = int(input('escolha uma opção: '))

    if escolhida == 1:
            soma()
    elif escolhida == 2:
            subtracao()
    elif escolhida == 3:
            multiplicacao()
    elif escolhida == 4:
            divisao()
    else:
            opcao_invalida()



def main():
    os.system('cls')
    exibir_opcoes()
    opcao_escolhida()

if __name__ == '__main__':
    main()


