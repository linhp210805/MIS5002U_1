# RSA with p=17, q=23, e=5
# Plaintext "Phuonglinh"

def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("No modular inverse")
    return x % m

p = 17
q = 23
e = 5
plaintext = "Phuonglinh"   

n = p * q
phi = (p - 1) * (q - 1)
d = modinv(e, phi)

print("Khóa công khai (n, e) =", (n, e))
print("Khóa bí mật (n, d)   =", (n, d))

max_block_bytes = 1

data = plaintext.encode("utf-8")
blocks = [data[i:i + max_block_bytes] for i in range(0, len(data), max_block_bytes)]

cipher_blocks = [pow(int.from_bytes(block, "big"), e, n) for block in blocks]

print("\nCiphertext (các số nguyên):")
print(cipher_blocks)



# GIẢI MÃ 
decrypted_blocks = [pow(c, d, n) for c in cipher_blocks]
recovered = b"".join(
    [db.to_bytes((db.bit_length() + 7) // 8 or 1, "big") for db in decrypted_blocks]
).decode("utf-8")

print("\nGiải mã thu được:")
print(recovered)
