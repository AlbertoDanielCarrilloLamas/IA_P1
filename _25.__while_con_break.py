
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_

#Crea un bucle while con las siguientes características:
#El valor inicial de la variable x será de 0.
#El valor de incremento será 1.
#La condición de salida del bucle será mayor o igual a 30.
#La ejecución se deberá romper cuando x valga 15.
#Debes imprimir la siguiente frase cada vez que se ejecute el bucle: 'El valor del bucle es: ' + x.
#Debes saltarte las ejecuciones con valor de x en 4, 6 y 10.
#En cada salto de ejecución, deberás mostrar los valores saltado con este mensaje: 'Se saltó el valor ' + x ' de x'.
#Cuando se rompa la ejecución del bucle deberás mostrar un mensaje indicándolo: 'Se rompió la ejecución del bucle cuando x valía ' + x.

x = 0
while x < 30: #se ejecuta el bucle mientras 'x' sea menor a 30
    x += 1 #incremento de 1
    if x == 4 or x == 6 or x == 10: #cuando 'x' valga 4 o 6 o 10 entrara a la condicion
        print("Se salto el valor " + str(x)) #imprime que se saltará el valor de x 
        continue #salta al inicio del ciclo
    if x == 15:
        print("se rompio la ejecucion del bucle cuando x valia " + str(x)) 
        break #break termina toda la ejecucion del ciclo
    print("El valor del bucle es: " + str(x)) #imprime el valor de 'x' en caso de que sea diferente de 4,6,10,15
    