# base58

Es un esquema de codificación de binario a texto, usada para representar grandes enteros como un número determinado de caracteres alfanumérico.

La codificación en base58 fue creada expresamente para el Bitcoin. Es igual que la codificación en base64 pero sin incluir los caracteres "+", "-", "1", "l", "0" y "O", los cuales pueden causar confusión ya que esta codificación es usada para las direcciones de monederos que los usuarios deben copiar y pegar en las interfaces gráficas.

Este encriptado sólo puede codificar números enteros. Si queremos codificar una cadena primero debemos decidir como interpretarla como entero, lo cual puede hacerse, por ejemplo, aplicando una codificación en base 128.