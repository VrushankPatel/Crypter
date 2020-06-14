import hashlib 
import sys
from arc4 import ARC4

class DecrytionEngine:
    def __init__(self,str):
        self.str = str

    def rc4(self,param):
        return ARC4(self.key).decrypt(self.cipher)

    def getDecrypted(self,object,decryption,cipher,key): 
        self.cipher = cipher
        self.key = key
        return getattr(object,decryption)()
