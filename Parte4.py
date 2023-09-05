#Questão 07 do arquivo

def ordenar_pivo(vetor,menor,maior):

    m=menor-1

    aux=0

    for n in range(menor,maior):
        
        if vetor[n]>=vetor[maior]:
            m+=1

            aux=vetor[m]
            vetor[m]=vetor[n]
            vetor[n]=aux

    m+=1

    aux=vetor[maior]
    vetor[maior]=vetor[m]
    vetor[m]=aux

    return m

def qsort(vetor,menor,maior):
    if menor<maior:

        pivo=ordenar_pivo(vetor,menor,maior)

        qsort(vetor,menor,pivo-1)

        qsort(vetor,pivo+1,maior)

def eh_permutacao(vetor1,vetor2):

    #organizando os 2 vetores
    qsort(vetor1,0,len(vetor1)-1)
    qsort(vetor2,0,len(vetor2)-1)

    #booleana que diz se é uma permutação

    permutacao=True
    i=0

    while permutacao==True and i<len(vetor1):

        #se ouver um elemento diferente entre os 2 vetores organizados, eles não são permutações, logo, permutaçao=False
        if vetor1[i]!=vetor2[i]:
            permutacao=False

        i+=1
    
    if permutacao==False:
        print("Não são permutações")
    else:
        print("São permutações")

#Demonstração do algortimo
vetor1=[1,2,3,4,5]
vetor2=[5,4,3,2,1]

eh_permutacao(vetor1,vetor2)

#No melhor caso, assim como no caso médio, esse algoritmo tem complexidade o(n), ou seja, operará em tempo linear, no pior caso, ele terá complexidade o(n^2), operando em tempo quadrático
