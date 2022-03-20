#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_

#Crea un bucle while que se ejecute hasta que x valga 15 con incrementos de 5.
print("primer ciclo")
x = 0
while x <= 15: #se ejecuta el ciclo mientras x sea menor o igual a 15
    print(x)
    x += 5 #incremento
print("\n\n")

#Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20.
print("segundo ciclo")
x = 0
while x >= -100: #se ejecuta el ciclo mientras x sea mayor o igual a -100
    print(x)
    x -= 20 #decremento
print("\n\n")

#Crea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1 y que muestre en cada
#ejecución esta frase con el valor de ejecución correspondiente: 'El valor del bucle es 10'..
x = 10
while x >= 0:
    print('El valor del bucle es ' + str(x)) #imprimimos convirtiendo el tipo de dato de 'x' a string
    x -= 1 #decremento