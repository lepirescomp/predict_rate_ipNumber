# escovando
from gzip import open as gzopen
from glob import glob as globglob
from itertools import *
import threading as th,os
import time
# total de memoria que vamos usar no buffer
# tamanhoMemoria = 1

# para 2gb de buffer
# NUMERO_LINHAS_NO_BUFFER = 1894 #tamanho medio da linha * tamanhoCaracter /  < tamanhoMemoria
NUMERO_PROCESSOS_POR_VEZ = 150

def leSubarquivos(linha, saida):
    # for linha in baseDados:
    # with open('teste', 'a') as arq:
    # if(linha is not ""):

        # lock.acquire(block=False)
        aux = linha.split()[0] + ',' + linha.split()[2][-8:]+'\n'
        # lock.release()
        # print(aux)
        saida.write(str(aux))
        # filaSaida.append(aux)
    # else:
    #     saida.write("acabou")

def executaParalelo(arquivo, saida):
    # print('pooooo')
    # lock = th.Lock()
    with gzopen('/home/snoopy/base_de_dados/Base_original/logs-leticia.gz', 'rt') as baseDados:
        threads = []
        # print(baseDados.readline(1999))
        # return
        # while(True):
            # try:
        linha = baseDados.readline()
        while(linha is not ""):
                # linha = baseDados.readline()
                for i in range(NUMERO_PROCESSOS_POR_VEZ):
                    #le uma linha
                    linha = baseDados.readline()
                    # print(linha)
                    #cria um processo
                    processo = th.Thread(target=leSubarquivos, args=(str(linha), saida))
                    threads.append(processo)
                    # inicia o processo
                    processo.start()
                #diz para esperar os n acabarem
                    for thread in threads:
                        thread.join()
            # except EOFError as e:
            #     print("acabei")
            #     return


# pega todos os arquivos de um diretorio .gz
nomeGzip = '/home/snoopy/base_de_dados/'
# pool = mp.Pool(NUMERO_PROCESSOS_POR_VEZ)
# processes = []

diretorio = globglob(nomeGzip)
with open('../gera_saida/LogsLeticiaPreProcessado.txt', 'w') as saida:
    # abri um arquivo
    # print('arquivo')
    for arquivo in diretorio:
        # print(arquivo)
        executaParalelo(arquivo, saida)
        # calculaBufferCorta(arquivo, numPartes=3)
        # leComBuffer(arquivo)
        # corta a base em partes para processar ao mesmo tempo
        # baseCortada = cortaBaseDadosParaMultiProcessar()
        # # processa arquivos cortados
        # for parte in baseCortada:
        #     leSubarquivos(baseDados)
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
# pool.close()?


# def chunkify(fname,size=1024*1024):
#     # pega ultima posicao do arquivo
#     fileEnd = os.path.getsize(fname)
#     #abri arquivo e gaurda fim do pedaco
#     with open(fname,'r') as f:
#         chunkEnd = f.tell()
#         while True:
#             chunkStart = chunkEnd
#             f.seek(size,1)
#             f.readline()
#             chunkEnd = f.tell()
#             yield chunkStart, chunkEnd - chunkStart
#             if chunkEnd > fileEnd:
#                 break

# def calculaBufferCorta(arquivo, numPartes):
#     '''
#     corta em partes para multiprocessar o arquivo
#
#     baseDados: um txt com n linhas o qual será dividido em numPartes partes
#     '''
#     baseDados = gzopen(arquivo, 'rt')
#     # numLinhasBase = len(baseDados.readline())
#     # print(numLinhasBase)
#     # baseCortada = list()
#     inicioLinhasBuffer = 0
#     fimLinhasBuffer =  NUMERO_LINHAS_NO_BUFFER
    # while(True):
    #         # cortaSubBuffer(baseDados, inicioLinhasBuffer, fimLinhasBuffer)
    #         try:
    #             iteratorParte = iter.islice(baseDados, inicio, fim)
    #             for linha in iteratorParte:
    #                 print(linha)
    #         except Exception as e:
    #             print('nao deu certo')
    #             exit(123)

    #     baseDados.bu
    # for fimParte in range(inicio+numPartes, numLinhasBase, numPartes):
    #     print(inicio, fimParte)
    #     # cortaSubBuffer(baseDados, inicio, fim)
    #     inicio = fimParte


# def cortaSubBuffer(arquivo, inicio, fim):
#     # abre o arquivo sem descomprimir tudo
#     for linha in iter.islice(baseDados, inicio, fim):
#         print(linha)





#lixoooo

        #le numeroDeProcessos linhas e manda executar
        # baseDadosIterator = iter(baseDados)
        # for linha in baseDados:
        # listaSaida = th.Queue()
        # i = 1
        # # lista = []
        # for linha in baseDados:
        #     # fazer n threads e lançar
        #     saida.write(str(leSubarquivos(str(linha), listaSaida)))


        #     if(i % NUMERO_PROCESSOS_POR_VEZ == 0):
        #         for one_process in processes:
        #                 print(i,'----', linha )
        #                 saida.write(listaSaida.get())
        #                 one_process.join()
        #         # while not listaSaida.empty():
        #
        #     # lista.append(linha)
        #     processo = mp.Process(target=leSubarquivos, args=(str(linha), listaSaida))
        #     processes.append(processo)
        #     processo.start()
        #     #problema aquiiii no start TEM muitooo
        #
        #     i+=1
        # for one_process in processes:
        #         one_process.join()
        # while not listaSaida.empty():
        #         saida.write(listaSaida.get())




        # for linha in baseDados:
        #
        #     print(linha)
        #     i=0
        #     while(i < NUMERO_PROCESSOS_POR_VEZ):
        #         try:
        #             processo = mp.Process(target=leSubarquivos, args=(str(linha), listaSaida))
        #             processes.append(processo)
        #             processo.start()
        #             linha = next(baseDados)
        #             i+=1
        #         except Exception as e:
        #             for one_process in processes:
        #                 one_process.join()
        #             while not listaSaida.empty():
        #                 saida.write(listaSaida.get())
        #             return

            #         jobs.append(pool.apply_async(leSubarquivos,(linha, saida)))
            #         # leSubarquivos(linha)
            #         linha = next(linha)
            #         i+=1
            # else:
            #     # if k == NUMERO_PROCESSOS_POR_VEZ-1:
            #     for one_process in processes:
            #         one_process.join()
            #     while not listaSaida.empty():
            #         saida.write(listaSaida.get())

                # for saida in listaSaida:
                #     saida.write(str(saida))
                # listaSaida.clear()


            # leSubarquivos(linha) # primeiro processo
            # for i in range(NUMERO_PROCESSOS_POR_VEZ):
            #     leSubarquivos(baseDados.next()) # n-1 processos
