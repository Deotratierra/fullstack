
// Compilación:
// gcc -Wall -O3 -shared lib_c.c -o lib_c.so

// Luego debemos agregar nuestro directorio a las bibliotecas dinámicas
// export LD_LIBRARY_PATH=$PWD


int _summa(int x) {
    int y = 0;
    for (int i=0; i<x; i++) {
        y += i + 1;
    }
    return y;
}
