import hashlib 
import sys
import RC4

class SHA:
    def __init__(self,str):
        self.str = str

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

    def rc4(self,key):
        print(key)
        return RC4.rc4crypt(self.str,key)

    def getEncrypted(self,object,encryption,param):
        if param:
            return getattr(object,encryption)(param)
        else:
            return getattr(object,encryption)()

sha = SHA("GeeksforGeeks")
print(sha.getEncrypted(sha,"sha256",None))
print(sha.getEncrypted(sha,"sha384",None))
print(sha.getEncrypted(sha,"sha224",None))
print(sha.getEncrypted(sha,"sha512",None))
print(sha.getEncrypted(sha,"sha1",None))
print(sha.getEncrypted(sha,"md5",None))
print(sha.getEncrypted(sha,"rc4","Vrushank"))
