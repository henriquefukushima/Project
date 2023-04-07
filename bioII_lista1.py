''' Aprendendo a plotar gráficos a partir de arquivos csv '''

'''''
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

'''''
import matplotlib.pyplot as plt
import csv 
import numpy as np
'''''
for linha in movimentos:
      print(linha)
'''''
# Questão 2
# (a) Usando 80 intervalos entre os valores de -180° e 180°, obtenha os seguintes gráficos para o ângulo theta e para os dois diedrais phi:

# (i) Histograma dos valores

# Histograma dos valores de theta entre os átomos do resíduo Phe-11

def histograma(movimentos, residuo):

    bins = [-180, -175.5, -171.0, -166.5, -162.0, -157.5, -153.0, -148.5, -144.0, -139.5, -135.0, -130.5, -126.0, -121.5, -117.0, -112.5, -108.0, -103.5, -99.0, -94.5, -90.0, -85.5, -81.0, -76.5, -72.0, -67.5, -63.0, -58.5, -54.0, -49.5, -45.0, -40.5, -36.0, -31.5, -27.0, -22.5, -18.0, -13.5, -9.0, -4.5, 0.0, 4.5, 9.0, 13.5, 18.0, 22.5, 27.0, 31.5, 36.0, 40.5, 45.0, 49.5, 54.0, 58.5, 63.0, 67.5, 72.0, 76.5, 81.0, 85.5, 90.0, 94.5, 99.0, 103.5, 108.0, 112.5, 117.0, 121.5, 126.0, 130.5, 135.0, 139.5, 144.0, 148.5, 153.0, 157.5, 162.0, 166.5, 171.0, 175.5, 180]
    if residuo == "P":
        theta_list = []
        for linha in movimentos:
            theta_list.append(linha[1])
        counts, bin_edges, patches = plt.hist(theta_list, bins, density = True)
        for i, count in enumerate(counts):
            print(f"Bin {i}: {count}")
        print(counts)
        plt.title("Histograma de valores de \u03B8 entre os átomos C\u03B1-C\u03B2-C\u03B3 do resíduo Phe-11")
        plt.ylabel("Frequência")
        plt.xlabel("Ângulo \u03B8")
        plt.show()
        return counts
    
    elif residuo == "G":
        theta_list = []
        for linha in movimentos:
            theta_list.append(linha[2])
        plt.hist(theta_list, bins)
        plt.title("Histograma de valores do ângulo diedral \u03A6 do resíduo Glu-10")
        plt.ylabel("Frequência")
        plt.xlabel("Ângulo \u03A6")
        plt.show()

        theta_list2 = []
        for linha in movimentos:
            theta_list2.append(linha[3])
        plt.hist(theta_list2, bins)
        plt.title("Histograma de valores do ângulo diedral \u03A8 do resíduo Glu-10")
        plt.ylabel("Frequência")
        plt.xlabel("Ângulo \u03A8")
        plt.show()
    
    elif residuo == "L":
        theta_list = []
        for linha in movimentos:
            theta_list.append(linha[4])
        plt.hist(theta_list, bins)
        plt.title("Histograma de valores do ângulo diedral \u03A6 do resíduo Leu-33")
        plt.ylabel("Frequência")
        plt.xlabel("Ângulo \u03A6")
        plt.show()

        theta_list2 = []
        for linha in movimentos:
            theta_list2.append(linha[5])
        plt.hist(theta_list2, bins)
        plt.title("Histograma de valores do ângulo diedral \u03A8 do resíduo Leu-33")
        plt.ylabel("Frequência")
        plt.xlabel("Ângulo \u03A8")
        plt.show()

def media(movimentos, residuo):
    soma = 0
    soma2 = 0
    n = len(movimentos)
    if residuo == 'P':
        for linha in movimentos:
            soma += linha[1]
        media = soma/n
        return media
    elif residuo == 'G':
        for linha in movimentos:
            soma += linha[2]
            soma2 += linha[3]
        media = soma/n
        media2 = soma2/n
        return media, media2
    if residuo == 'L':
        for linha in movimentos:
            soma += linha[4]
            soma2 += linha[5]
        media = soma/n
        media2 = soma2/n
        return media, media2
    
def variancia(movimentos, residuo):
    theta_list = []
    theta_list2 = []
    var = 0
    var2 = 0
    n = len(movimentos)
    if residuo == "P":
        m = media(movimentos,residuo)
        for theta in movimentos:
            theta_list.append(theta[1])
        for item in theta_list:
            var += (item - m)**2
        var = var/n
        return var
    elif residuo == "G":
        m1, m2 = media(movimentos,residuo)
        for theta in movimentos:
            theta_list.append(theta[2])
        for item in theta_list:
            var += (item - m1)**2
        var = var/n
        for theta in movimentos:
            theta_list2.append(theta[3])
        for item in theta_list2:
            var2 += (item - m2)**2
        var2 = var2/n
        return var, var2
    elif residuo == "L":
        m1,m2 = media(movimentos,residuo)
        for theta in movimentos:
            theta_list.append(theta[4])
        for item in theta_list:
            var += (item - m1)**2
        var = var/n
        for theta in movimentos:
            theta_list2.append(theta[5])
        for item in theta_list2:
            var2 += (item - m2)**2
        var2 = var2/n
        return var, var2

def desvio_padrao(movimentos, residuo):
    if residuo == "P":
        var = variancia(movimentos,residuo)
        dp = (var)**(1/2)
        return dp 
    elif residuo == "G" or residuo =="L":
        var1, var2 = variancia(movimentos,residuo)
        dp1 = (var1)**(1/2)
        dp2 = (var2)**(1/2)
        return dp1, dp2

def dens(movimentos, residuo):

    pi = 3.141592653589793238462643383279502884
    e = 2.718281828459045
    x = [-180, -175.5, -171.0, -166.5, -162.0, -157.5, -153.0, -148.5, -144.0, -139.5, -135.0, -130.5, -126.0, -121.5, -117.0, -112.5, -108.0, -103.5, -99.0, -94.5, -90.0, -85.5, -81.0, -76.5, -72.0, -67.5, -63.0, -58.5, -54.0, -49.5, -45.0, -40.5, -36.0, -31.5, -27.0, -22.5, -18.0, -13.5, -9.0, -4.5, 0.0, 4.5, 9.0, 13.5, 18.0, 22.5, 27.0, 31.5, 36.0, 40.5, 45.0, 49.5, 54.0, 58.5, 63.0, 67.5, 72.0, 76.5, 81.0, 85.5, 90.0, 94.5, 99.0, 103.5, 108.0, 112.5, 117.0, 121.5, 126.0, 130.5, 135.0, 139.5, 144.0, 148.5, 153.0, 157.5, 162.0, 166.5, 171.0, 175.5, 180]
    X = np.arange(-180,180,1)
    if residuo == "P":
        dp = desvio_padrao(movimentos, residuo)
        m = media(movimentos, residuo)
        y = ((((2*pi)**(1/2))*dp )**(-1)) *np.exp(-(((X - m)**2)/(2*(dp**2))))
        plt.plot(X, y)
        plt.title("Densidade de probabilidade normalizada para valores de \u03B8 entre os átomos C\u03B1-C\u03B2-C\u03B3 do resíduo Phe-11")
        plt.ylabel("Densidade de probabilidade")
        plt.xlabel("Ângulo \u03B8")
        plt.show()
    elif residuo == "G":
        dp1, dp2 = desvio_padrao(movimentos, residuo)
        m1, m2 = media(movimentos, residuo)
        y1 = ((((2*pi)**(1/2))*dp1 )**(-1)) *np.exp(-(((X - m1)**2)/(2*(dp1**2))))
        plt.plot(X, y1)
        plt.title("Densidade de probabilidade normalizada para valores do ângulo diedral \u03A6 do resíduo Glu-10")
        plt.ylabel("Densidade de probabilidade")
        plt.xlabel("Ângulo \u03A6")
        plt.show()

        y2 = ((((2*pi)**(1/2))*dp2 )**(-1)) *np.exp(-(((X - m2)**2)/(2*(dp2**2))))
        plt.plot(X, y2)
        plt.title("Densidade de probabilidade normalizada para valores do ângulo diedral \u03A8 do resíduo Glu-10")
        plt.ylabel("Densidade de probabilidade")
        plt.xlabel("Ângulo \u03A8")
        plt.show()
    elif residuo == "L":
        dp1, dp2 = desvio_padrao(movimentos, residuo)
        m1, m2 = media(movimentos, residuo)
        y1 = ((((2*pi)**(1/2))*dp1 )**(-1)) *np.exp(-(((X - m1)**2)/(2*(dp1**2))))
        plt.plot(X, y1)
        plt.title("Densidade de probabilidade normalizada para valores do ângulo diedral \u03A6 do resíduo Leu-33")
        plt.ylabel("Densidade de probabilidade")
        plt.xlabel("Ângulo \u03A6")
        plt.show()

        y2 = ((((2*pi)**(1/2))*dp2 )**(-1)) *np.exp(-(((X - m2)**2)/(2*(dp2**2))))
        plt.plot(X, y2)
        plt.title("Densidade de probabilidade normalizada para valores do ângulo diedral \u03A8 do resíduo Leu-33")
        plt.ylabel("Densidade de probabilidade")
        plt.xlabel("Ângulo \u03A8")
        plt.show()


'''''
# Criando uma lista de 80 intervalos entre -180 e 180 graus
i = -180
list = []
while i != 180:
     list.append(i)
     i += 4.5
print(list)
[-180, -175.5, -171.0, -166.5, -162.0, -157.5, -153.0, -148.5, -144.0, -139.5, -135.0, -130.5, -126.0, -121.5, -117.0, -112.5, -108.0, -103.5, -99.0, -94.5, -90.0, -85.5, -81.0, -76.5, -72.0, -67.5, -63.0, -58.5, -54.0, -49.5, -45.0, -40.5, -36.0, -31.5, -27.0, -22.5, -18.0, -13.5, -9.0, -4.5, 0.0, 4.5, 9.0, 13.5, 18.0, 22.5, 27.0, 31.5, 36.0, 40.5, 45.0, 49.5, 54.0, 58.5, 63.0, 67.5, 72.0, 76.5, 81.0, 85.5, 90.0, 94.5, 99.0, 103.5, 108.0, 112.5, 117.0, 121.5, 126.0, 130.5, 135.0, 139.5, 144.0, 148.5, 153.0, 157.5, 162.0, 166.5, 171.0, 175.5]
'''''

def main():

    # Formatação dos dados para float
    movimentos = []
    with open("trajetorias.csv") as csvfile:
            arquivo = csv.reader(csvfile)

            for linha in arquivo:
                new_list = [s.strip().replace(',', '').replace('\t', '') for s in linha]
                new_list = [float(x) for x in new_list]
                movimentos.append(new_list)

    # Questão: 

    questao = input("Digite a letra da questão: ")
    if questao == 'a':
        item = input("Digite o item da questão (a): ")
        if item == 'i':
            residuo = input("Histograma de Phe(P), Glu(G) ou Leu(L)? ")
            histograma(movimentos, residuo)
        elif item == 'ii':
            residuo = input("Histograma de Phe(P), Glu(G) ou Leu(L)? ")
            if residuo == "P":
                dp = desvio_padrao(movimentos, residuo)
                print(dp)
                dens(movimentos, residuo)
            elif residuo == "G":
                dp1, dp2 = desvio_padrao(movimentos, residuo)
                print(dp1, dp2)
                dens(movimentos, residuo)

            elif residuo == "L":
                dp1, dp2 = desvio_padrao(movimentos, residuo)
                print(dp1, dp2)
                dens(movimentos, residuo)
        
        elif item == 'iii':
            residuo = input("Repetir o item(a) para theta(P) ou phi de Glu-10(G)? ")
            if residuo == "P":
                histograma(movimentos[2251:], residuo)
            elif residuo == "G":
                histograma(movimentos[2251:], residuo)
    
    elif questao == "b":
        residuo1 = "P"
        residuo2 = "G"
        residuo3 = "L"
        m = media(movimentos, residuo1)
        var = variancia(movimentos, residuo1)
        print("Para o ângulo \u03B8:")
        print("Média = " + str(m))
        print("Variância = " + str(var))

        m1_G, m2_G = media(movimentos, residuo2)
        var1_G, var2_G = variancia(movimentos, residuo2)
        print("Para o ângulo diedral \u03A6 do Glu-10:")
        print("Média = " + str(m1_G))
        print("Variância = " + str(var1_G))
        print("Para o ângulo diedral \u03A8 do Glu-10:")
        print("Média = " + str(m2_G))
        print("Variância = " + str(var2_G))

        m1_L, m2_L = media(movimentos, residuo3)
        var1_L, var2_L = variancia(movimentos, residuo3)
        print("Para o ângulo diedral \u03A6 da Leu-33:")
        print("Média = " + str(m1_L))
        print("Variância = " + str(var1_L))
        print("Para o ângulo diedral \u03A8 da Leu-33:")
        print("Média = " + str(m2_L))
        print("Variância = " + str(var2_L))
    
    

'''''


    elif questao == 'c':
        item = input("Digite o item da questão (c): ")
'''''
main()