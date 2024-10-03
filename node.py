"""                           Node Class that Stores Data and Finger Table                          """
# use bits=160
from node import Node
from hash_util import hash_function

class Node:
    def __init__(self, node_id, bits=160) -> None:
        """ initialize the node attributes """
        self.node_id = node_id
        self.data= {}  #key value storage
        self.finger_table= [None]*bits 
        self.successor= None #store the successor node 
        self.predecessor= None  #store the predecessor node

    def store_data(self, key, value):
        """ Store the key value pair in the node"""
        self.data[key]= value

    def lookup_data(self , key:str):
        """ look up the key in the current node"""
        return self.data.get(key,None)


    def find_successor(self, key: str):
        """Find the successor node responsible for a given key"""
        pass
