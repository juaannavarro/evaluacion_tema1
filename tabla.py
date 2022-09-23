#ejercicio 4

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


