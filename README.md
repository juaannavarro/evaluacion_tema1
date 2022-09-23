# evaluacion_tema1

Para hacer esta tarea hemos creado el siguiente lin para acceder al repositorio: https://github.com/juaannavarro/evaluacion_tema1


Ejercicio 1

La siguiente matriz (o lista con listas anidadas) debe cumplir una condición, y es que en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?

Ayuda

La función llamada sum(lista) devuelve una suma de todos los elementos de la lista ¡Pruébalo!

matriz = [

    [1, 1, 1, 3],

    [2, 2, 2, 7],

    [3, 3, 3, 9],

    [4, 4, 4, 13]

]

 CÓDIGO:
 ``` 
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

``` 


Ejercicio 2

Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False).

CÓDIGO:

```
def evalua_cadena(c):
    if (len(cadena)>=3 and len(cadena)<10):
        return True
    else:
        return False

cadena = input('Introduzca una cadena: ')

resultado = evalua_cadena(cadena)
print(resultado)

```



Ejercicio 3

Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

·        Todos los números del 0 al 10 [0, 1, 2, ..., 10]

·        Todos los números del -10 al 0 [-10, -9, -8, ..., 0]

·        Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]

·        Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]

·        Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

Concepto útil

Se pueden generar saltos en el range() estableciendo su tercer parámetro range(inicio, fin, salto), experimenta.


CÓDIGO:

```
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

```



Ejercicio 4

Crea un script llamado tabla.py que realice las siguientes tareas:

·        Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.

·        El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.

·        En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.

·        El script contendrá un bucle for que itere el número de veces del primer argumento.

·        Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.

·        Dentro del segundo for ejecuta una instrucción print(" * ", end=''), (**end=''* evita el salto de línea)*.

·        Ejecuta el código y observa el resultado.

·        Intenta deducir dónde y cómo añadir otra instruccion print() para dibujar una tabla.

CÓDIGO:

```

from pickle import TRUE
from warnings import catch_warnings

while True: 
    print("Introduce dos números enteros del 1 al 9: ")
    try:
        filas= int(input())
        columnas = int(input())
        print("filas", filas)
        print("columnas", columnas)
        if (filas > 1 and filas < 9 and columnas > 1 and columnas < 9):
            break
        else:
            print("Error, el valor introducido no cumple la condición")
    except ValueError:
        print("Error, el valor introducido no cumple la condición")
        continue

for f in range(filas):
    print("*", end="")
    for c in range(columnas):
        if (c<columnas-1):
            print("*", end="")
        else:
            print()


```


