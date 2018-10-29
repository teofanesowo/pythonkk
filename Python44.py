#Estou com duvida nessa questão porque não sei se o ICMS é aplicado a conta
#Estou trabalhando calculando essa taxa de 17% que foi dada no valor final
#caso eu esteja errado vou deixar esse código como algo a revisar depois pq não achei nada para confirmar minha ideia
consumo = float(input('Digite o seu consumo do mês em KWh: '))
taxa = float(input('Digite o custo por KWh consumido na sua região: '))
print('~~~~ O valor da taxa de iluminação pública é R$15.00 ~~~~')
custo = (consumo*taxa + 15)*1.17
print('O valor que você deve pagar é R${:.2f}'.format(custo))