"""                               DHT Implementation  and Network Management               """
from node import Node
from chord import Chord
from hash_util import hash_function

class DHT:
    def __init__(self, chord: Chord) -> None:
        self.chord= chord #stores the chord instance inside the DHT object.


    def put(self,key,value):
        """ Store the key value pair in the appropriate node using finger table lookup"""
        key_id= hash_function(key) #determines which node in chord network responsible for storing key
        node = self.chord.find_successor(key_id) #find the node using finger table 
        node.store_data(key,value)

    def get(self, key):
        """ Retrieve value for a key from the appropriate node using finget table lookup"""
        key_id= hash_function(key)
        node= self.chord.find_successor(key_id) #find the node using finger table
        return node.lookup_data(key)
    