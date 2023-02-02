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

    if(method == "encrypt"):
        print(encodeAffine(text, key_m, key_b))
    else:
        print(decodeAffine(text, key_m, key_b))
