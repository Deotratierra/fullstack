# Macros

CFLAGS = -g -Wall
SRC = main.c funciones.c funciones.h
OBJ = main.o funciones.o

.PHONY: all clean

all: $(OBJ)
	gcc $(CFLAGS) -o main $(OBJ)

clean:
	rm $(OBJ) main
