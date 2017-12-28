El siguiente artículo es una traducción al español resumida realizada por [Álvaro Mondéjar Rubio](https://github.com/mondeja) del original [Bytes and hashes](http://davidederosa.com/basic-blockchain-programming/bytes-and-hashes/), publicado por [Davide De Rosa](http://davidederosa.com/).

## Bytes y hashes
Antes de comenzar, ten en mente que casi todas las estructuras de datos blockchain se serializan en forma [little-endian](http://en.wikipedia.org/wiki/Endianness#Little-endian), mientras algunos objetos (como las direcciones de red) mantienen la ordenación de bytes [big-endian](http://en.wikipedia.org/wiki/Endianness#Big-endian).

### Las funciones de hash de Bitcoin
En lo que a nosotros respecta, una funció hash](https://es.wikipedia.org/wiki/Funci%C3%B3n_hash) traduce una cantidad arbitraria de bytes en una fija. Olvídate de las propiedades de no reversibilidad y otras porque esa es la que nos interesa por ahora. Entre otros, Bitcoin confía en los hashes para algunos propósitos principales:

- Identificadores
- Direcciones
- Firmas de transacción
- [Sumas de verificación](https://es.wikipedia.org/wiki/Suma_de_verificaci%C3%B3n)

Bitcoin es muy interesante ya que adoptó un isistema bien establecido, a veces conceptos básicos de ciencias de la computación para crear algo alucinantemente innovador. Los hashes no son una excepción,ya que Satoshi usó combinaciones de [SHA-2](https://es.wikipedia.org/wiki/SHA-2) y [RIPEMD](https://en.wikipedia.org/wiki/RIPEMD) en lugar de definir sus propias funciones criptográficas.

Específicamente, él introdujo dos funciones de hash compuestas:

- hash256(d) = SHA-256(SHA-256(d))
- hash160(d) = RIPEMD-160(SHA-256(d))

donde SHA-256 es una variante de 256  bits de SHA-2, RIMPEMD-160 es una variante de 160 bits de RIPEMD y *d* es una array de byts genérico. No es de extrañar que las funciones hash256 y hash160 devuelvan arrays de 256
bits (32 bytes) y 160 bits (20 bytes) respectivamente.

¿Cual fue el motivo de elegir el doble hashing, personal o de seguridad? Lo siento por no ser un friki de la cryptografía pero basándome en [algunas discusiones](https://bitcointalk.org/index.php?topic=45456.0) parece que no quedó muy claro por la desaparición de Satoshi.

### Hash256 para identificadores
Si estás un poco familiarizado con cualquier monedero o explorador de bloques en la web te has topado con el hash256 al menos una vez, debido a que es el tipo de hash que Bitcoin usa para identificar las entidades nucleares: *bloques* y *transacciones*.

Condsidera el link a [este bloque] o [esta transacción] en la blockchain, sáltate las partes que no entiendas y enfócate en el último componente de ambas URLs. Esas largas cadenas son claves primarias en la base de datos de la cadena de bloques, accedes a un bloqe único con ese identificador y ningún otro bloque tendrá jamás el mismo identificador. QUizás habrás notado que comparten el mismo largo, 64 caracteres.

Ambas está heachas de dígitos headecimales (0-9 a-f). Cada par hex representa un solo byte de información y haciendo matemáticas encontrarás que 64 dígitos hex es un array de 32 bytes, como en hash256. De hecho, ambos identificadores resultan de un cálculo de hash256:

- block_id = hash256(block.header)
- transaction_id = hash256(transaction)

Nos sumergiremos en bloques y transacciones más tarde, pro estas es una de las aplicaciones del hash256 que vale la pena señalar desde el principio.
También señalar que los hash160 reinan en otra área estratégica del ecosistema Bitcoin: las *direcciones*.

### Hashes en la red
Los bloques y transacciones siguen la regla little-endian y esa es la razón de porqué tus primeros intentos de realizar una transacción en crudo pueden ser un puzzle cuando consultas los exploradores web. Por ejemplo, toma una cadena de 64 caracteres de largo en la siguiente transacción (a veces llamado *txid*) como se ve en [blockchain.info](https://blockchain.info/) y divídela en 32 grupos de 2 dígitos (un byte cada uno):

```
46 28 71 64 db 45 a7 8a
91 96 25 7d a4 5b 62 88
1e 39 4a 3d 11 fb 40 39
43 bb bf 8e c4 aa f9 ee
```



