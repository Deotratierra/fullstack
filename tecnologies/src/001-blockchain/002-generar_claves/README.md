# Claves
En Bitcoin se usa la criptografía (asimétrica) para crear un par de claves que controlen el acceso a la red. La clave pública se usa para recibir fondos y la clave privada para firmar transacciones al enviar los fondos.

## Generación de claves
Con la bblioteca OpenSSL podemos crear una clave privada asociada a una clave pública mediante el tipo [EC_key](https://wiki.openssl.org/index.php/Manual:EC_KEY_new(3))

### Números criptográficamente seguros
Lo primero es generar un número al azar [criptográficamente seguro](https://en.wikipedia.org/wiki/Cryptographically_secure_pseudorandom_number_generator). Para ello podemos elegir varias opciones. El software de Bitcoin utiliza los generadores de números aleatorios del sistema para producir 256 bits de entropía (aleatoriedad). Usualmente, el generador aleatorio del sistema es inicializado por una fuente humana de aleatoriedad, por lo cual puede que te pida que muevas tu ratón por unos segundos.

El número debe estar comprendido entre `1` y `n-1` donde `n = 1.158 * 1077` (un poco menor que 2²⁵⁶). Para ello generamos un número aleatorio de 256 bits y comprobamos que sea menor que `n-1`.

En términos de programación, esto usualmente se lleva a cabo alimentando de una cadena de bits aleatoria más larga tomada de una fuente de aleatoriedad criptográficamente segura a un algoritmo SHA256, el cual produce un número de 256 bits. Si el resultado es menor que `n-1`, tenemos una clave privada adecuada, si no volvemos a intentarlo.


