def crypt(data, key):
    res=""
    for a in data:
         res=res+chr(ord(a)^key)
    return res
def decrypt(data,key):
    return crypt(data,key)
    
print(crypt("Test",45))
print(decrypt("yH^Y",45))