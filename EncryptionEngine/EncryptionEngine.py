import hashlib 
import sys
#from arc4 import ARC4


class EncryptionEngine:
    def sha256(self):
        return hashlib.sha256(self.str.encode()).hexdigest()

    def sha384(self):
        return hashlib.sha384(self.str.encode()).hexdigest()
    
    def sha224(self):
        return hashlib.sha224(self.str.encode()).hexdigest()

    def sha512(self):
        return hashlib.sha512(self.str.encode()).hexdigest()
    
    def sha1(self):
        return hashlib.sha1(self.str.encode()).hexdigest()

    def md5(self):
        return hashlib.md5(self.str.encode()).hexdigest()        

    def rc4(self):
        print(self.key)
        cipher = b'U7\x06\xdf\xd7\xb5d\x16^\xeb\xc7\x02\xdf'
        print(ARC4(self.key).decrypt(cipher))
        return ARC4(self.key).encrypt(self.str)        

    def getEncrypted(self,object,encryption,str,key): 
        self.key = key
        self.str = str       
        return getattr(object,encryption)()
'''
sha = EncryptionEngine("GeeksforGeeks","")
print(sha.getEncrypted(sha,"sha256"))
print(sha.getEncrypted(sha,"sha384"))
print(sha.getEncrypted(sha,"sha224"))
print(sha.getEncrypted(sha,"sha512"))
print(sha.getEncrypted(sha,"sha1"))
print(sha.getEncrypted(sha,"md5"))
print(sha.getEncrypted(sha,"rc4"))
print(sha.getEncrypted(sha,"rc4","Vrushank"))
'''