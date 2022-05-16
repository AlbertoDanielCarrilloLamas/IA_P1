# Carrillo Lamas Alberto Daniel. 19310378. Implementacion de algoritmo Dijkstra.

#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

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
plt.show() #mostramos grafo


