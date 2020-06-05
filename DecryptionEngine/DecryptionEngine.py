import hashlib 
import sys
from arc4 import ARC4


class SHA:
    def __init__(self,str):
        self.str = str

    def rc4(self,param):
        return ARC4(param['key']).decrypt(param['cipher'])        

    def getDecrypted(self,object,decryption,param):
        if param:
            return getattr(object,decryption)(param)        
        return getattr(object,decryption)()

cipher = b'U7\x06\xdf\xd7\xb5d\x16^\xeb\xc7\x02\xdf'

print(sha.getEncrypted(sha,"rc4",{'key':"Vrushank",'cipher':cipher}))
