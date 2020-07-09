print ("Sistema para calcular el promedio de un alumno")

nombre =input ("Cual es tu nombre?: ")

mate = int(input(nombre + " Cual es tu Calificacion de Matematicas?: "))
quimica = int (input(nombre + " Cual es tu calificacion de Quimica?: "))
biologia = int (input(nombre + " Cual es tu calificacion de Biologia?: "))

promedio = (mate + quimica + biologia) / 3
promedio = int(promedio)

if promedio >= 5:
    print ('Felicidades ' + nombre + ' "Aprobaste" con un promedio de: ', promedio)

print ("Fin")




    
    
    
