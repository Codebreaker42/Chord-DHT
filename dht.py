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
    
if __name__ == "__main__":
    chord= Chord()
    dht= DHT(chord)
    chord.add_node(hash_function("node1",4))
    # chord.add_node(hash_function("node2"))
    # dht.put("fruit","apple")
    # print(f'{dht.get("fruit")}')
    for key, node in enumerate(chord.nodes):
        print(f"{key} : {node}")
        print(f" node_id: {node.node_id} , successor : {node.successor} , predecessor : {node.predecessor}")
        print("finger table: ")
        for idx, key_id in enumerate(node.finger_table):
            print(f" {idx}  :  {key_id}")
    # print(chord.remove_node(hash_function("node2")))
    # for key, node in enumerate(chord.nodes):
    #     print(f"{key} : {node}")
    #     print(f" node_id: {node.node_id} , successor : {node.successor} , predecessor : {node.predecessor}")
    
