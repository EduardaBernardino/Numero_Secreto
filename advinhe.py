##############JOGO DE ADVINHAÇÃO######
from random import randint

EASY = 10
HARD = 5

# Sorteia o número secreto
resposta_correta = randint(1, 100)

def dificuldade():
    """Escolhe o nível de dificuldade"""
    opcao = input("Escolha a sua dificuldade: 'easy' ou 'hard': ")
    if opcao == 'easy':
        return EASY
    elif opcao == 'hard':
        return HARD
    else:
        print("Opção inválida! Padrão 'easy'.")
        return EASY

def aposta(resposta_correta, tentativas):
    """Loop de tentativas até acertar ou acabar as chances"""
    while tentativas > 0:
        print(f"Você tem {tentativas} tentativas restantes")
        chute = int(input("Faça um chute: "))

        if chute > resposta_correta:
            print("Muito alto!")
        elif chute < resposta_correta:
            print("Muito baixo!")
        else:
            print(f"Parabéns! Você acertou, o número era {resposta_correta}")
            return

        tentativas -= 1  # agora sim decrementa certo

    print(f"Acabaram as tentativas! O número era {resposta_correta}")

def jogar():
    print("./Bem-vindo(a)! Vamos jogar? Adivinhe um número de 1 a 100")
    tentativas = dificuldade()
    aposta(resposta_correta, tentativas)

# Inicia o jogo
jogar()
