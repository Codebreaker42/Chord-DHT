"""                           Node Class that Stores Data and Finger Table                          """
# use bits=160
from hash_util import hash_function

class Node:
    def __init__(self, node_id, chord_ring, bits=160) -> None:
        """ initialize the node attributes """
        self.node_id = node_id
        self.bits= bits
        self.data= {}  #key value storage
        self.finger_table= [None]*bits 
        self.successor= None #store the successor node 
        self.predecessor= None  #store the predecessor node
        self.chord_ring= chord_ring #reference to the chord ring


    def store_data(self, key, value):
        """ Store the key value pair in the node"""
        self.data[key]= value

    def lookup_data(self , key:str):
        """ look up the key in the current node"""
        return self.data.get(key,None)
    
    def set_successor(self, successor_node):
        """ Set the successor of the current node in creation time"""
        self.successor= successor_node

    def set_predecessor(self, predecessor_node):
        """ Set the predecessor of the current node in creation time"""
        self.predecessor=predecessor_node

    def find_successor(self, key_id: int):
        """Find the successor node responsible for a given key"""
        if self.successor and self.node_id < key_id <= self.successor.node_id:
            """ If keys lies between current node and successor return successor"""
            return self.successor
        else:
            closest_preceding_node=self.closest_preceding_node(key_id) 
            if closest_preceding_node == self:
                return self.successor
            return closest_preceding_node.find_successor(key_id) #continue the lookup at preceding nodes

    def initialize_finger_table(self):
        """ Initialize the finger table for a given node"""
        # print(f"bits: {self.bits}")
        for ith_entry in range(self.bits):
            """calculate the target id for the ith finger:  (self.node_id+2^entry)%self.bits"""
            target_id= (self.node_id + 2 ** ith_entry)% (2**self.bits)
            self.finger_table[ith_entry]= self.find_successor(target_id)

    def closest_preceding_node(self, key_id: int):
        """ find the closest preceding node in the finget table for the given key_id"""
        for i in range(self.bits-1, -1, -1):
            finger= self.finger_table[i]
            if finger and self.node_id < finger.node_id <key_id:
                return finger # return the closest finger node preceding the key
            return self # if no finger is closer return the current finger
