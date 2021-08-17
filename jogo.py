def usuario_escolhe_jogada(n, m):
    return int(input("Quantas peças você vai tirar? "))

def computador_escolhe_jogada(n, m):
    if n >= m:
        return m
    else:
        return n

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print("")
    if n % (m + 1) == 0:
        print("Voce começa!")
    else:
        print("Computador começa!")
    if n % (m + 1) != 0:
        while n >= 0:
            print("")
            comput = computador_escolhe_jogada(n, m)
            n = n - comput
            if comput > 1:
                print("O computador tirou", comput, "peças.")
            else:
                print("O computador tirou uma peça.")
            if n > 1:
                print("Agora restam", n, "peças no tabuleiro.")
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            elif n == 0:
                break
            print("")
            voce = usuario_escolhe_jogada(n, m)
            if voce <= m:
                if voce > 1:
                    print("Voce tirou", voce,"peças.")
                else:
                    print("Você tirou uma peça.")
                n = n - voce
                if n > 1:
                    print("Agora restam", n, "peças no tabuleiro.")
                elif n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                elif n == 0:
                    break
            else:
                print("")
                print("Oops! Jogada inválida! Tente de novo.")
                print("")
                voce = usuario_escolhe_jogada(n, m)
                if voce > 1:
                    print("Voce tirou", voce,"peças.")
                else:
                    print("Você tirou uma peça.")
                n = n - voce
                if n > 1:
                    print("Agora restam", n, "peças no tabuleiro.")
                elif n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                elif n == 0:
                    break
                
    elif n % (m + 1) == 0:
        while n >= 0:
            print("")
            voce = usuario_escolhe_jogada(n, m)
            if voce <= m:
                if voce > 1:
                    print("Voce tirou", voce,"peças.")
                else:
                    print("Você tirou uma peça.")
                n = n - voce
                if n > 1:
                    print("Agora restam", n, "peças no tabuleiro.")
                elif n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                elif n == 0:
                    break
            else:
                print("")
                print("Oops! Jogada inválida! Tente de novo.")
                print("")
                voce = usuario_escolhe_jogada(n, m)
                if voce > 1:
                    print("Voce tirou", voce,"peças.")
                else:
                    print("Você tirou uma peça.")
                n = n - voce
                if n > 1:
                    print("Agora restam", n, "peças no tabuleiro.")
                elif n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                elif n == 0:
                    break         
            print("")
            comput = computador_escolhe_jogada(n, m)
            n = n - comput
            if comput > 1:
                print("O computador tirou", comput, "peças.")
            else:
                print("O computador tirou uma peça.")
            if n > 1:
                print("Agora restam", n, "peças no tabuleiro.")
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            elif n == 0:
                break
    print("Fim do jogo! O computador ganhou!")

print("Bem-vindo ao jogo do NIM! Escolha:")
print("")
print("1 - para jogar uma partida isolada")
cp = int(input("2 - para jogar um campeonato "))
print("")
if cp == 1: 
    print("Voce escolheu uma partida!")
    print("")
    print("**** Rodada 1 ****")
    print("")
    partida()
    
elif cp == 2:
    print("Voce escolheu um campeonato!")
    print("")
    print("**** Rodada 1 ****")
    print("")
    partida()
    print("")
    print("**** Rodada 2 ****")
    print("")
    partida()
    print("")
    print("**** Rodada 3 ****")
    print("")
    partida()
    print("")
    print("**** Final do campeonato! ****")
    print("")
    print("Placar: Você 0 X 3 Computador")
