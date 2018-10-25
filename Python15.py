#ignora os printskkkjk, essa era uma atividade de manipulação simples de string
palavra = input('Digite uma palavra: ')
posicao = int(input('Digite a posição que vc quer: '))
if posicao < 0:
    print('Não existe posição {}, você não estudou geometria euclidiana não?(eu sei que existe em programação, mas pau no seu cu porra me da um valor positivo é pedir muito?)'.format(posicao))
if 0 < posicao < (len(palavra)):
    valor = palavra[posicao-1]
    print('A letra é {}'.format(valor))
if posicao > len(palavra):
    print('Então, você precisa me fornecer uma posição que esteja no tamanho de sua palavra né?')