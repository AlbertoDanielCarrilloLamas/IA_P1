#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_

#Haz una tupla que contenga cuatro colores de tu elección. Tendrás que poner una condición con el condicional
# if para cada color que le avise al usuario que el color está en la tupla con un mensaje como este: 
# print('El color rojo está admitido') y una condición False para contemplar cualquier color que no esté en
# la tupla con un mensaje como este: print('Color no admitido'). No puedes utilizar el operador ==. Además
# tendrás que hacer esto con un input() que permita introducir un color al usuario.

colores = ('azul','blanco','rojo','verde') #creamos tupla

color = input("introduce un color. ") #pedimos el color al usuario

if color in colores: #verificamos si el color está en la tupla
    print("El color " + color + " está admitido") #si está, imprimimos con el color introducido por el usuario
else:
    print("Color no admitido") #sino está, imprimimos sin el color introducido

