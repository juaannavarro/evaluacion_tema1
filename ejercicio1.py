matriz = [

    [1, 1, 1, 3],

    [2, 2, 2, 7],

    [3, 3, 3, 9],

    [4, 4, 4, 13]

]

def modificar_suma(matriz, index):
    if len(matriz[0]) == index:
        return
    lista = matriz[index]
    l = lista[0:3]
    valor = sum(l)
    matriz[index][3] = valor
    print(matriz[index])
    index += 1
    modificar_suma(matriz,index)

modificar_suma(matriz, 0)
print(matriz)

