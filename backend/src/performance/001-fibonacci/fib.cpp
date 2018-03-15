#include <iostream>
#include <stdio.h>

using namespace std;

long fib(long n);

main(int argc, char **argv) {
    long arg = strtol(argv[1], NULL, 10);

    fib(arg);

    return 0;
}

long fib(long n) {
    long a = 0, b = 1;
    long tmp;
    for (long i=0; i<=n; i++) {
        tmp = a;
        a = a + b;
        b = tmp;
    }
    return a;
}
