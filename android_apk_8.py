
import base64
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Hash import MD5


enc = "G38zckAufW4B9A6sywz28kzgW8CCx1UWugLUTjKlo/kwV1CVesmr0tPX/JZOW0aik0TlkrcAIZZ/G0BigUtmeg=="
enc = base64.b64decode(enc)

IV = enc[0:16]
data = enc[16:]

result = []
for i in range(9999):
    str2 = str(i).zfill(4)

    # get md5 of str2
    h = MD5.new()
    h.update(str("<=== P3nt3st3rL4b ===>" + str2).encode("utf-8"))
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