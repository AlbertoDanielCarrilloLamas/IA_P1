# Carrillo Lamas Alberto Daniel. 19310378. Implementacion de algoritmo Dijkstra.

#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
"""
datos = pd.read_csv('Nodos y caminos.csv') #importamos datos del archivo csv (creacion de dataframe) con ayuda de panda
datos.head() #mostramos dataframe

Rutas = nx.from_pandas_edgelist(datos,source='Origen',target='Destino',edge_attr='Longitud camino')#Creacion de grafica a partir de datos

Rutas.nodes() #mostramos nodos
Rutas.edges() #mostramos aristas
Rutas.order() #mostramos cantidad de nodos en grafo

djk_path=nx.dijkstra_path(Rutas, source='Casa',target='Pablo neruda',weight=True)
djk_path #indicamos origen y destino y con la funcion dijkstra_path encontramos la ruta de menos costo

mejor_ruta = Rutas.subgraph(['Casa', 'Base aerea', 'Real center', 'Trompo magico', 'Juan palomar','Estadio 3 de marzo','Pablo neruda','CETI']) #almacenamos la mejor ruta calculada
nx.draw(mejor_ruta,with_labels=True) #dibujamos la mejor ruta
plt.show() #mostramos grafo"""

#Grafo
Grafo = nx.Graph() # creamos un grafo y añadimos nodos

#Añadir aristas
# G.add_edge(2, 3, weight=0.9) /// a = random.randint(1,5)
e = [('Casa', 'Base aerea', random.randint(1,5)), ('Base aerea', 'Real center', random.randint(1,5)), ('Real center', 'Trompo magico', random.randint(1,5)), ('Trompo magico', 'Juan palomar', random.randint(1,5)), ('Juan palomar', 'Estadio 3 de marzo', random.randint(1,5)), ('Estadio 3 de marzo', 'Pablo Neruda', random.randint(1,5)), ('Pablo Neruda', 'CETI', random.randint(1,5)), ('Trompo magico', 'Acueducto', random.randint(1,5)), ('Acueducto', 'Pabellon', random.randint(1,5)), ('Pabellon', 'Pablo Neruda', random.randint(1,5)), ('Pabellon', 'Alberta', random.randint(1,5)), ('Alberta', 'CETI', random.randint(1,5)), ('Base aerea', 'La cima', random.randint(1,5)), ('La cima', 'Belenes', random.randint(1,5)), ('Belenes', 'Zapopan', random.randint(1,5)), ('Zapopan', 'Americas', random.randint(1,5)), ('Americas', 'Alberta', random.randint(1,5)), ('Zapopan', 'Plaza patria', random.randint(1,5)), ('Plaza patria', 'Alberta', random.randint(1,5)) ]

Grafo.add_weighted_edges_from(e)
print(nx.dijkstra_path(Grafo, 'Casa', 'CETI')) #mostrar en consola el mejor camino

"""
ejemplo Dijsktra internet
G = nx.Graph()
e = [('a', 'b', 0.3), ('b', 'c', 0.9), ('a', 'c', 0.5), ('c', 'd', 1.2)]
G.add_weighted_edges_from(e)
print(nx.dijkstra_path(G, 'a', 'd'))

['a', 'c', 'd']  salida por consola

"""
#graficar gafo

best = nx.dijkstra_path(Grafo, 'Casa', 'CETI')
nx.draw(Grafo, node_size = 100, width = 1, with_labels = True, edge_color="tab:red")
plt.show() #mostramos grafo


