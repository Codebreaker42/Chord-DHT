import threading
from chord import Chord
from node import Node 
from node_server import NodeServer
from node_client import NodeClient

class ChordNetwork:
    def __init__(self, chord: Chord) -> None:
        self.chord= chord

    def start_nodes(self,node_ports):
        """Start the node servers for each node in the chord ring"""

    def send_request(self, node_id, request_type, key, value= None):
        """ Send  a request to a specific node in the network."""