#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_

#Elimina el diccionario teclado1 entero . De teclado2 elimina las claves 'Categoría' y 'Precio'. 
#Muestra la última clave ('Modelo') que queda en la consola.

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclado1 #eliminamos todo el diccionario 1

del teclado2["Categoría"] #eliminamos con metodo 'del'
teclado2.pop("Precio")    #eliminamos con metodo 'pop'
print(teclado2) #imprimimos lo restante del diccionario con print

#abajo mostramos lo mismo pero con un ciclo for
for x, y in teclado2.items():
	print(x, ": ", y)
