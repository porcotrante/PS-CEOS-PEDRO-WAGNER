#Questão 05 do arquivo

def ordenar_pivo(vetor,menor,maior):

    #setando um dos índicies que vão ser utilizados
    m=menor-1

    aux=0

    for n in range(menor,maior):
        
        #se o elemento for maior do que o pivô, incrementamos o índice m e trocamos o elemento vetor[m] com o elemento vetor[n]
        if vetor[n]>=vetor[maior]:
            m+=1

            aux=vetor[m]
            vetor[m]=vetor[n]
            vetor[n]=aux

    m+=1

    #por fim, colocamos o pivô na posição certa
    aux=vetor[maior]
    vetor[maior]=vetor[m]
    vetor[m]=aux

    return m

def qsort(vetor,menor,maior):
    if menor<maior:

        #fazemos o primeito pivô e conseguimos a posição dele, depois, fazemos o lado esquerdo e direito do pivô recursivamente
        pivo=ordenar_pivo(vetor,menor,maior)

        qsort(vetor,menor,pivo-1)

        qsort(vetor,pivo+1,maior)

#demonstração do algoritmo
vetor=[9,8,10,-5,3,7,21]

qsort(vetor,0,len(vetor)-1)

print("O terceiro maior elemento do vetor é",vetor[2])

#No caso médio, assim como o melhor caso, esse algoritmo tem complexidade o(n*logn), no pior caso, ele tem complexidade o(n^2)