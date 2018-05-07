import multiprocessing as mp
import time as start_time
import matplotlib.pyplot as plt
from glob import glob as globglob
import datetime
import numpy as np
# import cenarios

TAMANHO_JANELA_TEMPO = 3 #180 # em segundosss

def converte_tempo(hora):
    # print(hora,"deus")
    x = start_time.strptime(hora,"%H:%M:%S")
    y = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
    return y


# def inicia_dicionario_tempo_tempo(tempoInicial, segundos=1):
#     dicionario = {}

def funcao_gera_dicionario(f):
    '''
    gera dicionario a partir da base crua
    '''
    dicionario_ips_tempos ={}
    # dicionario_Horas = {}
    for linha in f:
        if linha is not "":
            # aux=str(linha.split()[2][-8:])
            # x = start_time.strptime(str(aux),"%H:%M:%S")
            hora = converte_tempo(linha.split()[2][-8:])
            aux = int(hora)
            # print(aux)
            ip = linha.split()[0]
            if(not(aux) in dicionario_ips_tempos):
                list=[]
                # ip = linha.split()[0]
                list.append(str(ip))
                dicionario_ips_tempos[aux]=list
            else:
                dicionario_ips_tempos[aux].append(str(ip))
    return dicionario_ips_tempos


def escreve_dicionario_arquivo(dic):
    '''
    escreve dicionario no arquivo
    '''
    with open("/home/snoopy/Projetos_codigos/projeto_logLeticia/gera_saida/dicionario.csv","w") as dicionario:
        for data, num_ip in zip(dic.keys(),dic.values()):
            dicionario.write(str(data)+","+str(num_ip)+"\n")


def funcao_gera_histograma_burro(dic):
    # tamanhos=[len(x) for x in dic.values()]
    
    # horas = [ int(float(x)) for x in dic.keys()]
    # print(horas)
    # print
    tempos = list(dic.keys())
    # print(tempos)
    numeroBins = int((np.max(tempos)-np.min(tempos)+int(1))/TAMANHO_JANELA_TEMPO)
    # print("aqqquuiiiii ",numeroBins)
    # plt.hist(dic.keys(),density=True, stacked=True,cumulative=True,histtype='bar')
    counts, bin_edges = np.histogram(list(dic.keys()), bins=numeroBins)
    print(bin_edges[:-1], counts)
    dic = dict(zip(bin_edges[:-1], counts))
    # print(dicionario)
    return dic
    # print('counts', counts)
    # print('edges', bin_edges)
    # cdf =np.cumsum(counts)
    # plt.plot(bin_edges[1:],cdf)
    # # plt.bar(list(dic.keys()),tamanhos,color='b')
    # plt.show()
    # f = open('/home/snoopy/Projetos_codigos/projeto_logLeticia/instancia/instaciaBoa.txt','r')
    # for linha in f:4
    #     if linha is not "":
    #         print()

f = open('/home/snoopy/Projetos_codigos/projeto_logLeticia/instancia/instanciaTesteMaior.txt','r')
# escreve_dicionario_arquivo(funcao_gera_dicionario(f))
escreve_dicionario_arquivo(funcao_gera_histograma_burro(funcao_gera_dicionario(f)))
# for k in dicionario_ips_tempos:
#     print(k.keys,k.value)
# print(dicionario_ips_tempos)
