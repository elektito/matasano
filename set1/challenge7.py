from Crypto.Cipher import AES
from base64 import b64decode

cipher = AES.new('YELLOW SUBMARINE', mode=AES.MODE_ECB)
with open('7.txt') as i:
    data = i.read()

data = ''.join(i.strip() for i in data.split('\n'))
data = b64decode(data)
data = cipher.decrypt(data)
print data
