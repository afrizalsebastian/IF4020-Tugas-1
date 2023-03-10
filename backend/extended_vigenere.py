import sys

def encodeExtendedVigenere(text, key):
    result = ""
    idx = 0
    for char in text:
        key_ascii = ord(key[idx % len(key)])
        char_ascii = ord(char)
        result += chr((char_ascii + key_ascii) % 256)
        idx += 1
    return result

def decodeExtendedVigenere(text, key):
    result = ""
    idx = 0
    for char in text:
        key_ascii = ord(key[idx % len(key)])
        char_ascii = ord(char)
        result += chr((char_ascii - key_ascii + 256) % 256)
        idx += 1
    return result

if __name__ == '__main__' :
    method = sys.argv[1]
    text = sys.argv[2]
    key = sys.argv[3]
    path = sys.argv[4]

    if(method == "encrypt"):
        cipher = encodeExtendedVigenere(text, key)
        print(cipher)
        f = open(path, "w")
        f.write(cipher)
        f.close()
    else:
        plain = decodeExtendedVigenere(text, key)
        print(plain)
        f = open(path, "w")
        f.write(plain)
        f.close()