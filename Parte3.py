#Questão 06 do arquivo

def ordenar_pivo(vetor,menor,maior,ordem):

    m=menor-1

    aux=0

    for n in range(menor,maior):

        #se a variavel ordem for igual a 0, o algoritmo ordenará em ordem crescente, se for 1, será em ordem decrescente
        if ordem==0:
            if vetor[n]<=vetor[maior]:
                m+=1

                aux=vetor[m]
                vetor[m]=vetor[n]
                vetor[n]=aux

        elif ordem==1:
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

def qsort(vetor,menor,maior,ordem):
    if menor<maior:

        pivo=ordenar_pivo(vetor,menor,maior,ordem)

        qsort(vetor,menor,pivo-1,ordem)

        qsort(vetor,pivo+1,maior,ordem)

def organizar_vetores(vetor1,vetor2):

    #organizando o primeiro vetor em ordem decrescente
    qsort(vetor1,0,len(vetor1)-1,1)

    #organizando o segundo vetor em ordem crescente
    qsort(vetor2,0,len(vetor2)-1,0)

    aux=0
    for i in range(len(vetor1)):
        #se algum elemento do vetor1 for maior do que o elemento de mesmo índice no vetor 2, eles são trocados
        if vetor1[i]>vetor2[i]:

            aux=vetor1[i]
            vetor1[i]=vetor2[i]
            vetor2[i]=aux

    print("vetor dos menores:",vetor1)

    print("vetor dos maiores:",vetor2)

#Demonstração do algoritmo
vetor1=[12,47,13,41,8]

vetor2=[44,32,21,49,10]

organizar_vetores(vetor1,vetor2)
