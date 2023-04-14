str ="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".encode()
str_enc="b6a90c3BVh7irf5h0KHBQYlauiew09iutFHvxD3fu0VYUX56wVFVjIYlAIoK gfY/vjUDRrqrLck7ZKcgoRo="

key_enc="N/K/gMqTARuuqaYzhO2URo0K9iez1Nvi5QO/wT/cvhIMA3p/"



import base64

key_enc=base64.b64decode(key_enc)
str_enc=base64.b64decode(str_enc)




def xor(str1, str2):
    return [(a^b) for a,b in zip(str1, str2)]

key = xor(xor(str_enc, key_enc), str)
print(key)

key_str = [chr(i) for i in key]
print("".join(key_str))