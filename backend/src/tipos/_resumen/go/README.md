## Tipos en Golang

#### bool
- Es un entero especial de 1 bit.
- Operadores lógicos: `&&` (and), `||` (or) y `!` (not).

#### string
- Las cadenas en Go están compuestas de bytes individuales, usualmente uno por caracter.

#### int, uint, uintptr
- El tamaño depende de la arquitectura (32 bits en sistemas de 32 bits ó 64 en sistemas de 64).

#### int8, int16, int32, int64
- Números enteros con o sin signo.
- Su tamaño en bits lo indica el número en el nombre del tipo.

#### uint8, uint16, uint32, uint64
- Números enteros sin signo.
- Su tamaño en bits lo indica el número en el nombre del tipo.

#### byte
- Alias para **uint8**, debido a que un byte son 8 bits sin signo (no tiene sentido un número binario negativo).

#### rune
- Representa un punto de código Unicode.
- Alias para **int32**, debido a que son enteros de 4 bytes. Tan sólo se necesita un byte para representar el alfabeto ASCII, pero esto puede aumentar hasta 4 bytes para representar el alfabeto Unicode.

#### float32, float64
- Los números de punto flotante son inexactos. Por ejemplo, el cálculo de `1.01 - 0.99 = 0.020000000000000018`.
- Su tamaño en bits lo indica el número en el nombre del tipo.
- El tipo **float64** tiene más precisión que el tipo **float32**.

#### complex64, complex128