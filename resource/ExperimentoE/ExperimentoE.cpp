#ifndef EXPERIMENTOE_CPP
#define EXPERIMENTOE_CPP
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <list>
#include <iomanip>
#include <random>
#include "Graf_impl.h"
using namespace std;

//Genera un graf amb n vèrtex i amb la probabilitat p de generar arestes entre vèrtexs
grafo static genera_random(int n, float p) {
    grafo G;
    int pr = p*100;
    for (int i = 0; i < n; ++i) G.insert_vertice(i);  //Afegeix el node i al graf
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            int r = rand()%100;
            if (r < pr) G.insert_aresta(i,j); //Afegeix al node i una aresta al node j
        }
    }
    return G;
}

void static site_perlocation(grafo& grafo, double p) {

    //Generar distribucio aleatoria
    random_device gen_rand;
    default_random_engine generator(gen_rand());
    uniform_real_distribution<double> distribution(0,1);  

    double a; 
    list<pair<int, list<int>>> aux1 = grafo.get_vertices();
    for (auto itr = aux1.begin(); itr != aux1.end(); ++itr) {
        a = distribution(generator);
        if (a > (1-p)) {
            grafo.remove_vertice((*itr).first);
        }  
    }  
}

//percolacion de arestas
void static bond_perlocation(grafo& grafo, double p) {

    random_device gen_rand;
    default_random_engine generator(gen_rand());
    uniform_real_distribution<double> distribution(0,1);


    double a;
    list<pair<int, list<int>>> aux1 = grafo.get_vertices();

    for (auto itr = aux1.begin(); itr != aux1.end(); ++itr) {
        for (auto itr2 = (*itr).second.begin(); itr2 != (*itr).second.end(); ++itr2) {
            a = distribution(generator);
            if (a > (1-p)) {
                grafo.remove_aresta((*itr).first, (*itr2));
            }  
        }
    }
}


void ExperimentoE() {
    ofstream file("estadisticas(50-100).csv");
    cout << "Experimento con 50-100 nodos" << endl;
    file << "p, p de transición" << endl;
    bool ok = true;
    double p = 0.00;

    int res = system("python3 ./resource/ExperimentoE/Geometric_Generator.py");
    if (res != 0) ok = false;


    ifstream grafos("graf_geometric.csv");
    if (not grafos.is_open()) {
        ok = false;
        cout << "No se puede abrir los grafos geometricos" << endl;
    }

    while (ok and p <= 1.0) {
        int res = system("python3 ./resource/ExperimentoE/Geometric_Generator.py");

        if (res != 0) ok = false;


        ifstream grafos("graf_geometric.csv");
        if (not grafos.is_open()) {
            ok = false;
            cout << "No se puede abrir los grafos geometricos" << endl;
        }

        double percolados = 0.0;
        double validos = 0.0;

        for (int i = 0; i < 100; ++i) {
            grafo act;
            act.read(grafos);

            if (act.CC() == 1) {
                cout << validos << endl;
                ++validos;
                bond_perlocation(act, p);
                if (act.CC() != 1) ++percolados;
            }
        }

        double ppercolado = percolados/(10.0 - (10.0 -validos));
        file << std::fixed << std::setprecision(5);
        file << p << "," << ppercolado << endl;
        cout << "Probabilidad " << p <<  " echa" << endl;
        p += 0.001;
    }

    system("python3 ./resource/ExperimentoE/Grafic_estadisticas.py");
}
#endif