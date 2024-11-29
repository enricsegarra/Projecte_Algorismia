#SCRIPT PER A COMPACTAR TOTES LES ESTADÍSTIQUES DE DIFERENTS EXPERIMENTS EN UN SOL DOCUMENT

import os
import pandas as pd

# Defineix el directori on es troben els fitxers CSV
directori = './'  # Canvia-ho pel camí correcte

# Llegeix tots els fitxers CSV del directori
fitxers_csv = [f for f in os.listdir(directori) if f.endswith('.csv')]

# Diccionari per emmagatzemar les sumes i els comptadors per a cada identificador
valors = {}

# Processa cada fitxer CSV
for fitxer in fitxers_csv:
    cami_fitxer = os.path.join(directori, fitxer)
    df = pd.read_csv(cami_fitxer, header=None, names=['ID', 'Valor'])
    
    for _, row in df.iterrows():
        id = row['ID']
        valor = row['Valor']
        
        if id in valors:
            valors[id]['suma'] += valor
            valors[id]['comptador'] += 1
        else:
            valors[id] = {'suma': valor, 'comptador': 1}

# Calcula la mitjana per a cada identificador
resultats = []
for id, dades in sorted(valors.items()):
    mitjana = dades['suma'] / dades['comptador']
    resultats.append([id, mitjana])

# Guarda els resultats en un nou fitxer CSV
df_resultats = pd.DataFrame(resultats, columns=['ID', 'Mitjana'])
df_resultats.to_csv('estadisticageneral.csv', index=False)

print("Fitxer 'estadisticageneral.csv' creat amb èxit.")
