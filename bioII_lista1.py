''' Aprendendo a plotar gráficos a partir de arquivos csv '''

import matplotlib.pyplot as plt  #importa biblioteca de plotação

def recebe_arq(arq):
    dados = []
    dados_edit = []
    arquivo = open(arq, 'r')
    for linha in arquivo:
        line = list(map(str,linha.split()))
        dados.append(line)  
    print(dados)
    for linha in dados:
        dados_edit.append(list(map(int,linha.split(' '))))
    
    matriz = []
    for dado in dados_edit[1:82]:
        matriz.append(dado)
        
    return d

dado = recebe_arq("trajetorias.csv")
print(dado)

        

