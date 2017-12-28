#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# El siguiente código está extraido de:
# https://github.com/dvf/blockchain/blob/master/blockchain.py
# https://hackernoon.com/learn-blockchains-by-building-one-117428612f46

import hashlib
import json
from time import time
from urllib.parse import urlparse

class Blockchain:
    def __init__(self):
        self.current_transactions = []
        self.chain = []
        self.nodes = set()

        # Creamos el bloque genesis
        self.new_block(previous_hash="1", proof=100)

    def register_node(self, address):
        """Agrega un nuevo nodo a la lista de nodos

        Args:
            address (str): Dirección del nodo,
                por ejemplo "http://192.168.0.5:5000"
        """
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def valid_chain(self, chain):
        """Determina si una cadena de bloques es válida

        Args:
            chain (list): Cadena de bloques

        Returns (bool):
            True si es válida, False en caso contrario
        """
        last_block = chain[0]  # Último bloque (primero en la lista)
        current_index = 1      # Empezamos a contar por el segundo bloque

        while current_index < len(chain): # Nos olvidamos del primer bloque (<)
            block = chain[current_index]  # Bloque a bloque
            #print(last_block)
            #print(block)
            #print("\n-----------\n")

            # Comprobamos que el hash del bloque es correcto
            if block['previous_hash'] != self.hash(last_block):
                return False

            # Comprobamos que la Prueba de Trabajo es correcta
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False

            last_block = block
            current_index += 1

        return True

    def resolve_conflicts(self):
        """Algoritmo de consenso, resuelve conflictos
        reemplazando la cadena con la más larga en la red

        Returns (bool):
            True si la cadena ha sido reemplazada,
            False en caso contrario
        """
        neighbours = self.nodes
        new_chain = None

        # Estamos buscando cadenas más largas que la nuestra
        max_length = len(self.chain)

        # Coge y verifica las cadenas de todos los nodos en la web
        for node in neighbours:
            response = requests.get("http://%s/chain" % node)

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                # Comprueba si el largo es mayor y la cadena es válida
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        # Reemplaza nuestra cadena si hemos encontrado una válida
        # más larga que la nuestra
        if new_chain:
            self.chain = new_chain
            return True

        return False

    def new_block(self, proof, previous_hash):
        """
        Crea un nuevo bloque en la blockchain

        Args:
            proof: La prueba dada por el algoritmo de prueba de trabajo
            previous_hash: Has del bloque previo

        Returns:
            Nuevo bloque
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),   # Cada bloque nuevo guarda las transacciones actuales
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reseteamos la lista actual de transacciones
        self.current_transactions = []

        # Añadimos el nuevo bloque a la cadena
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Crea una nueva transacción que irá en el próximo bloque minado

        Args:
            sender (str): Dirección del remitente
            recipient (str): Dirección del receptor
            amount (float): Cantidad

        Returns (int):
            Índice del bloque que llevará a cabo esta transacción
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        # La transacción será efectuada por el próximo bloque
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        """Último bloque"""
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """Crea un hash SHA-256 del bloque

        Args:
            block (dict): Bloque
        """

        # Debemos asegurarnos de que el diccionario esté ordenado,
        # o tendremos hashes inconsistentes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        """Simple algoritmo de Prueba de Trabajo:
            Busca un número p_1 tal que el final del hash de p_1·p_2 contenga 4 ceros,
            donde p_2 es la prueba previa y p1 es la nueva
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validación de la prueba de trabajo

        Args:
            last_proof: Prueba previa
            proof: Prueba actual

        Returns:
            True si es correcta, False si no.
        """
        guess = "{}{}".format(last_proof, proof).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

from pprint import pprint

# Creamos una nueva blockchain
blockchain = Blockchain()
pprint(blockchain.chain) # Vemos sólo el bloque génesis en la cadena

# Registramos un nuevo nodo a la red
blockchain.register_node("http://192.168.0.5:5000")
pprint(blockchain.nodes) # Vemos el nuevo nodo

# Creamos una nueva transacción
blockchain.new_transaction("Bob", "Alice", 0.45)
pprint(blockchain.current_transactions)


