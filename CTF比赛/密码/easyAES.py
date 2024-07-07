import os
from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long

flag = "vmc{****************}" # 未知

message = b"Welcome to NCC, hope you be happy in today's CTF!! Come on!!!!!!"

key = b"****************"  # 未知
init_vector = flag.replace("vmc{", "").replace("}", "").encode()
key_len = len(key)


r = os.urandom(4) * 8
gift = bytes_to_long(r) ^ bytes_to_long(key)


def encrypttttt(msg):
    aes = AES.new(key, AES.MODE_CBC, init_vector)
    res = aes.encrypt(msg)
    return res


print(key_len)
print(gift)
print(hex(bytes_to_long(encrypttttt(message)))[-32:])

"""
16
50455174541563286575772300159154005086016143694349352802282206363407615655565
b290f7b4894c5b7609fe52de49d0c4fe
"""