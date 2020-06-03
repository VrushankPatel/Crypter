import hashlib 
import sys

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

    def getEncrypted(self,object,encryption):
        return getattr(object,encryption)()

sha = SHA("GeeksforGeeks")
print(sha.getEncrypted(sha,"sha256"))
print(sha.getEncrypted(sha,"sha384"))
print(sha.getEncrypted(sha,"sha224"))
print(sha.getEncrypted(sha,"sha512"))
print(sha.getEncrypted(sha,"sha1"))
print(sha.getEncrypted(sha,"md5"))