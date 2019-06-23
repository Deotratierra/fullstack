import java.util.Scanner;

public class KeyboardInput {
	public static void main(String[ ] arg) {
        // Creamos un scanner que leerá la entrada del usuario
        Scanner keyboard = new Scanner(System.in);
        System.out.print("Escribe tu nombre: ");

        // Almacenamos la entrada del usuario en una variable
        String name = keyboard.nextLine();

        // Imprimimos el saludo completo
        System.out.println("Bienvenid@ a mi documentación, " + name + ".");
    }
}