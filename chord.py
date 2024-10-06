"""                                  Main Code Node Logic                             """

# join , Leave and Lookup 
from node import Node 
from hash_util import hash_function 


# join, leave and lookup operations 
class Chord:
    def __init__(self,bits=160):
        self.bits= bits
        self.nodes= [] #list of nodes in the system

    def add_node(self, node_id):
        """  Add a node to the chord ring"""
        # take the node id and create the node 
        node= Node(node_id,self.bits) #node creation 
        # integrating the node in the ring 
        self.nodes.append(node)

    def remove_node(self,node_id):
        """remove a node from the chord ring"""
        # logic for removing the node and redistributing its data 
        self.nodes= [node for node in self.nodes if node.node_id!= node_id] #stores the all node in list expect the given node 

    def lookup(self, key):
        """ Lookup the node responsible for key"""
        key_id = hash_function(key,self.bits)
        #logic for finding the responisble node
        # if there are no nods in a system return None 
        if not self.nodes:
            return None
        self.nodes.sort(key=lambda node: node.node_id)
        # finding which node is closest to the key 
        for node in self.nodes:
            if node.node_id>=key_id:
                return node 
        return self.nodes[0]     # If no node with node_id >= key_id is found, wrap around to the first node (circular nature)

        
