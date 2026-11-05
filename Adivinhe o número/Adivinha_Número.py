
import random

def validar_numero(valor: int) -> bool:
    if valor >= menor and valor <= maior:
        return True
    else:
        return False


def verificar_acerto(valor: int) -> bool:
    if valor == sorteio:
        return True
    else:
        return False

def define_pontos(tentativas:int)-> int:
    if(tentativas == 0):
        return 100
    elif(tentativas == 1):
        return 80
    elif(tentativas == 2):
        return 60
    elif(tentativas == 3):
            return 40
    elif(tentativas == 4):
        return 20
    
def jogarnovamente(resposta:int)-> bool:
    if(resposta == 1):
        return True
    else:
        return exit

def escolherdificuldade(escolha_dificuldade:int):
    if(escolha_dificuldade == 0):
        menor, maior = random.randint(0, 0), random.randint(50, 50)
        return menor, maior
    elif(escolha_dificuldade == 1):
        menor, maior = random.randint(0, 0), random.randint(100, 100)
        return menor, maior
    elif(escolha_dificuldade == 2):
        menor, maior = random.randint(0, 0), random.randint(500,500)
        return menor, maior
        

# Main
resposta = True
dificuldade = -1

   

#loop para jogar Novamente
while(resposta == True):
    
     #Verificação pra escolher apenas números de 0 a 2
    while(dificuldade < 0 or dificuldade > 2):

        print("Escolha a diciculdade ")
        print("[0] Fácil (números de zero a cinquenta)")
        print("[1] Médio (números de zero a cem)")
        print("[2] Difícil (números de zero a quinhentos)")
        dificuldade = int(input())
        
    #saindo do laço de verificação da dificuldade
        if(dificuldade <0 or dificuldade >2):
            print("Número inválido")

    #atribuindo o menor e maior valor dependendo da resposta do usuário
    menor,maior = escolherdificuldade(dificuldade)
    
    tentativa = 0
    
    #Apenas para exibir na tela as tentativas
    conta_tentativa = 5

    sorteio = random.randint(menor, maior)
    '''
    mostra numéro escolhido e quantidade de tentativas (para teste)
    
    print(sorteio)
    print(f"{tentativa}")
    '''

    num = int(input(f'Número ({menor}-{maior}): '))

    while verificar_acerto(num) != True and validar_numero(num) == True:
        
        tentativa +=1
        conta_tentativa -=1 
        if (tentativa >= 5):
           
            break
        if num > sorteio:
            maior = num - 1
            print('Errou: Seu chute foi maior.')
        else:
            menor = num + 1
            print('Errou: Seu chute foi menor.')
        
        
        print(f"Você tem {conta_tentativa} tentativas restantes")    
        num = int(input('Número: '))


    # saiu do laço
    
    #resultado certo
    if verificar_acerto(num) == True:
        total_pontos = define_pontos(tentativa)
        print('Acertou:', num)
        print(f"Total de tentativas:{tentativa}")
        print(f"Pontuação total: {total_pontos}")
    #Resultado perda    
    elif(tentativa>=5):
     print("Você perdeu! ")
     print(f"o número escolhido era {sorteio}")
    #Resultado número inválido 
    else:
        print('Chute inválido!')
        


    dificuldade = -1
    #resetando dificuldade para escolhe-la novamente
    
    #Jogar novamente
    print("Deseja jogar novamente?")
    print("Digite 1 para jogar novamente e 0 para sair")
    resposta = int(input())
    jogarnovamente(resposta)
