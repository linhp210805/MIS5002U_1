k = 17
plaintext = "TranLePhuongLinh"

ciphertext = ""

for ch in plaintext:
    if ch.isalpha():  
        base = ord('A') if ch.isupper() else ord('a')
        ciphertext += chr((ord(ch) - base + k) % 26 + base)
    else:
        ciphertext += ch

print("k :", k)
print("Plaintext :", plaintext)
print("Ciphertext:", ciphertext)
