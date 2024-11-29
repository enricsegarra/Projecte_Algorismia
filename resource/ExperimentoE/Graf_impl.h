#ifndef GRAF_IMPL_H
#define GRAF_IMPL_H

#include "graf.h"
#include <fstream>
#include <vector>
#include <stack>
#include <list>
#include <sstream>
#include <iostream>
#include <stdio.h>
#include <stdexcept>
using namespace std;


grafo::grafo() {

}

grafo::grafo(int v, const list<int>& arestas) {
    list<int> aux = arestas;
    vertices.push_back({v,aux});
}

void grafo::insert_vertice(int v) {
    list<int> aux;
    vertices.push_back({v,aux});
}

void grafo::remove_one_direction(int n, int v) { //eliminamos de v la conexion hacia n
    bool found = false;
    auto it = vertices.begin();

    while (not found and it != vertices.end()) {
        if ((*it).first == v) {
            found = true;

            bool found2 = false;
            auto it2 = (*it).second.begin();
            while(not found2 and it2 != (*it).second.end()) {

                if ((*it2) == n) {
                    found2 = true;
                    (*it).second.erase(it2);
                } else ++it2;
            }
        } else ++it;
    }
}

void grafo::DFS(int v, vector<bool>& visitados) {
    visitados[v] = true;

    for (auto vertex : vertices) {
        if (vertex.first == v) {
            for (auto adj : vertex.second) {
                if (not visitados[adj]) DFS(adj, visitados);
            }
        }
    }
}

int grafo::CC() {
    int V = vertices.size();
    vector<bool> vis(V, false);

    int componentes = 0;
    for (auto it : vertices) {
        int v = it.first;
        if (not vis[v]) {
            DFS(v, vis);
            ++componentes;
        }
    }
    return componentes;
}

void grafo::remove_vertice(int v) {
    bool found = false;

    auto it = vertices.begin();
    while (not found and it != vertices.end()) {
        if ((*it).first == v) {
            found = true;
            for (auto it2 = (*it).second.begin(); it2 != (*it).second.end(); ++it2) remove_one_direction((*it).first, (*it2));
            vertices.erase(it);
        } else ++it;
    }
}

void grafo::insert_aresta(int v1, int v2) {
    if (not exist_conection(v1, v2) and exist(v1) and exist(v2)) {
        for (auto it = vertices.begin(); it != vertices.end(); ++it) {
            if ((*it).first == v1) (*it).second.push_back(v2);
            else if ((*it).first == v2) (*it).second.push_back(v1);
        }
    }
}

bool grafo::exist_conection(int v1, int v2) const {
    for (auto& it1 : vertices) {
        if (it1.first == v1) {
            for (auto& it2 : it1.second) {
                if (it2 == v2) return true;
            }
        }
    }
    return false;
}

void grafo::remove_aresta(int v1, int v2) {
    auto it = vertices.begin();
    
    bool f1 = false;
    bool f2 = false;

    while ((not f1 or not f2) and it != vertices.end()) {
        if ((*it).first == v1) {
            f1 =  true;
            bool found = false;

            auto it2 = (*it).second.begin();
            while (not found and it2 != (*it).second.end()) {
                if ((*it2) == v2) {
                    found = true;
                    (*it).second.erase(it2);
                } else ++it2;
            }

        } else if ((*it).first == v2) {
            f2 = true;
            bool found = false;

            auto it2 = (*it).second.begin();
            while (not found and it2 != (*it).second.end()) {
                if ((*it2) == v1) {
                    found = true;
                    (*it).second.erase(it2);
                } else ++it2;
            }

        } 
        
        if ((not f1 or not f2))++it;
    }
}

void grafo::read(ifstream& file) {
    string linea;
    while(getline(file, linea)) {
        if (not linea.empty()) {
            stringstream line(linea);

            string vertice;
            getline(line, vertice, ',');
            if (not exist(stoi(vertice))) insert_vertice(stoi(vertice));
            
            string arestas;
            while (getline(line, arestas, ',')) {
                insert_aresta(stoi(vertice), stoi(arestas));
            }
        } else break;
    }
}

int grafo::get_element() const {
    return (* vertices.begin()).first;
}

void grafo::write(ofstream& file) {
    for (auto& vertice : vertices) {
        file << to_string(vertice.first);
        for (auto& aresta : vertice.second) {
            file << "," << to_string(aresta);
        }
        file << endl;
    }
}

void grafo::print() const {
    for (auto& v : vertices) {
        cout << "Soy " << v.first << " con numero de arestas " << v.second.size() << " y estamos conectado a : ";
        for (auto& a : v.second) {
            cout << a << " ";
        }
        cout << endl;
    }
}

int grafo::size() const {
    return vertices.size();
}

void grafo::copia_grafo(list<pair<int, list<int>>> aux) {
    vertices = aux;
}

list<pair<int, list<int>>> grafo::get_vertices() const {
    return vertices;
}

bool grafo::exist(int v) const {
    for (auto& i : vertices) {
        if (i.first == v) return true;
    }
    return false;
}

#endif
