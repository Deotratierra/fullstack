package main

import (
    "fmt"
)

// Nodo
type Node struct {
    Value int
}

func (n *Node) String() string {
    return fmt.Sprint(n.Value)
}

// Pila
type Stack []*Node

// Crea una nueva pila vacía
func NewStack() *Stack {
    return &Stack{}
}

// Añade un nodo a la pila
func (s *Stack) Push(n *Node) {
    *s = append(*s, n)
}

// Elimina y devuelve un nodo de la pila en orden LIFO
func (s *Stack) Pop() (n *Node) {
    x := len(*s) - 1
    n = (*s)[x]
    *s = (*s)[:x]
    return
}

func main() {
    s := NewStack()
	s.Push(&Node{1})
	s.Push(&Node{3})
	s.Push(&Node{5})

    s.Pop()

    for _, node := range *s {
        fmt.Printf("%v\n", node)
    }
}

/* Fuentes:
https://gist.github.com/moraes/2141121#gistcomment-1361598
*/
