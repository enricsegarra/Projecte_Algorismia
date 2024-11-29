import networkx as nx
import numpy as np
import csv
import random

def guardar_graf_csv(graf, nom_fitxer, i):
    # Obrim el fitxer en mode escriptura
    with open(nom_fitxer, mode='a', newline='') as fitxer_csv:
        writer = csv.writer(fitxer_csv, delimiter=',')  # Utilitzem l'espai com a delimitador
        
        # Iterem per cada node del graf
        for node in graf.nodes:
            veins = list(graf.neighbors(node))  # Obtenim els nodes veïns (nodes amb els que comparteix una aresta)
            writer.writerow([node] + veins)  # Escrivim el node seguit dels seus veïns
        fitxer_csv.write('\n')

def esborrar_fitxer(nom_fitxer):
    with open(nom_fitxer, mode='w') as fitxer_csv:
        pass  # Obrim el fitxer en mode 'w' per sobreescriure el contingut existent i buidar-lo



# Paràmetres per generar el graf
num_grafs = 10
nom_resultat_csv = 'graf_geometric.csv'  # Nom del fitxer de sortida per al CSV

esborrar_fitxer(nom_resultat_csv)

for i in range(num_grafs):
    num_nodes = random.randint(50, 100) #numero de nodes
    radi = 0.4   # Radi de connexió (EXPERIMENTEU)

    # Genera un graf geomètric aleatori
    graf = nx.random_geometric_graph(num_nodes, radi)

    # Guardar el graf en el format especificat al CSV
    guardar_graf_csv(graf, nom_resultat_csv, i)
