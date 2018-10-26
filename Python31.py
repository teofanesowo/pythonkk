#duvida em uma coisa aqui
acerto = int(input('Digite o número de acertos: '))
erro = int(input('Digite o número de erros: '))
branco = int(input('Questões em branco: '))
pontuacao = 5*acerto - 3*erro
print('Pontuação final: {}'.format(pontuacao))