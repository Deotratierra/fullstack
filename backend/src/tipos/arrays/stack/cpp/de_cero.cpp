#include <iostream>
#include <cstdlib>

using namespace std;

// =============     STACK    =================
/* La siguiente pila está creada de 0 con propósitos de aprendizaje:
   Para no reinventar la rueda usa:
   http://www.cplusplus.com/reference/stack/stack/
*/

template <typename Type>
class stack {
    public:
        Type *_data;   // Datos
        ulong _s;      // Tamaño
        ulong _p;      // Puntero de la pila (posición de la próxima escruitura)
        ulong _grow_n; // Indicar si crecerá la pila n elementos si es necesario
                       //     (0 significa que no crecerá)

        // Constructor
        stack(ulong n, ulong grow_n=0) {
            _s = n;
            _data = new Type[_s];  // Creamos una lista en memoria
            _p = 0;                // La pila está vacía
            _grow_n = grow_n;
        }

        // Destructor
        ~stack() { delete [] _data; }

        ulong num()  const { return _p; }

        ulong push(Type z) {
            /* Añade un elemento z en la parte superior de la pila
               Retorna el tamaño de la misma, 0 si la pila se desborda
               con el nuevo elemento. Si el atributo _grow_n no es 0,
               la pila crece este indique. */
            if (_p >= _s ) {
                if (_grow_n == 0 ) { return 0; } // desbordamiento
                grow();                          // si no, crece
            }

            _data[_p] = z;  // entra el nuevo elemento
            ++_p;                   // el puntero avanza
            return _s;
        }

        ulong pop(Type &z) {
            /* Lee la entrada superior y se elimina. Devuelve
               el número de entradas que existían antes de eliminar
               el elemento. Si está vacía devuelve 0 y deja a z sin
               definir
               . */
            ulong ret = _p;
            if (0 != _p) { --_p; z = _data[_p]; }
            return ret;
        }

        ulong poke(Type z) {
            // Modifica la entrada superior.
            // Devuelve el número de entradas.
            // Si está vacía devuelve 0 y no hace nada.
            if (0 != _p) { _data[_p-1] = z; }
            return _p;
        }

        ulong peek(Type &z) {
            // Lee la entrada superior, sin eliminarla.
            // Devuelve el número de entradas en la pila.
            // Si está vacía devuelve 0 y deja a z sin definir.
            if (0 != _p) { z = _data[_p-1]; }
            return _p;
        }

        ulong peek_at(ulong i, Type &z)  const
         // Lee la entrada _data[i] sin eliminar ninguna.
         // Retorna el número de entradas.
         // Si i está fuera de rango devuelve 0 y deja z sin definir.
        {
            if ( i >= _p ) { return 0; }
            z = _data[i];
            return _p;
        }

    private:
        void grow() {
            // Función interna para hacer crecer la pila si el
            // atributo _grow_n es diferente a 0.
            ulong new_size = _s + _grow_n; // Nuevo tamaño
            _data = (Type *)realloc(_data, new_size);  // man realloc
            _s = new_size;
        }
};

// ===============================================

template <typename Type>
void vpush(stack<Type> &pila, ulong z) {
	ulong response = pila.push(z);
	 if (response == 0) {
        cout << "El elemento " << z << " no fue insertado" << endl;
    } else {
        cout << "El elemento " << z << " fue insertado con éxito" << endl;
    }

}

int main() {

    ulong num = 4;
    stack<ulong> pila(num, num);
    ulong k = 1;

    vpush(pila, k);
    k = 3;
    vpush(pila, k);

    ulong last;
    pila.peek(last);
    cout << "Último elemento de la pila: " << last << endl << endl;

    cout << "Usamos pop en la pila" << endl;
    pila.pop(num);
    cout << "Hemos sacado el elemento " << num << " de la pila" << endl << endl;

    ulong new_elements = 4;
    cout << "Insertamos " << new_elements << " elementos más en la pila" << endl;
    int count = 1;
    for (ulong in=5; count < new_elements+1; count++) {
    	vpush(pila, in*count);
    }

    ulong size;
    size = pila.peek(num);
    cout << "La pila tiene " << size << " elementos y el último es " << num << endl;

    return 0;
}
