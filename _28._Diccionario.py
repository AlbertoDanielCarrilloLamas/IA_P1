#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_

#Del diccionario teclado2 del capítulo, muestra los elementos Modelo y Precio con presentación en un print().
# El resultado será esto en la consola: El modelo Corsair K55 RGB cuesta 59,99 $.

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro', #declaracion de teclado 1
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',     #declaracion teclado 2
	'Precio': '59,99'
}

consulta1 = teclado2["Modelo"] #almacenamos la prier consulta
consulta2 = teclado2["Precio"] ##amacenamos la segunda
print("El modelo " + consulta1 + " cuesta " + consulta2 + " $ .") #imprimimos la info
