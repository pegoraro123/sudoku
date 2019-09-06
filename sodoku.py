import sys
menu= input('Você deseja jogar Sudoku{S/N}:').upper()#Pede ao usuário se ele deseja jogar ou não
if menu == 'N':
	print('Passe bem')
	sys.exit()
	
elif menu == 'S':
	print('Bom jogo!!!')
	
else:
	print('Opção invalida')
	sys.exit()
	
tuto = '''

O Sudoku é um passatempo, pra ser jogado em uma pessoa,
que envolve raciocínio e lógica. A ideia do jogo é bem simples, completar todas as 81 células usando números de 1 a 9,
sem repetir os números numa mesma linha, coluna ou grade (3x3).'''



print(tuto)


import random 
num=random.randint(0,9)
num1=random.randint(0,9)
num2=random.randint(0,9)
num3=random.randint(0,9)
num4=random.randint(0,9)
num5=random.randint(0,9)
num6=random.randint(0,9)
num7=random.randint(0,9)
num8=random.randint(0,9)
num9= (num,num2,num3,num4,num5,num6,num7,num8)#Sorteia números no tabuleiro
lista = [
    [' ', ' ' ,num, ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', num1, ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', num2],
    [' ', num3, ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', num4, ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', num5, ' ', ' '],
    [' ', ' ', ' ', ' ', num6, ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', num7, ' '],
    [num8,' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]
def tabuleiro():#Printa o tabuleiro 

    print ('''
    		1   2   3   4   5   6   7   8   9
              +===================================+
           1  | {} | {} | {} | {} | {} | {} | {} | {} | {} |
           2  | {} | {} | {} | {} | {} | {} | {} | {} | {} |
           3  | {} | {} | {} | {} | {} | {} | {} | {} | {} |
              +===================================+
           4  | {} | {} | {} | {} | {} | {} | {} | {} | {} |
           5  | {} | {} | {} | {} | {} | {} | {} | {} | {} |
           6  | {} | {} | {} | {} | {} | {} | {} | {} | {} |
              +===================================+
           7  | {} | {} | {} | {} | {} | {} | {} | {} | {} |
           8  | {} | {} | {} | {} | {} | {} | {} | {} | {} |
           9  | {} | {} | {} | {} | {} | {} | {} | {} | {} |
              +===================================+
             '''.format(lista[0][0],lista[0][1],lista[0][2],lista[0][3],lista[0][4],lista[0][5],lista[0][6],lista[0][7],lista[0][8],

                        lista[1][0],lista[1][1],lista[1][2],lista[1][3],lista[1][4],lista[1][5],lista[1][6],lista[1][7],lista[1][8],

                        lista[2][0],lista[2][1],lista[2][2],lista[2][3],lista[2][4],lista[2][5],lista[2][6],lista[2][7],lista[2][8],

                        lista[3][0],lista[3][1],lista[3][2],lista[3][3],lista[3][4],lista[3][5],lista[3][6],lista[3][7],lista[3][8],

                        lista[4][0],lista[4][1],lista[4][2],lista[4][3],lista[4][4],lista[4][5],lista[4][6],lista[4][7],lista[4][8],

                        lista[5][0],lista[5][1],lista[5][2],lista[5][3],lista[5][4],lista[5][5],lista[5][6],lista[5][7],lista[5][8],

                        lista[6][0],lista[6][1],lista[6][2],lista[6][3],lista[6][4],lista[6][5],lista[6][6],lista[6][7],lista[6][8],

                        lista[7][0],lista[7][1],lista[7][2],lista[7][3],lista[7][4],lista[7][5],lista[7][6],lista[7][7],lista[7][8],

                         lista[8][0],lista[8][1],lista[8][2],lista[8][3],lista[8][4],lista[8][5],lista[8][6],lista[8][7],lista[8][8],))#Acessa os indices do tabuleiro

vitoria= 0
seq= {"1","2","3","4","5","6","7","8","9"}


while True:
#Repete as jogadas


    def ganhador():
        cont = 0

        vitoria = 0

        for p in range(0,9):#Facilita a verificação transformando inteiros para strings
            for g in range(0,9):

                if lista[p][g] in num9:

                    lista[p][g] = str(lista[p][g])



        for linha in lista:

            coluna = [f[cont] for f in lista]#Acessa colunas
            quad = (cont // 3) * 3#Acessa quadrados
            cont += 1

            square = [lista[k][v] for k in range(quad, quad + 3) for v in range(quad, quad + 3)]#Acessa o quadrante
            if set(square) == seq and set(coluna) == seq and set(linha) == seq:#Compara com um conjunto em caso de vitória
                vitoria+=1

        if vitoria == 9:

            print("PARABÉNS!!!")

            sys.exit()

        else:

            for p in range(0,9):

                for g in range(0,9):

                    if lista[p][g] in num9:

                        lista[p][g] = int(lista[p][g])#Transforma em strings, caso usuário perca






    for m in lista:

        if ' ' in m or ' ' not in m:

            tabuleiro()
#Chama o tabuleiro
            fila = input("Digite fila desejada:")

            coluna = input("Digite coluna desejada:")

            num = input("Digite número desejado:")
#Interage com usuario
            while fila not in seq or coluna not in seq or num not in seq or lista[int(fila)-1][int(coluna)-1] in num9:#Verifica valides da jogada
                fila = input("Digite uma fila válida:")

                coluna = input("Digite uma coluna válida:")

                num = input("Digite um número válido de 1 a 9:")

            lista[int(fila)-1][int(coluna)-1] = num#Faz com que número apareça no tabuleiro
            ganhador()
#Chama a função ganhador
