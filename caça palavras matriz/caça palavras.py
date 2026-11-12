import random

def criar_matriz(linhas:int,colunas:int)->list:
    matriz = []
    for i in range(linhas):
        matriz.append(["" ]* colunas)
    return matriz

def exibir_matriz(matriz:list):
    for linha in matriz:
        print(*linha)

def iniciar_matriz(matriz:list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = chr(random.randint(ord("A"),ord("Z")))
        #CHR transforma o codigo ascii em simbolo e ORD transforma simbolo em ascii

def validacao(posicoes_ocupadas,linha,coluna):
    if [linha,coluna] not in posicoes_ocupadas:
        return True
    else:
        return False

def palavra_horizontal(palavra:str,matriz):
    #linha_inicial = random.randint (0,len(matriz) -1)
    #escolhe a linha aleatoria, de zero até o tamanho maxímo de linhas

    #max_palavra =len(matriz[0]) - len(palavra)
    #calcula a posição maxima na matriz (coluna) que a palavra pode ficar

    #sortear_comeco_palavra = random.randint(0,max_palavra) 
    #sorteia começo da palavra (coluna)
    contador = 0
    while contador < 10:
        linha_inicial = random.randint (0,len(matriz) -1)
        max_palavra =len(matriz[0]) - len(palavra)
        sortear_comeco_palavra = random.randint(0, max_palavra)
        posicoes_validas = True

        for i in range (len(palavra)):
            linha = linha_inicial
            coluna = sortear_comeco_palavra + i
            resultado = validacao(posicoes_ocupadas,linha,coluna)
            #valida a linha e coluna baseado no array de posição ocupadas

            if resultado == False:
                posicoes_validas = False 
                break
            #Se cair em uma posição ocupada volta pra o while
   
        if posicoes_validas == True:
                for j in range(len(palavra)):
                    linha = linha_inicial
                    coluna = sortear_comeco_palavra + j
                    #Anda uma casa (Coluna) a cada letra
                    
                    posicoes_ocupadas.append([linha ,coluna])
                    #Add a posição no array
                    matriz[linha][coluna] = palavra[j]
                    #Add a letra na sua posição na matriz
                break
        contador+= 1 
        #Se chegar em 10 tentativas inválidas a palavra não será adicionada a matriz
                

def palavra_vertical(palavra:str,matriz:list):
    coluna_inicial = random.randint(0,len(matriz[0])-1)

    max_palavra = len(matriz) - len(palavra)

    sortear_comeco_palavra = random.randint(0,max_palavra)

    for i in range (len(palavra)):
        posicoes_ocupadas.append([sortear_comeco_palavra + i,coluna_inicial])

def diagonal_decressente (palavra:str,matriz:list):
    coluna_max = len(matriz[0]) - len(palavra)
    linha_max = len(matriz) - len(palavra)

    sortear_linha = random.randint(0,linha_max)
    sortear_coluna = random.randint(0,coluna_max)

    linha_atual = sortear_linha
    coluna_atual = sortear_coluna

    for i in range (len(palavra)):
            posicoes_ocupadas.append([linha_atual,coluna_atual])
            linha_atual +=1
            coluna_atual +=1 



def diagonal_crescente(palavra:str,matriz:list):
     max_linha  =  (len(matriz) -1)
     
     max_coluna = (len(matriz[0]) - len(palavra))
     #max de colunas e a quantidade de colunas - tamanho da palavra

     sortear_linha = random.randint(len(palavra) - 1, max_linha)
     #sorteia uma linha entre o tamanho da palavra e o max de linha
     #esse len palavra é pq se começar com uma linha alta [0,1,2] a palavra sai da matriz

     sortear_coluna = random.randint(0,max_coluna)

     coluna_atual = sortear_coluna
     linha_atual = sortear_linha

     for i in range (len(palavra)):
          posicoes_ocupadas.append([linha_atual,coluna_atual])
          linha_atual -=1
          coluna_atual +=1
#TODO colocar palavras reverso,Adicionar verificação nos outros sentidos              

            
            

def adicionar_palavras(palavras:list,matriz:list):
    for i in range(4): 
        num = random.randint(1,4)

        match num:
            case 1:
                palavra_vertical(palavras[i],matriz)
            case 2:
                palavra_horizontal(palavras[i],matriz) 
            case 3:
                diagonal_crescente(palavras[i],matriz)
            case 4:
                diagonal_decressente(palavras[i],matriz) 


def validar_posicao(matriz):
    pass


#Main
posicoes_ocupadas = []

PALAVRAS = ["PYTHON","JAVA","RUST","PHP"]

tabuleiro = criar_matriz(10,10)
iniciar_matriz(tabuleiro)
#exibir_matriz(tabuleiro)
palavra_horizontal("PYTHON",tabuleiro)
palavra_vertical("JAVA",tabuleiro)

diagonal_decressente("RUST",tabuleiro)
exibir_matriz(tabuleiro)   
