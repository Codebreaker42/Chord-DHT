"""                                  Main Code Node Logic                             """

# join , Leave and Lookup 
from node import Node 
from hash_util import hash_function 


# join, leave and lookup operations 
class Chord:
    def __init__(self,bits=160):
        self.bits= bits
        self.nodes= [] #list of nodes in the system

    def add_node(self, node_id ):
        """  Add a node to the chord ring"""
        # take the node id and create the node 
        new_node= Node(node_id,15,self.bits) #node creation 

        if not self.nodes:
            """ for first node in the ring"""
            new_node.set_successor(new_node)
            new_node.set_predecessor(new_node)
        else:
            # find where to place the node 
            successor_node= self.find_successor(node_id) #calling the successor function 
            predecessor_node= successor_node.predecessor#predecessor of successor node become the predecessor of current node

            new_node.set_successor(successor_node) #set the successor
            new_node.set_predecessor(predecessor_node) #set the predecessor

            successor_node.set_predecessor(new_node) #current node become the predecessor of current node's seccessor_node
            predecessor_node.set_successor(new_node) #current node become the successor of current node's predecessor node

        new_node.initialize_finger_table() 
        self.nodes.append(new_node)
        self.nodes.sort(key= lambda x: x.node_id)


    def remove_node(self,node_id):
        """remove a node from the chord ring and transfer the information to its successor"""

        # find the node to be removed
        node_to_remove= next((node for node in self.nodes if node.node_id== node_id),None)
        if not node_to_remove:
            """ if node is not found which need to remove"""
            print(f"Node {node_id} not found in dht")
            return 
        
        # transfer the data to its successor
        successor_node= node_to_remove.successor
        predecessor_node = node_to_remove.predecessor
        if successor_node:
            for key,value in node_to_remove.data.items():
                successor_node.store_data(key,value)

        # updating the successor and predecessor link 
        if predecessor_node:
            predecessor_node.set_successor(successor_node)
        if successor_node:
            successor_node.set_predecessor(predecessor_node)

        # removing the node from the ring 
        self.nodes= [node for node in self.nodes if node.node_id != node_id]

        # updating the finger table of all other remaining nodes 
        for node in self.nodes:
            node.initialize_finger_table()
        print(f"Node {node_id} has left the dht.")


    def lookup(self, key):
        """ Lookup the node responsible for key"""
        key_id = hash_function(key,self.bits)
        # if there are no nods in a system return None 
        if not self.nodes:
            return None
        # finding which node is closest to the key 
        for node in self.nodes:
            if node.node_id>=key_id:
                return node 
        return self.nodes[0]     # If no node with node_id >= key_id is found, wrap around to the first node (circular nature)

    def find_successor(self, key_id):
        """ Find the successor node resposible for the given key_id"""
        if not self.nodes:
            return None
        # start lookup from the first table 
        return self.nodes[0].find_successor(key_id)

        
