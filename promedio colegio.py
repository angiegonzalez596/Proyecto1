
nombre = input("Cual es tu nombre ")
calificacion_bio = int(input("Cual es tu calificación en Biología %s?" % nombre))
calificacion_mate = int(input("cual es tu calificacion en matematicas " + nombre + " " ))
calificacion_quim = int (input("Cual es tu calificacion en Quimica " + nombre + " " ))


suma = calificacion_bio + calificacion_mate + calificacion_quim 
promedio = suma / 3
promedio = int(promedio)

if promedio >= 50:
    print ("Aprobaste con un promedio de: " + str(promedio))


else:
    print ("Tu promedio es: " + str(promedio) + " Recuperas")


print ("Fin")     
    
