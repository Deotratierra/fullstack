// Primero incluimos la biblioteca de Python para C
#include <Python.h>

/* Creamos la función que calcula el sumatorio.
La hacemos privada (_<nombre_de_función>) ya que la envoltura
cogerá el nombre de la función sin _ */
int _summa(int x) {
    int y = 0;
    for (int i=0; i<x; i++) {
        y += i + 1;
    }
    return y;
}

// Envoltura de Python para la funcion summa()
static PyObject *summa(PyObject *self, PyObject *args) {
    /* La función toma dos objetos PyObject.
    Este es el objeto de Python a más bajo nivel ya que todos los tipos de objetos en Python
    son extensiones de este. Como en Python todo es un objeto, pues le pasamos *self
    como si estuviéramos haciendo programación orientada a objetos:
    https://docs.python.org/3/c-api/structures.html */

    int num; // Declaramos el argumento de entrada (x)

    // Parseamos los argumentos de entrada de enteros en Python a enteros de C:
    // https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple
    if (!PyArg_ParseTuple(args, "i", &num)) {
        return NULL;
        /* En el caso de pasar agumentos incorrectos la función retornará nula
        y el intérprete lanzará una excepción apropiada. La cadena "i" indica
        que queremos pasarle un int, si fueran 2 sería "ii". */
    }

    /* Retornamos la función convirtiendo el entero de C en entero de Python
       gracias a la función Py_BuildValue():
       https://docs.python.org/3.6/c-api/arg.html#c.Py_BuildValue   */
    return Py_BuildValue("i", _summa(num));
}

// Definimos las funciones del módulo
static PyMethodDef summa_Methods[] = {
    {"summa", summa, METH_VARARGS, "Calcula el sumatorio de un número entero."},
    {NULL, NULL, 0, NULL}
};

/* Struct con la definición del módulo
(contiene toda la información necesaria para crear el objeto) */
static struct PyModuleDef summamod = {
    PyModuleDef_HEAD_INIT,
    "summa",  // nombre del módulo
    "Módulo con función para calcular el sumatorio de un número entero",  // documentación del módulo
    -1,
    summa_Methods
};


/* Inicialización del módulo (todos los módulos deben ser inicializados).
Hay algo importante aquí: cuando llamamos a PyInit_lib_c, debemos entender que
lib_c es el nombre de la extensión que estamos creando, el cual lo definimos
en el setup.py

Si pruebas a cambiar el nombre de la función por PyInit_summa, compilará correctamente,
pero al intentar importar el módulo desde Python te dará el error:
"ImportError: dynamic module does not define module export function (PyInit_lib_c)"
Lo cual quiere decir que, si has especificado en el archivo de instalación el nombre
de extensión "lib_c", debes exportar la función como PyInit_lib_c */
PyMODINIT_FUNC PyInit_lib_c(void) {
    return PyModule_Create(&summamod);
}

/* Fuentes:
https://es.stackoverflow.com/questions/102982/puedo-insertar-c%C3%B3digo-c-en-python
*/
