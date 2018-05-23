package base58

import (
    "fmt"
    "math/big"
)

// Esquema de una codificación en base58
type Base58Encoding struct {
    alphabet  [58]byte
    decodeMap [256]int64
}

// Crea una estructura para la codificación
// de un alfabeto en base 58
func newBase58Encoding(alphabet []byte) *Base58Encoding {
    enc := &Base58Encoding{}
    copy(enc.alphabet[:], alphabet[:])
    for i := range enc.decodeMap {
        enc.decodeMap[i] = -1
    }
    for i, b := range enc.alphabet {
        enc.decodeMap[b] = int64(i)
    }
    return enc
}

func ShowBase58Encoding(encoding *Base58Encoding) string {
    response := fmt.Sprintf("%#v", encoding)
    fmt.Printf("%s\n", response)
    return response
}

// FlickrEncoding es el esquema de codificación usado por el acortador de urls de Flickr
var FlickrEncoding = newBase58Encoding([]byte("123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"))

// RippleEncoding es el esquema de codificación usado par las direcciones de Ripple
var RippleEncoding = newBase58Encoding([]byte("rpshnaf39wBUDNEGHJKLM4PQRST7VWXYZ2bcdeCg65jkm8oFqi1tuvAxyz"))

// BitcoinEncoding es el esquema de codificación usado par las direcciones de Bitcoin
var BitcoinEncoding = newBase58Encoding([]byte("123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"))

// Base 58   ("radix" == "base")
var radix = big.NewInt(58)

// Base58Encode codifica un array de bytes a Base58
//func Base58Encode(input []byte) []byte {
//
//}

// Función que da la vuelta a un array de bytes
func reverse(data []byte) {
    for i, j := 0, len(data)-1; i < j; i, j = i+1, j-1 {
        data[i], data[j] = data[j], data[i]
    }
}

// Esta función es aplicada a una estructura Base58Encoding
// y codifica un array de bytes de tipo numérico
func (encoding *Base58Encoding) Base58Encode(src []byte) ([]byte, error) {
    if len(src) == 0 {
        return []byte{}, nil
    }
    n, ok := new(big.Int).SetString(string(src), 10)
    if !ok {
        return nil, fmt.Errorf("expecting a number but got %q", src)
    }
    bytes := make([]byte, 0, len(src))
    for _, c := range src {
        if c == '0' {
            bytes = append(bytes, encoding.alphabet[0])
        } else {
            break
        }
    }
    zerocnt := len(bytes)
    mod := new(big.Int)
    zero := big.NewInt(0)
    for {
        switch n.Cmp(zero) {
        case 1:
            n.DivMod(n, radix, mod)
            bytes = append(bytes, encoding.alphabet[mod.Int64()])
        case 0:
            reverse(bytes[zerocnt:])
            return bytes, nil
        default:
            return nil, fmt.Errorf("expecting a positive number in base58 encoding but got %q", n)
        }
    }
}

func (encoding *Base58Encoding) Base58Decode(src []byte) ([]byte, error) {
    if len(src) == 0 {
        return []byte{}, nil
    }
    var zeros []byte
    for i, c := range src {
        if c == encoding.alphabet[0] && i < len(src)-1 {
            zeros = append(zeros, '0')
        } else {
            break
        }
    }
    n := new(big.Int)
    var i int64
    for _, c := range src {
        if i = encoding.decodeMap[c]; i < 0 {
            return nil, fmt.Errorf("invalid character '%c' in decoding a base58 string \"%s\"", c, src)
        }
        n.Add(n.Mul(n, radix), big.NewInt(i))
    }
    return n.Append(zeros, 10), nil
}
