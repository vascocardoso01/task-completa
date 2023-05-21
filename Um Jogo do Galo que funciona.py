# Lista do jogo e Regras
tab = ['#','1','2','3','4','5','6','7','8','9']
print('BEM-VINDOS ao Jogo do Galo! Este é o vosso tabuleiro de jogo!')


# Função que define o tabuleiro
def tabuleiro():
    print(tab[7],'|', tab[8],'|',tab[9])
    print('----------')
    print(tab[4],'|',tab[5],'|', tab[6])
    print('----------')
    print(tab[1],'|',tab[2],'|',tab[3])
tabuleiro()

# Definição que verifica os resultados
def verificar():
    for i in range(1,10,3):
        if tab[i]==tab[i+1]==tab[i+2]:
            return True
    for i in range(1,4):
        if tab[i]==tab[i+3]==tab[i+6]:
            return True
    if tab[1]==tab[5]==tab[9]:
        return True
    elif tab[7]==tab[5]==tab[3]: 
        return True
    return False

# Função que define os caracteres utilizados em jogo
def caracteres():
    print('Em primeiro lugar, vamos definir os caracteres de jogo:')
    char_jogador1 = input('JOGADOR 1 -> Escolhe um caracter para jogares:')
    while len(char_jogador1) != 1 or char_jogador1.isdigit()==True:
        char_jogador1 = input('ERRRADO! Escolhe UM caracter para jogares:')
    else:
        print(f'O JOGADOR 1 vai jogar com o caracter {char_jogador1}')

    char_jogador2 = input('JOGADOR 2 -> Escolhe um caracter para jogares, diferente do JOGADOR 1:')
    while len(char_jogador2) != 1 or char_jogador2 == char_jogador1 or char_jogador1.isdigit()==True:
        char_jogador2 = input('ERRRADO! Escolhe UM caracter para jogares, DIFERENTE do JOGADOR1:')
    else:
        print(f'O JOGADOR 2 vai jogar com o caracter {char_jogador2}')
    return char_jogador1,char_jogador2

simbolo1, simbolo2 = caracteres()

# Jogadas 
def jogo():
    jogadas_possiveis = ['1','2','3','4','5','6','7','8','9']
    count = 0
    while count <= 8:
        print(tabuleiro()) 
        jogada = input('Escolhe em que posição colocar o teu caracter (1-9):')
        while jogada not in jogadas_possiveis:                                                              
            jogada = input('Escolhe em que posição (disponível) colocar o teu caracter (1-9) - número:')
        if count%2 == True:
            tab[int(jogada)] = simbolo1
        else:
            tab[int(jogada)] = simbolo2
        jogadas_possiveis.remove(jogada) 
        count +=1
        if verificar():
            tabuleiro()
            print('Parabéns')
            return True
        else:
            continue
    tabuleiro()
    print('Empate! Tentem outra vez!')


#Jogo
jogo()

