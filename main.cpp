#include <iostream>
#include <string>
using namespace std;

void Usage() {
    cout << "Para seleccionar una experimento escriba la letra en mayuscula del apartado respectivo" << endl;
    cout << "Para acabar el programa escriba 'end'" << endl;
    cout << "Los experimentos validos son C, D, E" << endl;
    cout << endl;

    cout << "Se deben tener instalados los siguientes modulos python:" << endl;
    cout << "matplotlib, numpy, networkx, random, pandas y pillow" << endl;
    cout << "para instalarlos ejecuta pip3 install modulo" << endl;
    cout << endl;
}

void ExperimentoE();

int main() {
    Usage();
    string exp = "act";
    while (exp != "end") {
        cout << "Seleccione el experimento" << endl;
        cin >> exp;
        if (exp == "C") {
            cout << "Experimento de graellas cuadradas" << endl;
            system("python3 ./resource/ExperimentoC/EXPERIMENT.py");
        } else if (exp == "D") {
            cout << "Experimento de grafos triangulados" << endl;
            system("python3 ./resource/ExperimentoD/EXPERIMENT.py");
        } else if (exp == "E") {
            cout << "Experimento de grafos geometricos" << endl;
            ExperimentoE();
        } else if (exp != "end") cout << "Seleccione un experimento valido" << endl << endl;

    }
}