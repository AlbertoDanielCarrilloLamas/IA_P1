#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_

#Haz una tupla que contenga cuatro colores de tu elecci�n. Tendr�s que poner una condici�n con el condicional
# if para cada color que le avise al usuario que el color est� en la tupla con un mensaje como este: 
# print('El color rojo est� admitido') y una condici�n False para contemplar cualquier color que no est� en
# la tupla con un mensaje como este: print('Color no admitido'). No puedes utilizar el operador ==. Adem�s
# tendr�s que hacer esto con un input() que permita introducir un color al usuario.

colores = ('azul','blanco','rojo','verde') #creamos tupla

color = input("introduce un color. ") #pedimos el color al usuario

if color in colores: #verificamos si el color est� en la tupla
    print("El color " + color + " est� admitido") #si est�, imprimimos con el color introducido por el usuario
else:
    print("Color no admitido") #sino est�, imprimimos sin el color introducido

