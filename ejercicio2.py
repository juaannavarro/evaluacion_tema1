
cadena = str(input("Introduce una cadena: " ))
correcto = [3, 4, 5, 6, 7, 8, 9]
class verificar:
    def __init__(self, cadena):
        self.cadena = cadena

    def cadenaOK(self):
        if cadena == correcto:
            print("True")
        else:
            print("False")

verificacion = verificar(cadena)
print(verificacion.cadenaOK)
        
