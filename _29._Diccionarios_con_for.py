#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_

#Itera el diccionario teclado1 con un solo bucle for que muestre esto en la consola:
#Categoría = Teclados.
#Modelo = HyperX Alloy FPS Pro.
#Precio = 89,99.

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',     #creacion dicciionario 1
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',         #creacion diccionario 2
	'Precio': '59,99'
}

for x, y in teclado1.items():#La funcion 'items()' obtiene los elementos del diccionario y ademas sus atributos
	print(x, ": ", y , ".") #mostramos en consola añadiendo presentacion con los puntos y espacios