#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
cost = 0

"""
Grafo = nx.Graph() # creamos un grafo y añadimos nodos
#Añadir aristas
# G.add_edge(2, 3, weight=0.9) /// a = random.randint(1,5)

e = [('Casa', 'Base aerea', random.randint(1,5)), ('Base aerea', 'Real center', random.randint(1,5)), 
     ('Real center', 'Trompo magico', random.randint(1,5)), ('Trompo magico', 'Juan palomar', 
     random.randint(1,5)), ('Juan palomar', 'Estadio 3 de marzo', random.randint(1,5)), ('Estadio 3 de marzo'
    , 'Pablo Neruda', random.randint(1,5)), ('Pablo Neruda', 'CETI', random.randint(1,5)), ('Trompo magico',
     'Acueducto', random.randint(1,5)), ('Acueducto', 'Pabellon', random.randint(1,5)), ('Pabellon', 
     'Pablo Neruda', random.randint(1,5)), ('Pabellon', 'Alberta', random.randint(1,5)), ('Alberta', 'CETI',
     random.randint(1,5)), ('Base aerea', 'La cima', random.randint(1,5)), ('La cima', 'Belenes', 
     random.randint(1,5)), ('Belenes', 'Zapopan', random.randint(1,5)), ('Zapopan', 'Americas', 
     random.randint(1,5)), ('Americas', 'Alberta', random.randint(1,5)), ('Zapopan', 'Plaza patria',
     random.randint(1,5)), ('Plaza patria', 'Alberta', random.randint(1,5)) ]

Grafo.add_weighted_edges_from(e)

#weights = nx.get_edge_attributes(Grafo, "weight")

Grafo.add_nodes_from(Grafo.nodes)
Grafo.add_weighted_edges_from(e)

weight=nx.get_edge_attributes(Grafo,'weight')
nx.draw(Grafo, node_size
       = 100, width = 1, with_labels = True)
plt.show() #mostramos grafo


#graficar gafo
best_road = nx.DiGraph()
best = nx.dijkstra_path(Grafo, 'Casa', 'CETI')
for i in range(len(best)-1):
    best_road.add_edge(best[i], best[i+1])

nx.draw(best_road, node_size = 100, width = 1, with_labels = True, edge_color ="tab:red",)
plt.show()

print(best) #mostrar en consola el mejor camino
"""

print("")


c1 = random.randint(1,5)
c2 = random.randint(1,5)
c3 = random.randint(1,5)
c4 = random.randint(1,5)
c5 = random.randint(1,5)
c6 = random.randint(1,5)
c7 = random.randint(1,5)
c8 = random.randint(1,5)
c9 = random.randint(1,5)
c10 = random.randint(1,5)
c11 = random.randint(1,5)
c12 = random.randint(1,5)

if c3<c2:
   if c10<c11:
    cost=c1+c3+c9+c10+c12
   else:
        cost=c1+c3+c9+c11+c8
else:
    if c5<c6:
        cost=c1+c2+c4+c5+c7+c8
    else:
        cost=c1+c2+c4+c6+c8


nodos={'Casa','Base aerea','Real center','Acueducto','Pablo Neruda','CETI','Alberta','La cima'
   ,'Zapopan','Plaza patria'}


aristas = [('Casa', 'Base aerea', c1), ('Base aerea', 'Real center', c3), 
     ('Real center', 'Acueducto', c9), ('Acueducto', 'Pablo Neruda', c10),
     ('Pablo Neruda', 'CETI', c12), ('Acueducto', 'Alberta', c11), 
     ('Alberta', 'CETI', c8), ('Base aerea', 'La cima', c2), 
     ('La cima', 'Zapopan', c4), ('Zapopan', 'Alberta', c6), 
     ('Zapopan', 'Plaza patria', c5), ('Plaza patria', 'Alberta', c7)]

G=nx.DiGraph()
G.add_nodes_from(nodos)
G.add_weighted_edges_from(aristas)

pos={'Casa':[1,2],'Base aerea':[2,1],'Real center':[3,2],'Acueducto':[0.5,3],'Pablo Neruda':[3.5,3],
   'CETI':[0.5,6],'Alberta':[3.5,6],'La cima':[1,7],'Zapopan':[3,7],'Plaza patria':[2,8]}


weight=nx.get_edge_attributes(G,'weight')
nx.draw(G, pos=pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weight)

best= nx.dijkstra_path(G, 'Casa', 'CETI')
print("la mejor ruta es la siguiente:")
print(best)
print("El costo del camino menor es de: " + str(cost))
best_road = nx.DiGraph()

for i in range(len(best)-1):
    best_road.add_edge(best[i], best[i+1])
    

nx.draw(best_road, node_size = 1000, width = 1, with_labels = True, edge_color ="tab:red",)
plt.show()

