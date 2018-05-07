from RNA.SerieTemporal import SerieTemporal
from RNA.EntradaRna import EntradaRna
# from RNA.Rna import Rna
from keras import *
from keras.layers import Dense

serie = SerieTemporal('gera_saida/dicionario.csv')
anoFinal = len(serie.Serie)-10
entrada = EntradaRna(serie, anoFinal, ordemEntrada= 11)
entrada.preparaTreinoComListaMesesEspecificos(anoFinal, [1])
entrada.preparaTesteComMesEspecifico(anoFinal, 1)

def rna(x_treino, x_teste, y_treino, yTeste, epocas, numNeuroniosCamOculta, optimizer, entrada):
    rna = Sequential()
    rna.add(Dense(units=numNeuroniosCamOculta, input_dim=entrada.ordemEntrada, activation='relu'))
    # rna.add(Dense(units=numNeuroniosCamOculta, activation='relu'))
    # rna.add(Dense(units=100, input_dim=29, activation='relu'))
    # rna.add(Dense(units=10, activation='linear'))
    # rna.add(Dense(units=10, input_dim=29, activation='linear'))
    # # rna.add(Dense(units=60, input_dim=7, activation='RELU'))
    # rna.add(Dense(units=320, activation='relu'))
    # rna.add(Dense(units=320, activation='relu'))
    rna.add(Dense(units=1, activation='linear'))
    # print(x_treino)
    rna.compile(optimizer=optimizer,
                loss='mean_squared_error',
                metrics=[ 'mean_absolute_percentage_error'])
    modelo = rna.fit(x_treino, y_treino, verbose=2, epochs=epocas)
    # return rna.predict(x_teste, verbose=0), rna.evaluate(xTeste, yTeste), modelo.history['binary_crossentropy']
    return rna.predict(x_teste, verbose=0), None, modelo.history['mean_absolute_percentage_error']

# print(entrada.xTreino)
# print(entrada.yTreino)
for x, y in zip(entrada.xTreino, entrada.yTreino):
	print(x , y)

for x, y in zip(entrada.xTeste, entrada.yTeste):
	print(x , y)
print(rna(entrada.xTreino, entrada.xTeste, entrada.yTreino, entrada.yTeste, 1000, 30, 'adam', entrada))
# rna = Rna(EntradaRna)
# rna.ArquiteturaRna([(10, 'sigmoid'), (1, 'sigmoid')], verbose=1, epocas=10)
# print(rna.previsaoSerie(final))

