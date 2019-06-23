public class HigherNumber {
    public static Integer mayor(Integer a, Integer b) {
    	if (a > b) {
    		return a;
    	} else {
    		return b;
    	}
    }

	public static void main(String[ ] arg) {
		System.out.println(mayor(3, 5));
	}
}

/*
Más fácil (sin importar nada):

Math.max(3, 5);
*/