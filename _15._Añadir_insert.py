#31- Añade a la siguiente lista los colores 'magenta' y 'turquesa' utilizando insert().
# Tendrás que posicionar 'magenta' en la posición siguiente a la de 'lila' y 'turquesa' en la penúltima posición.
# Deberás hacer esto utilizando posiciones de lista negativa

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
#creamos lista colores

colores.insert(-4,'magenta') #añadimos el color con el parametro de la posicion
colores.insert(-1,'turquesa') #añadimos usando numeros negativos

print(colores) #mostramos lista actualizada
