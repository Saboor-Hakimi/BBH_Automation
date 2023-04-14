
import base64
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Hash import MD5


enc = "ED1nf3uLW4Hkwr1aGw+NpN5sgcRMPCFuk0XgtW181m4o6d0Ml3D/j6h1NSyOh4dbcGsbK6rcZOUyzHxWVb4QkA=="
enc = base64.b64decode(enc)

IV = enc[0:16]
data = enc[16:]

result = []
for i in range(9999):
    str2 = str(i).zfill(4)

    # get md5 of str2
    h = MD5.new()
    h.update(str2.encode())
    key = h.digest()[0:16]


    try:
        # AES/CBC/PKCS5Padding decrypt enc
        aes = AES.new(key, AES.MODE_CBC, IV)
        tmp = aes.decrypt(data)
        result.append(tmp)

    except:
        pass


# print(result)
for line in result:
    if str(line).count("-") == 4:
        print(line)