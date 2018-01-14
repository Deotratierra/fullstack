#include <Python.h>

/* El entorno de ejecución de Python ve todos los objetos del lenguaje como
    variables del tipo PyObject*, el cual sirve como tipo base para todos los objetos de Python.
    El objeto PyObject en sí mismo sólo contiene el contador de referencia
    y un puntero al tipo del objeto. Aquí es donde sucede la acción; el tipo del objeto
    determina que funciones de C son llamadas cuando, por ejemplo, un atributo se busca
    en un objeto si este es multiplicado por otro objeto. Estas funciones de C son llamados
    "métodos del tipo".
*/

// Creamos una nueva estructura para nuestro tipo
typedef struct {
    PyObject_HEAD
    double x;
    double y;
} PuntoObject;

// Características del nuevo tipo
static PyTypeObject PuntoType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "lib_c.Punto",             /* tp_name */
    sizeof(PuntoObject),       /* tp_basicsize */
    0,                         /* tp_itemsize */
    0,                         /* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
    0,                         /* tp_reserved */
    0,                         /* tp_repr */
    0,                         /* tp_as_number */
    0,                         /* tp_as_sequence */
    0,                         /* tp_as_mapping */
    0,                         /* tp_hash  */
    0,                         /* tp_call */
    0,                         /* tp_str */
    0,                         /* tp_getattro */
    0,                         /* tp_setattro */
    0,                         /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT,        /* tp_flags */
    "Objeto de tipo Punto.",    /* tp_doc */
};

// Especificaciones del módulo
static PyModuleDef lib_c_module = {
    PyModuleDef_HEAD_INIT,
    "lib_c",
    "Módulo de ejemplo para crear un nuevo tipo para Python.",
    -1,
    NULL, NULL, NULL, NULL, NULL
};

PyMODINIT_FUNC PyInit_lib_c(void)
{
    PyObject* m;

    PuntoType.tp_new = PyType_GenericNew;
    if (PyType_Ready(&PuntoType) < 0)  // Si no está listo el tipo
        return NULL;                   // devuelve nul cancelando la operación

    m = PyModule_Create(&lib_c_module); // Creamos el ódulo
    if (m == NULL)
        return NULL;

    Py_INCREF(&PuntoType);
    PyModule_AddObject(m, "Punto", (PyObject *)&PuntoType);
    return m;
}

