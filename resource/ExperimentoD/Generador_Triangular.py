import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import csv

def generar_graella_triangular(n):
    G = nx.Graph()

    # Afegir nodes i arestes
    for i in range(n):
        for j in range(i + 1):
            node = (i, j)  # Cada node és una tupla (fila, columna)
            G.add_node(node)

            # Connectar amb el node de la dreta
            if j < i:
                G.add_edge((i, j), (i, j + 1))
            # Connectar amb el node de baix
            if i < n - 1:
                G.add_edge((i, j), (i + 1, j))
                # Connectar amb el node de baix a la dreta
                G.add_edge((i, j), (i + 1, j + 1))

    return G

def guardar_graella_en_fitxer(G, fitxer):
    nodes = list(G.nodes())
    node_index = {nodes[i]: i for i in range(len(nodes))}  # Diccionari per a obtenir l'índex de cada node

    with open(fitxer, 'w') as f:
        for node in nodes:
            # Obtenim els veïns (nodes amb els que comparteix aresta)
            veins = list(G.neighbors(node))
            # Escrivim la línia al fitxer
            f.write(f"{node_index[node]}," + ",".join(str(node_index[v]) for v in veins) + "\n")


n = int(input("Introdueix el nombre de grafs a generar\n")) # Numero de grafs creats
nom_resultat_csv = './docs/graf_triangular'  # Nom del fitxer de sortida per al CSV

for i in range(n):
    nom_csv = nom_resultat_csv+str(i)
    num_nodes = random.randint(2, 10) #Alçada
    G = generar_graella_triangular(num_nodes)
    guardar_graella_en_fitxer(G,nom_csv+'.csv')
