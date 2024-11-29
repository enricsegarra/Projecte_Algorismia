#SCRIPT PER A CONSULTAR LES ESTADÍSTIQUES DE PERCOLACIÓ D'UN EXPERIMENT EN CONCRET (de la forma estadisticas0,estadisticas1...)

import pandas as pd
import matplotlib.pyplot as plt

# Llegeix el fitxer CSV
# Assegura't que el fitxer 'valors.csv' estigui en el mateix directori que aquest script
data = pd.read_csv('./estadisticas1.csv', header=None)

# Assigna les columnes a variables
x = data[0]
y = data[1]

# Crea el gràfic
plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title('Gràfic de valors')
plt.xlabel('Eix X (Primera columna)')
plt.ylabel('Eix Y (Segona columna)')
plt.grid(True)

# Mostra el gràfic
plt.show()