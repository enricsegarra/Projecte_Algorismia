# SCRIPT PER VISUALITZAR UN GRAF DES DE TOTS ELS CSV D'UNA CARPETA

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import glob
import os



nom_carpeta = './docs/*.csv'  # Canvia això pel camí de la carpeta amb els CSVs

# Funció per disposar els nodes en una quadrícula
def quadrat_layout(graf):
    nodes = list(graf.nodes)
    costat = int(np.ceil(np.sqrt(len(nodes))))  # El nombre de nodes per costat
    pos = {}

    # Assignem les posicions en una quadrícula
    for i, node in enumerate(nodes):
        fila = i // costat
        columna = i % costat
        pos[node] = (columna, -fila)  # Cada node es col·loca a la seva posició (x, y)
    
    return pos

def triangular_layout(graf):
    nodes = list(graf.nodes)
    num_nodes = len(nodes)
    
    # Calculem el nombre de files necessàries per a la graella triangular
    rows = 0
    while (rows * (rows + 1)) // 2 < num_nodes:
        rows += 1
    
    # Assignem les posicions en una graella triangular
    pos = {}
    index = 0
    for row in range(rows):
        for col in range(row + 1):  # Cada fila té un node més
            if index < num_nodes:
                pos[nodes[index]] = (col - row / 2, -row)  # Coloca cada node en (x, y)
                index += 1
    
    return pos

# Llegeix el CSV
def llegir_graf_csv(nom_fitxer):
    df = pd.read_csv(nom_fitxer, names=list(range(500))).dropna(axis='columns', how='all')  # Llegeix el CSV sense capçalera
    graf = nx.Graph()  # Crea un graf no dirigit

    # Afegeix els nodes del graf
    for _, fila in df.iterrows():
        origen = fila[0]
        graf.add_node(str(int(origen)))

    df = pd.read_csv(nom_fitxer, names=list(range(500))).dropna(axis='columns', how='all')  # Llegeix el CSV sense capçalera
    # Afegeix arestes al graf des de les files del CSV
    for _, fila in df.iterrows():
        origen = fila[0]  # El primer element de la fila és el node origen
        for desti in fila[1:]:  # La resta són nodes destinació
            if pd.notna(desti):  # Ignora els valors NaN
                # print("aresta: ",origen,"al",desti)
                graf.add_edge(str(int(origen)), str(int(desti)))  # Afegeix una aresta entre l'origen i el destí
    return graf

# Cerca tots els fitxers CSV dins de la carpeta
fitxers_csv = glob.glob(nom_carpeta)
# Itera per cadascun dels fitxers CSV
for fitxer in fitxers_csv:
    nom_fitxer, _ = os.path.splitext(fitxer)  # Elimina l'extensió .csv per obtenir el nom base

    # Llegeix el graf des del fitxer CSV
    graf = llegir_graf_csv(fitxer)

    # Crea el gràfic
    plt.figure(figsize=(8, 6))  # Configura la mida del gràfic
    pos = quadrat_layout(graf)  # Disposa els nodes en un layout de quadrícula
    nx.draw(graf, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', edge_color='gray')
    plt.title(f'Visualització del graf: {os.path.basename(fitxer)}')

    # Guarda el gràfic com una imatge PNG amb el mateix nom del fitxer CSV
    plt.savefig(f'{nom_fitxer}.png')  # Guarda el gràfic en un fitxer PNG amb el mateix nom
    plt.close()  # Tanca la figura per evitar sobreescriptura a la següent iteració