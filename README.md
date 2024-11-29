# Algoritmia_Project

Per executar aquest programa cal seguir aquests passos:

1.  S'ha de tenir instalat python3 i les llibreries corresponents: matplotlib numpy networkx pandas i pillow
    per instalar-les pots fer $pip3 install modul

2.  S'ha de tenir en compte que dins dels experiments utilitzem el compilador clang++ per poder fer servir la llibreria filesystem
    si es vol canviar el compilador s'ha d'entrar dins del fitxer EXPERIMENT.py als experiments C i D i canviar la comanda clang++ per g++
    No podem assegurar que funcioni amb g++.

3. El directori /obj ha d'estar buit abans d'executar el makefile

4. Un cop l'entorn estigui preparat, ja pots fer make

5. Un cop hagi compilat tot executa el programa ./program
