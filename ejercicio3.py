def lista_1(valor_inicio,valor_fin,incremento):
    if valor_inicio >= valor_fin:
        print()
        return
    print(list(range(valor_inicio,valor_inicio+incremento,incremento)), end=' ')
    nuevo_valor = valor_inicio + incremento
    lista_1(nuevo_valor, valor_fin, incremento)



print('--Todos los numeros del 0 al 10:' )
lista_1(0,11,1)

print('--Todos los números del -10 al 0: ')
lista_1(-10,1,1)

print('--Todos los números pares del 0 al 20: ')
lista_1(0,21,2)

print('--Todos los números impares entre el -20 y el 0: ')
lista_1(-20,2,2)

print('--Todos los números múltiples de 5 del 0 al 50: ')
lista_1(0,51,5)
