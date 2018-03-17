#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;

void rs(long n);

main(int argc, char **argv) {
    long n = strtol(argv[1], NULL, 10);

    rs(n);

    return 0;
}

void rs(long n) {
    for (int i=0; i<n; i++) {
        string str = "Salida de emergencia";
        string substitution = "Entrada";
        string result = str.replace(str.begin(), str.begin()+6, substitution);
        //cout << result << endl;
    }
}
