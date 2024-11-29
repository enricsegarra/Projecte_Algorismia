import subprocess
import os
import glob
from PIL import Image

def compilar_i_executar_cpp(fitxer_cpp):
    # Nom del fitxer binari després de compilar
    fitxer_executable = 'experimentcpp'
    
    # Comanda per a compilar el fitxer C++ amb g++
    comanda_compilacio = ['clang++', '-std=c++17',fitxer_cpp, '-o', fitxer_executable]
    
    try:
        # Compilar el fitxer C++
        print("Compilant el fitxer C++...")
        subprocess.run(comanda_compilacio, check=True)
        print("Compilació finalitzada amb èxit.")
        
        # Comanda per a executar el programa compilat
        print("Executant el programa...")
        subprocess.run(f'./{fitxer_executable}', check=True)
        
    except subprocess.CalledProcessError as e:
        print(f"Error durant la compilació o execució: {e}")
    finally:
        # Esborrem el fitxer executable després de la seva execució
        if os.path.exists(fitxer_executable):
            os.remove(fitxer_executable)
            print(f"Fitxer {fitxer_executable} esborrat.")

def executar_script(script_path):
    try:
        # Executar l'script com una comanda del sistema
        subprocess.run(['python3', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"S'ha produït un error executant l'script: {e}")

def esperar_tecla(missatge):
    # Si estem en Windows, usem msvcrt
    if os.name == 'nt':
        import msvcrt
        print("\n"+missatge+"Prem qualsevol tecla per continuar")
        msvcrt.getch()
    # Si estem en un sistema Unix, usem termios i tty
    else:
        import sys
        import tty
        import termios
        print("\n"+missatge+"Prem qualsevol tecla per continuar")
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def esborrar_fitxers_directori(directori):
    try:
        # Llista tots els fitxers del directori
        for fitxer in os.listdir(directori):
            fitxer_complet = os.path.join(directori, fitxer)
            # Comprova si és un fitxer (i no un subdirectori)
            if os.path.isfile(fitxer_complet):
                os.remove(fitxer_complet)
    except Exception as e:
        print(f"S'ha produït un error: {e}")

def eliminar_fitxersconcrets(directori,extensio):
    # Cerca tots els fitxers .csv dins del directori
    patron = os.path.join(directori, extensio)
    fitxers_csv = glob.glob(patron)
    
    # Eliminar cadascun dels fitxers trobats
    for fitxer in fitxers_csv:
        try:
            os.remove(fitxer)
        except Exception as e:
            print(f"Error eliminant {fitxer}: {e}")

def obrir_tots_els_pngs(directori):
    # Busca tots els fitxers .png del directori especificat
    patron = os.path.join(directori, '*.png')
    fitxers_png = glob.glob(patron)
    
    # Obre i mostra cada imatge .png
    for fitxer in fitxers_png:
        imatge = Image.open(fitxer)
        print(f"Obrint: {fitxer}")
        imatge.show()





# Exemple d'ús
mode = int(input("Aquest és l'script per executar l'experiment.\nSi desitges crear un nou conjunt de grafs aleatoris introdueïx 0, si vols utilitzar els grafs ja existents al directori docs prem qualsevol altre nombre.\n"))

if(len(os.listdir("./docs/")) == 0 and mode != 0):
    esperar_tecla("El directori que ha de guardar els grafs està buit, genera els grafs siusplau.\n")
    mode = 0

if(mode == 0):
    esborrar_fitxers_directori('./docs/')
    print("Directori /docs/ netejat dels grafs anteriors\nExecutant el Generador de grafs:\n")
    executar_script('./resource/ExperimentoD/Generador_Triangular.py')
    print("Grafs Generats correctament\n")
    esperar_tecla("Iniciant l'experiment amb els grafs acabats de generar\n")

esperar_tecla("Elminem els resultats de l'experiment anterior\n")
eliminar_fitxersconcrets('./','*.csv')
eliminar_fitxersconcrets('./','*.png')
eliminar_fitxersconcrets('./resource','*.csv')
eliminar_fitxersconcrets('./resource','*.png')


esperar_tecla("Executem l'experiment per a tots els grafs al directori /docs/\n")
compilar_i_executar_cpp('./resource/ExperimentoD/resource/main.cpp')

esperar_tecla("Juntem tots els resultats creats dins del fitxer estadisticageneral\n")
executar_script("./resource/ExperimentoD/resource/Compactador_estadistiques.py")

esperar_tecla("Visualitzem els resultats de l'estadística general\n")
executar_script("./resource/ExperimentoD/resource/Grafic_est_general.py")

obrir_tots_els_pngs(".")

netejar = int(input("Ja hem acabat l'experiment\nprem 0 -> si vols netejar tots els resultats menys les imatges\nprem 1 -> Si vols netejar tots els resultats.\nprem qualsevol altre per acabar\n"))
if netejar == 0:
    esborrar_fitxers_directori('./docs/')
    eliminar_fitxersconcrets('./','*.csv')
    eliminar_fitxersconcrets('./resource','*.csv')
    eliminar_fitxersconcrets('./','*.exe')
    eliminar_fitxersconcrets('./','*.out')

elif netejar == 1:
    esborrar_fitxers_directori('./docs/')
    eliminar_fitxersconcrets('./','*.csv')
    eliminar_fitxersconcrets('./','*.png')
    eliminar_fitxersconcrets('./resource','*.csv')
    eliminar_fitxersconcrets('./resource','*.png')
    eliminar_fitxersconcrets('./','*.exe')
    eliminar_fitxersconcrets('./','*.out')
