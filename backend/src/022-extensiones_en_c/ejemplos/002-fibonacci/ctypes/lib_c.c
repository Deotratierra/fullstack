// Compilación:
// gcc -Wall -O3 -shared lib_c.c -o lib_c.so

// Luego debemos agregar nuestro directorio a las bibliotecas dinámicas
// export LD_LIBRARY_PATH=$PWD

double cfib(int n) {
    int i;
    double a=0.0, b=1.0, tmp;
    for (i=0; i<n; ++i) {
    	tmp = a; a = a + b; b = tmp;
    }
    return a;
}
