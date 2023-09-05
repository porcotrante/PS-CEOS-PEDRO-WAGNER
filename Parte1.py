#Essa parte engloba as 4 primeiras tarefas em um só arquivo
import numpy

#Função para ler matriz
def lermatriz(arquivo):
    vetoraux=[]
    matriz=[]

    #Contadores de linhas e colunas
    linhas=0
    colunas=0

    #A variavel Leitura recebe o arquvio em formato de string
    leitura=arquivo.read()

    #A as barras são removidas da matriz
    leitura=leitura.split("|")
    n=len(leitura)

    for i in range(n):

        #Se o elemento for numérico, ele é colocado no vetor auxiliar e o contator de colunas é incrementado
        if leitura[i].isnumeric():
            vetoraux.append(leitura[i])
            colunas+=1

        #se uma quebra de linha for lida, o vetor auxiliar é adicionado na matriz e depois é esvaziado e o contador de linhas é aumentado
        elif leitura[i]=='\n' or i==n-1:
            linhas+=1
            matriz.append(vetoraux)
            vetoraux=[]
    
    #por fim, o contador de colunas recebe colunas/linhas, como foram contabilizados todos os elementos da matriz no contador, a divisão será inteira
    colunas=int(colunas/linhas)

    #A função retorna a matriz (na forma de uma array do numpy), o seu número de linhas e o seu número de colunas
    return (numpy.array(matriz),linhas,colunas)

#Função que identifica os elementos repetidos da matriz e os substitui por 0
def repeticao(matriz,linhas,colunas):

    #transformando a matriz em um vetor para trabalhar com ele
    vetor=matriz.flatten()
    s=set()

    #se um elemento do vetor estiver no set, ele virará 0, se não, será adicionado
    for i in range(len(vetor)):
        if vetor[i] in s:
            vetor[i]=0

        s.add(vetor[i])
    
    #reconstruindo a matriz com os novos elementos
    matriz=numpy.reshape(vetor,(linhas,colunas))
    return matriz

#Função que imprime a matriz
def printmatriz(matriz,colunas):

    #transformando a matriz em vetor
    vetor=matriz.flatten()

    #variável que conta as colunas
    countcoluna=0

    #printa os elementos da matriz, quando o contador de colunas for um múltiplo do número de colunas da matriz, o programa printa \n
    for i in range(len(vetor)):
        print("|%d|"%int(vetor[i]),end="")
        countcoluna+=1
        if countcoluna%colunas==0:
            print("\n",end="")


#Demonstração do algoritmo
with open("matriz.txt","r") as arquivo:
    (matriz,linhas,colunas)=lermatriz(arquivo)
    print(matriz)
    matriz=repeticao(matriz,linhas,colunas)
    printmatriz(matriz,colunas)


