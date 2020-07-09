#ejercicio "escriba un numero"

def es_numerico(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False

esvalido = True

while esvalido:
    numero = input("Ingrese un Numero")

    if es_numerico(numero):
        print ("Ha digitado un valor valido")
        esvalido = False 
       
    else:
        print ("El valor digitado no corresponde a un numero")

