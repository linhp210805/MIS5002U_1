import unicodedata

def remove_diacritics(s: str) -> str:
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def preprocess(name: str) -> str:
    s = remove_diacritics(name)
    s = ''.join(ch for ch in s if ch.isalpha()) 
    return s.upper()

def caesar_encrypt(plaintext: str, k: int) -> str:
    k = k % 26
    out_chars = []
    for ch in plaintext:
        idx = ord(ch) - ord('A')         
        cidx = (idx + k) % 26
        out_chars.append(chr(cidx + ord('A')))
    return ''.join(out_chars)

def main():
    TenCuaBan = "PhuongLinh"   
    STT = 17           
    P = preprocess(TenCuaBan)
    k = STT % 26
    C = caesar_encrypt(P, k)

    print("Plaintext (sau tiền xử lý):", P)
    print("K (STT mod 26):", k)
    print("Ciphertext:", C)

if __name__ == "__main__":
    main()
