#De la lista, elimina los colores 'azul', 'marrón', 'negro' y 'rosa'.
#Debes utilizar al menos una vez las posiciones negativas para eliminar un color. 
#Después, imprime la lista para ver los colores que se han eliminado.

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
#declaramos lista

del colores[1] #eliminamos el color azul
del colores[4] #eliminamos el marron
del colores[-4] #eliminamos negro
del colores[-3] #eliminamos rosa

print(colores)#imprimimos para comprobar las eliminaciones
