def main():
    ''' teste da funcao maximo '''

    minha_lista = [23,74,634,89,35,3,964,345]
    maior_numero,indice = max_lista(minha_lista)

    print("O maior elemento é: ", maior_numero)
    print("O indice = ", indice)

def max_lista(lista):
    ''' (list) -> int, int
    recebe uma lista de inteiros e retorna o
    valor maximo da lista e o indice onde ele ocorre '''

    # ESCREVA A SUA FUNCAO
    maior = -1
    indice = -1

    for n in lista:
        print(n)


    return maior,indice
    

main()
