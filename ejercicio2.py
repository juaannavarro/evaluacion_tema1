def evalua_cadena(c):
    if (len(cadena)>=3 and len(cadena)<10):
        return True
    else:
        return False

cadena = input('Introduzca una cadena: ')

resultado = evalua_cadena(cadena)
print(resultado)
