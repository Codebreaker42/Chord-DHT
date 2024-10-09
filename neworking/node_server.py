import socket 
import threading
import json 
from node import Node 

class NodeServer:
    def __init__(self, node: Node, port) -> None:
        self.node= node 
        self.port= port 

    def start(self):
        """ Start the server for listen the incoming requests"""

    def handle_request(self,client_socket):
        """ Handle incoming client request"""
