#include <iostream>
#include <string>
using namespace std;

int main() {
  // Declaración de variables
  int n;
  string word;
  int m;
  string search;

  // Creación de arbol TRIE con n palabras
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> word;
  }

  // Busqueda de m palabras dentro del arbol
  cin >> m;
  for (int i = 0; i < m; i++) {
    cin >> search;
  }
  return 0;
}