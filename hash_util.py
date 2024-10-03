"""                                                  Utility Function for Hashing                                         """

import hashlib #To change the data into the hash value

def hash_function(key:str, bits=160) -> int:
    """ Hashed the key using SHA-1 and returns the integer value in the range [0,2^bits-1]"""
    hash_bytes= hashlib.sha1(key.encode()).digest()
    hash_int= int.from_bytes(hash_bytes,byteorder='big')
    return hash_int%(2**bits)

# testing the code 
# print(hash_function("node2"))