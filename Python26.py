#essa deu trabalho pq fazer assim é triste
atleta_peso11 = float(input('Peso em kg atleta1 dupla1: '))
atleta_peso12 = float(input('Peso em kg atleta2 dupla1: '))
atleta_peso21 = float(input('Peso em kg atleta1 dupla2: '))
atleta_peso22 = float(input('Peso em kg atleta2 dupla2: '))
atleta_peso31 = float(input('Peso em kg atleta1 dupla3: '))
atleta_peso32 = float(input('Peso em kg atleta2 dupla3: '))
atleta_peso41 = float(input('Peso em kg atleta1 dupla4: '))
atleta_peso42 = float(input('Peso em kg atleta2 dupla4: '))
atleta_altura11 = float(input('Altura em cm atleta1 dupla1: '))
atleta_altura12 = float(input('Altura em cm atleta2 dupla1: '))
atleta_altura21 = float(input('Altura em cm atleta1 dupla2: '))
atleta_altura22 = float(input('Altura em cm atleta2 dupla2: '))
atleta_altura31 = float(input('Altura em cm atleta1 dupla3: '))
atleta_altura32 = float(input('Altura em cm atleta2 dupla3: '))
atleta_altura41 = float(input('Altura em cm atleta1 dupla4: '))
atleta_altura42 = float(input('Altura em cm atleta2 dupla4: '))
mediaaltura1 = (atleta_altura11 + atleta_altura12)/2
mediaaltura2 = (atleta_altura21 + atleta_altura22)/2
mediaaltura3 = (atleta_altura31 + atleta_altura32)/2
mediaaltura4 = (atleta_altura41 + atleta_altura42)/2
mediapeso1 = (atleta_peso11 + atleta_peso12)/2
mediapeso2 = (atleta_peso21 + atleta_peso22)/2
mediapeso3 = (atleta_peso31 + atleta_peso32)/2
mediapeso4 = (atleta_peso41 + atleta_peso42)/2
mediaalturaall = (atleta_altura11 + atleta_altura12 + atleta_altura21 + atleta_altura22 + atleta_altura31 + atleta_altura32 + atleta_altura41 + atleta_altura42)/8
mediapesoall = (atleta_peso11 + atleta_peso12 + atleta_peso21 + atleta_peso22 + atleta_peso31 + atleta_peso32 + atleta_peso41 + atleta_peso42)/8
print('As médias de cada dupla são:')
print('-> Dupla 1 média de altura e peso, respectivamente: {}cm e {}kg'.format(mediaaltura1, mediapeso1))
print('-> Dupla 2 média de altura e peso, respectivamente: {}cm e {}kg'.format(mediaaltura2, mediapeso2))
print('-> Dupla 3 média de altura e peso, respectivamente: {}cm e {}kg'.format(mediaaltura3, mediapeso3))
print('-> Dupla 4 média de altura e peso, respectivamente: {}cm e {}kg'.format(mediaaltura4, mediapeso4))
print('Médias de todos os participantes: ')
print('Altura: {}cm //// Peso: {}kg'.format(mediaalturaall, mediapesoall))