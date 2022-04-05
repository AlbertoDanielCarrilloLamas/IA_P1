#!/usr/bin/env python
# * coding: cp1252 *
# * cdoing: 850 *
# * coding: utf-8 *

# ¿Cuál es el MINIMO # de carreras se necesitan para obtener a los 2 caballos más rápidos?... si...
# Se tienen 25 caballos. y por carrera se pueden correr solamente 5 caballos, no más no menos.
# Programa en Python entregando de manera aleatoria la velocidad de cada caballo en la escala que usted prefiera.
# Parte gráfica, realizar el Gráfo de caballos mostrando los resultados después de analizarlos. 
# Dar el mínimo de carreras y realizar la inferencia final para la organización.


import random
from networkx.utils.decorators import nodes_or_number
import numpy as np
from numpy.core.numeric import array_equiv
import matplotlib.pyplot as plt
import networkx as nx

c1 = random.uniform(1,100)
c2 = random.uniform(1, 100)
c3 = random.uniform(1, 100)
c4 = random.uniform(1, 100)
c5 = random.uniform(1, 100)
c6 = random.uniform(1, 100)
c7 = random.uniform(1, 100)
c8 = random.uniform(1, 100)
c9 = random.uniform(1, 100)
c10 = random.uniform(1, 100)
c11 = random.uniform(1, 100)
c12 = random.uniform(1, 100)
c13 = random.uniform(1, 100)
c14 = random.uniform(1, 100)
c15 = random.uniform(1, 100)
c16 = random.uniform(1, 100)
c17 = random.uniform(1, 100)
c18 = random.uniform(1, 100)
c19 = random.uniform(1, 100)
c20 = random.uniform(1, 100)
c21 = random.uniform(1, 100)
c22 = random.uniform(1, 100)
c23 = random.uniform(1, 100)
c24 = random.uniform(1, 100)
c25 = random.uniform(1, 100)

print("Los caballos correran en 5 hits de 5 caballos cada uno y sus tiempos se guardaran en una matriz de la siguiente manera: ")
print("\t[c1,c2,c3,c4,c5,]\n\t[c6,c7,c8,c9,c10]\n\t[c11,c12,c13,c14,c15]\n\t[c16,c17,c18,c19,c20]\n\t[c21,c22,c23,c24,c25]")


caballos = np.array([[c1,c2,c3,c4,c5,], [c6,c7,c8,c9,c10], [c11,c12,c13,c14,c15], [c16,c17,c18,c19,c20], [c21,c22,c23,c24,c25]])

tiempos = np.array([[c1,c2,c3,c4,c5,], [c6,c7,c8,c9,c10], [c11,c12,c13,c14,c15], [c16,c17,c18,c19,c20], [c21,c22,c23,c24,c25]])
print("\nTiempos registrados por cada caballo al terminar las 5 carreras: ")
print(tiempos)


print("\nOrdenamos los resultados dejando los gaadores de cada carrera hasta la izquierda: ")
tiempos.sort() #cada fila representa los tiempos de una carrera y dejamos los mas rapidos a la izquierda
print(tiempos)

print("\n Resultados de la Carrera entre los primeros 5 ganadores (carrera 6): ")
carrera6 = [tiempos[0,0], tiempos[1,0], tiempos[2,0], tiempos[3,0], tiempos[4,0] ]
carrera6.sort() #creamos la carrera 6 con los 5 ganadores y los ponemos a correr de nuevo
print(carrera6)

for x in range(5):
    for y in range(5):
        if carrera6[0] == caballos[x][y]:
            winner = (x*5) + (y*1) +1
            i = x # i Almacena la fila en la que se encuentra el caballo ganador
print("\n\tEl caballo más rapido es el caballo numero: " + str(winner) + " con un tiempo de: " + str(carrera6[0]))

# para buscar al segundo más rapido, omitimos al caballo ganador y eliminamos a todos los demas caballos que hayan sido superados en tiempo por al menos otro caballo. Por lo que nos quedan los 4 caballos ganadores de sus respectivos hits (carreras de 5) y el segundo lugar del hit del caballo ganador
carrera7 = [tiempos[i,1], carrera6[1], carrera6[2], carrera6[3], carrera6[4] ]
carrera7.sort()
print("\n\nResultados carrera 7: ")
print(carrera7)
for x in range(5):
    for y in range(5):
        if carrera7[0] == caballos[x][y]:
            winner2 = (x*5) + (y*1) +1
print("\n\tEl segundo caballo más rapido es el caballo numero: " + str(winner2) + " con un tiempo de: " + str(carrera7[0]))

print("\n\n\t El numero minimo de carrera necesitadas para descubrir a los dos más rapidos son 7\n")

#Grafica
fig, grafica = plt.subplots()
grafica.bar(["C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","C11","C12","C13","C14","C15","C16","C17","C18","C19","C20","C21","C22","C23","C24","C25"], [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25])
grafica.set_title("Tiempo registrado por cada caballo durante la carrera (maximizar ventana)", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})
grafica.set_xlabel("Numero de caballo")
grafica.set_ylabel("Tiempo (en segundos)")
plt.show()

#Grafo
Grafo = nx.Graph() # creamos un grafo y añadimos nodos
Grafo.add_node("Winner")
Grafo.add_node("winner 2")

Grafo.add_node("sub1")
Grafo.add_node("sub2")
Grafo.add_node("sub3")
Grafo.add_node("sub4")
Grafo.add_node("sub5")

Grafo.add_nodes_from(["sub1.1", "sub1.2", "sub1.3"])
Grafo.add_nodes_from(["sub2.1", "sub2.2", "sub2.3"])
Grafo.add_nodes_from(["sub3.1", "sub3.2", "sub3.3", "sub3.4"])
Grafo.add_nodes_from(["sub4.1", "sub4.2", "sub4.3", "sub4.4"])
Grafo.add_nodes_from(["sub5.1", "sub5.2", "sub5.3", "sub5.4"])

#Añadir aristas
Grafo.add_edge("Winner", "winner 2")

Grafo.add_edge("winner 2", "sub1")
Grafo.add_edge("winner 2", "sub2")
Grafo.add_edge("winner 2", "sub3")
Grafo.add_edge("winner 2", "sub4")
Grafo.add_edge("winner 2", "sub5")

Grafo.add_edges_from([("sub1", "sub1.1"),("sub1", "sub1.2"), ("sub1", "sub1.3")])
Grafo.add_edges_from([("sub2", "sub2.1"),("sub2", "sub2.2"), ("sub2", "sub2.3")])
Grafo.add_edges_from([("sub3", "sub3.1"),("sub3", "sub3.2"), ("sub3", "sub3.3"), ("sub3", "sub3.4")])
Grafo.add_edges_from([("sub4", "sub4.1"),("sub4", "sub4.2"), ("sub4", "sub4.3"), ("sub4", "sub4.4")])
Grafo.add_edges_from([("sub5", "sub5.1"),("sub5", "sub5.2"), ("sub5", "sub5.3"), ("sub5", "sub5.4")])

#graficar gafo
nx.draw(Grafo, node_size = 50, width = 0.3, with_labels=False)
plt.show() #mostramos grafo

