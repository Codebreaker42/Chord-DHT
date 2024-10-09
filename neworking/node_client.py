import socket 
import json 

class NodeClient:
    def __init__(self,host, port) -> None:
        self.host= host
        self.port= port 

    def send_request(self,request_type, key, value=None):
        """ Send a request to the node server """
