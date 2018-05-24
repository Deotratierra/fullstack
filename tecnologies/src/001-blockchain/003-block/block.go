package main

import (
    "fmt"
    "time"
    //"bytes"
    "reflect"
    "encoding/binary"
    //"crypto/sha256"
)

type BasicBlock struct {
    Timestamp     int64
    PrevHash      []byte
    Hash          []byte
}

func NewBasicBlock(prevHash []byte) *BasicBlock {
    block := &BasicBlock{-1, prevHash, []byte{}}
    return block
}

func (block *BasicBlock) link(linked_block *BasicBlock) *BasicBlock {
    block.PrevHash = linked_block.Hash
    return block
}

func (block *BasicBlock) seal() *BasicBlock {
    block.Timestamp = time.Now().Unix()

    timestamp := make([]byte, 8)
    binary.LittleEndian.PutUint64(timestamp, uint64(block.Timestamp))

    data := append([]byte(timestamp), []byte(block.PrevHash)...)

    fmt.Printf("%s\n", reflect.TypeOf(data))

    //block.Hash = sha256.Sum256(data)

    return block
}

func main(){
    b1 := NewBasicBlock([]byte{})
    b2 := NewBasicBlock([]byte{})

    b1.seal()
    fmt.Printf("%d\n", b2.Hash)
}