# Bloques

La estructura básica de un bloque sería (python):

```python
class Block:
    def __init__(self):
        self.timestamp = None
        self.prev_hash = None
        self.hash = None
        # ...
```

Podemos añadir la información que queramos a parte a los bloques, depende de los objetivos de la implementación.

Una algo más compleja sería (golang):

```go
type Block struct {
    Timestamp     int64
    Transactions  []*Transaction
    PrevHash      []byte
    Hash          []byte
    Nonce         int  // https://en.wikipedia.org/wiki/Cryptographic_nonce
    Height        int
}
```

En este ejemplo se incluye un array de transacciones, por lo que podemos deducir que estos bloques han sido creados para almacenar transacciones.

## Campos básicos
Los campos comunes a la mayoría de implementaciones de cadenas de bloques son:

- `timestamp`: Marca de tiempo en segundos Unix necesaria para determinar cuando fue creado este bloque.
- `prev_hash`: El hash del bloque previo. Esto asegura que cada bloque vaya después del anterior en la cadena.
- `hash`: El hash del bloque, corresponde al valor almacenado en el campo `prev_hash` del próximo bloque en la cadena.



___________________________

#### Fuentes:
- https://github.com/davecan/easychain/blob/master/blockchain.py
- https://github.com/Jeiwan/blockchain_go/blob/master/block.go