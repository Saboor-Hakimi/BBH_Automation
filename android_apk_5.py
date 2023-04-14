str1 = "i]\rD\u0004\u0015\u0017\u0004_~\u0002\u0006`HZ@UBY\\Ku\u0002O2\u0003_MQB\u0010\u0007G~\u0004Q"

result = []
for i in range(9999):
    str2 = "PentesterLab"
    tmp = ""
    for i in range(len(str1)):
        tmp += (chr(ord(str1[i])^ord(str2[i%len(str2)])))
    result.append(tmp)

print(result)
