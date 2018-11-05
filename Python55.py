# engenharia kKKJK
numerop = int(input('Número de pedreiros: '))
numeroa = int(input('Número de ajudantes: '))
diariap = int(input('Diária do pedreiro: '))
custo = numerop*diariap*180 + numeroa*(diariap/2)*180
print('O custo total da mão de obra foi: R${:.2f}'.format(custo))

