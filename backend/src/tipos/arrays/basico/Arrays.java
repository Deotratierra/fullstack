/**
 * En Java, los arrays tienen un tamaño fijo tras ser inicializados.
 *   Para usar arrays de tamaño dinámico usamos el objeto `ArrayList`.
 **/

// Arrays de tamaño dinámico
import java.util.ArrayList;

public class Arrays {
	public static void main(String[ ] arg) {

        // ---------------------------------------------------------

		//              ARRAYS DE TAMAÑO ESTÁTICO

		// Inicialización de array
		int[] arrayDeEnteros1;
		
        // Si la variable ya ha sido inicializada pero su contenido
        //   no ha sido definido, como en `arrayDeEnteros1`,
        //   debemos usar la siguiente sintaxis (con `new`) para
        //   definir su contenido:
        arrayDeEnteros1 = new int[] {1, 2, 3};

        // Otra forma de inicializar un array de enteros es usar
        //   la siguiente sintaxis. En este caso, inicializamos
        //   un array de 10 ceros:
        int[] arrayDeEnteros2 = new int[10];

        // Inicialización de un array de cadenas
        String[] arrayDeCadenas1 = {"Hola", "Hasta luego"};
        System.out.println(arrayDeCadenas1[1]); // Hasta luego
        

        //          -----------------------------------------

        // Acceso a los valores del array
        System.out.println(arrayDeEnteros1[1]); // 2
        System.out.println(arrayDeEnteros2[9]);  // 0

        // Al acceder a un valor que no existe en el array,
        //   nos salta una excepción en tiempo de ejecución:

        //System.out.println(arrayDeEnteros2[10]);
        //  Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: 10
        
        System.out.print("\n");

        //         -------------------------------------------

        // Recorrer un array (¡igual que en Javascript!)
        for (int i=0; i<arrayDeEnteros1.length; i++) {
        	System.out.print(arrayDeEnteros1[i] + " "); // 1 2 3 
        }

        System.out.print("\n");

        // ---------------------------------------------------------


        //              ARRAYS DE TAMAÑO DINÁMICO

        // Inicialización de array de tamaño dinámico vacío
        //   que admite valores de múltiples tipos
        ArrayList arrayDinamico1 = new ArrayList();

        // Adición de elementos al array
        arrayDinamico1.add(1);
        arrayDinamico1.add("dos");
        arrayDinamico1.add(3.0);

        // Impresión del array completo
        System.out.println(arrayDinamico1); // [1, dos, 3.0]

        // Acceso a los valores del array
        System.out.println(arrayDinamico1.get(1)); // dos

        // Eliminación de elementos del array por su índice
        arrayDinamico1.remove(0);
        System.out.println(arrayDinamico1); // [dos, 3.0]

        // Eliminación de elementos por su valor
        arrayDinamico1.remove("dos"); 
        System.out.println(arrayDinamico1); // [3.0]


        System.out.print("\n");


        //          -------------------------------

        // Inicialización de array de tamaño dinámico vacío
        //   que admite valores de sólo un tipo
        ArrayList<String> arrayDinamico2 = new ArrayList<String>();

        //arrayDinamico2.add(1);
        // Si intentamos añadirle un valor de un tipo que no
        //   admite nos saldrá el siguiente error en tiempo
        //   de compilación:
        //   no suitable method found for add(int)

        arrayDinamico2.add("uno");
        arrayDinamico2.add("uno");
        arrayDinamico2.add("uno");
        arrayDinamico2.add("dos");

        // Eliminación de todos los elementos de un array 
        //   dado un cierto valor
        while(arrayDinamico2.remove("uno")) {};

        System.out.println(arrayDinamico2); // [dos]
	}
}