from hashlib import sha256
from pwn import *
charset = string.ascii_letters + string.digits #+ string.punctuation

def xor(a, b):
    return bytes([i ^ j for i, j in zip(a, b)])

def H(m):
    return sha256(m).digest()

io = remote("83.136.252.32", 42278)
p = log.progress("flag")
last_flag = last_hash = new_hash = zero_xor_hash = ""
while zero_xor_hash == new_hash:
    flag_length = len(last_flag) + 1
    zero_xor_flag = "." * flag_length
    zero_xor_hash = H(xor(zero_xor_flag.encode(),
                          zero_xor_flag.encode())).hex()
    for c in charset:
        new_flag = last_flag + c
        io.recvuntil(b"> ")
        io.send(b"1\n")
        io.recvuntil(b": ")
        io.send(new_flag.encode() + b"\n")
        io.recvuntil(b": ")
        new_hash = io.recvline().decode().rstrip()
        if last_hash == new_hash:
            p.success(f"Success ! Your flag is {last_flag}")
            exit()
        if zero_xor_hash == new_hash:
            p.status(f"{new_hash} {new_flag}")
            last_flag = new_flag
            last_hash = new_hash
            break

p.failure(f"Failed !")
