public class Ascii{
	public static void main(String[ ] arg) {
		String caracter = "a";

		// Casteamos a entero el primer caracter de la cadena
		//   (en Java String != Character)
		Integer caracterEnAscii = (int) caracter.charAt(0);
		
		System.out.println(
			"El caracter \"" + caracter + "\" en ASCII es "
			    + caracterEnAscii + ".");
	}
}