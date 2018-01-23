#include <stdio.h>
#include "libpitagoras.h"

void saludo();

int main(int argc, char *argv[])
{
  printf("La hipotenusa es: %f\n", pitagoras(3, 4));

  return 0;
}