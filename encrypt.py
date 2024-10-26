#ENCRYPTED STRING
def encrypt(s, k):
    enc = ""
    n = len(s)

    for i in range(n):
        j = (i + k) % n
        enc += s[j]

    return enc

s = input("STRING - ")
k = int(input("NUMBER - "))

print(encrypt(s, k))
