class Pareja {
	private int n1;
	private int n2;

	// Constructor
	public Pareja(int n1, int n2) {
		this.n1 = n1;
		this.n2 = n2;
	}

	/**
	 * Sobrecarga de representación como cadena de caracteres
	 *
	 * Por defecto, el método `toString` de una clase incluye
	 *   la siguiente implementación:
	 *
	 *     public String toString() {
     *         return getClass().getName() + "@" + Integer.toHexString(hashCode());
     *     }
     **/
	@Override
	public String toString() {
		return "Pareja(" + this.n1 + ", " + this.n2 + ")";
	}

	/**
	 * En Java, no podemos realizar sobrecarga de operadores,
	 *   como por ejemplo `pareja1 + pareja2`. Para realizarlo
	 *   necesitaríamos el paquete `java-oo` http://amelentev.github.io/java-oo/
	 * Sin embargo, podemos realizar la siguiente implementación:
	 **/
	public Pareja add(Pareja other) {
		return new Pareja(this.n1 + other.n1, this.n2 + other.n2);
	}
}

public class Overload {
	public static void main(String [] arg) {

		// Representación como cadena
		Pareja pareja1 = new Pareja(1, 2);
		System.out.println(pareja1);  // Pareja(1, 2)

		// Sobrecarga de suma mediante método (sin sobrecarga real)
		Pareja pareja2 = new Pareja(1, 2);
		System.out.println(pareja1.add(pareja2)); // Pareja(2, 4)
	}
}

/**
 * Fuentes:
 *   - https://stackoverflow.com/questions/27647567/how-can-i-support-println-in-a-class
 *   - https://stackoverflow.com/questions/8375229/is-it-possible-to-overload-operators-in-java
 **/