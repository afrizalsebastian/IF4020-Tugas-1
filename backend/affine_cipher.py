import sys
import math

def modInv(a, m) -> int:
    return pow(a, -1, m)

def encodeAffine(text:str, key_m:int, key_b:int):
    if math.gcd(26,key_m) != 1:
        return False
    else:
        result = ""
        text = text.upper()
        for char in text:
            char_int = ord(char) - ord('A')
            result += chr(ord('A') + ((key_m*char_int + key_b) % 26) )
        return result

def decodeAffine(text:str, key_m:int, key_b:int):
    if math.gcd(26,key_m) != 1:
        return False
    else:
        result = ""
        text = text.upper()
        for char in text:
            char_int = ord(char) - ord('A')
            result += chr(ord('A') + (modInv(key_m,26)*(char_int-key_b) % 26) )
        return result

if __name__ == '__main__' :
    method = sys.argv[1]
    text = sys.argv[2]
    key_m = int(sys.argv[3])
    key_b = int(sys.argv[4])
    path = sys.argv[5]

    if(method == "encrypt"):
        cipher = encodeAffine(text, key_m, key_b)
        print(cipher)
        f = open(path, "w")
        f.write(cipher)
        f.close()
    else:
        plain = decodeAffine(text, key_m, key_b)
        print(plain)
        f = open(path, "w")
        f.write(plain)
        f.close()