from RNA.SerieTemporal import SerieTemporal
from RNA.EntradaRna import EntradaRna
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
    rna.add(Dense(units=1, activation='linear'))
    rna.compile(optimizer=optimizer,
                loss='mean_squared_error',
                metrics=[ 'mean_absolute_percentage_error'])
    modelo = rna.fit(x_treino, y_treino, verbose=2, epochs=epocas)
    return rna.predict(x_teste, verbose=0), None, modelo.history['mean_absolute_percentage_error']


for x, y in zip(entrada.xTreino, entrada.yTreino):
	print(x , y)

for x, y in zip(entrada.xTeste, entrada.yTeste):
	print(x , y)
print(rna(entrada.xTreino, entrada.xTeste, entrada.yTreino, entrada.yTeste, 1000, 30, 'adam', entrada))