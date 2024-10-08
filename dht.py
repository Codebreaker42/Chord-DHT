"""                               DHT Implementation  and Network Management               """
from node import Node
from chord import Chord
from hash_util import hash_function

class DHT:
    def __init__(self, chord: Chord) -> None:
        self.chord= chord #stores the chord instance inside the DHT object.


    def put(self,key,value):
        """ Store the key value pair in the appropriate node"""
        key_id= hash_function(key) #determines which node in chord network responsible for storing key
        node = self.chord.lookup(key) #find the node responsible for storing the data associated with this key
        node.store_data(key,value)

    def get(self, key):
        """ Retrieve value for a key from the appropriate node"""
        key_id= hash_function(key)
        node= self.chord.lookup(key)
        return node.lookup_data(key)
    