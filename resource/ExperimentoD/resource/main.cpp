#include <iostream>
#include <vector>
#include <string>
#include <random>
#include <iomanip>
#include <filesystem>
#include <algorithm>
#include "Graf_impl.h"
using namespace std;

//Genera un graf amb n vèrtex i amb la probabilitat p de generar arestes entre vèrtexs
grafo genera_random(int n, float p) {
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

bool check_infinite_cluster(grafo& grafo) {
    // Obtenim el nombre de components connexes
    list<pair<int, list<int>>> aux1 = grafo.get_vertices();

    if (aux1.size() == 0) return false; // Si el graf és buit, no hi ha clúster infinit

    int n = aux1.size(); // Nombre total de vèrtexs

    // Mida màxima de qualsevol component
    int max_component_size = 0;

    // Llista per guardar les components ja explorades
    list<list<int>> components = grafo.get_all_components();

    for (const auto& component : components) {
        int component_size = component.size();
        if (component_size > max_component_size) {
            max_component_size = component_size;
        }
    }

    // Considerem un clúster infinit si la mida màxima de la component és almenys el 50% dels vèrtexs totals
    if (max_component_size >= n * 0.5) {
        return true;
    } else {
        return false;
    }
}


//Percolacion de vertice
void site_perlocation(grafo& grafo, double p) {

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
void bond_perlocation(grafo& grafo, double p) {

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

int main() {
    string directorio = "./docs/";

    int percolacio = -1;
    while(percolacio < 0 || percolacio > 1){
        cout << "Introdueix 0 si vols realitzar la percolació de nodes o 1 per realitzar percolació d'arestes" << endl;
        cin >> percolacio;
    }

    int num_experiments;
    cout << "introdueix el numero d'experiments que vols fer" << endl;
    cin >> num_experiments;

    for(int i = 0; i < num_experiments; ++i){
        double p = 0;
        double percolados = 0;
        double descartados = 0; //si generamos un grafo y este desde el principio no es connexo no podemos ver el cambio de fase
        ofstream file("estadisticas"+to_string(i)+".csv");
        while(p <= 1){
            percolados = 0;
            descartados = 0;
            for(const auto& entry : filesystem::directory_iterator(directorio)){
                if(entry.is_regular_file() && entry.path().extension() == ".csv" && entry.path().string().rfind("perc.csv") != (entry.path().string().size() - 8)){
                    string filePath = entry.path().string();
                    ifstream fgraf(filePath);

                    //string outfilePath = filePath;
                    //outfilePath.erase(outfilePath.length() - 4, 4);
                    //ofstream outgraf(outfilePath+to_string(p)+"perc"+".csv");

                    grafo generat;
                    generat.read(fgraf); //Inicialitzem el graf
                        if(percolacio == 1){
                            bond_perlocation(generat, p);
                        }
                        else{
                            site_perlocation(generat, p);
                        }
                        //generat.write(outgraf);
                        if (generat.CC() == 1){
                            cout << "Graf amb 1 component conexa: " << filePath << endl;
                            ++percolados;
                        }
                        else ++descartados;

                } 
            }
            
            double p_trans = double(percolados/max(descartados,1.0));
            cout <<  p << "," << percolados << descartados << endl;
            file << std::fixed << std::setprecision(3);
            file << p << "," << p_trans << endl;
            p += 0.005;
        }
    }
}