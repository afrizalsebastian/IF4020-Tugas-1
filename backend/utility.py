import math
# Extended Vigenere
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

# Affine Cipher

# m bernilai 25, 26, atau 27 karena jumlah alphabet 26. (Atau ini buat pakai seluruh karakter?)
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

# Playfair Cipher
def create_matrix(key):
    matrix = []
    key = key.upper().replace("J", "")
    key = key.upper().replace(" ", "")
    for char in key:
        if char not in matrix:
            matrix.append(char)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def get_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return (i, row.index(char))
    return None

def encodePlayfair(text, key):
    matrix = create_matrix(key)
    text = text.upper().replace("J", "I")
    text = text.upper().replace(" ", "")

    # Sisipkan huruf
    conv_text = ""
    for i in range(len(text) - 1):
        if text[i] == text[i+1]:
            conv_text += text[i] + 'X'
        else:
            conv_text += text[i]
    conv_text += text[len(text)-1]

    if len(conv_text) % 2 == 1:
        conv_text += 'X' 
    result = []
    for i in range(0, len(conv_text), 2):
        char1 = conv_text[i]
        char2 = conv_text[i + 1]
        pos1 = get_position(matrix, char1)
        pos2 = get_position(matrix, char2)
        if pos1[0] == pos2[0]:
            result.append(matrix[pos1[0]][(pos1[1] + 1) % 5])
            result.append(matrix[pos2[0]][(pos2[1] + 1) % 5])
        elif pos1[1] == pos2[1]:
            result.append(matrix[(pos1[0] + 1) % 5][pos1[1]])
            result.append(matrix[(pos2[0] + 1) % 5][pos2[1]])
        else:
            result.append(matrix[pos1[0]][pos2[1]])
            result.append(matrix[pos2[0]][pos1[1]])
    
    return "".join(result)

def decodePlayfair(text, key):
    matrix = create_matrix(key)
    text = text.upper().replace(" ", "")

    result = []
    for i in range(0, len(text), 2):
        char1 = text[i]
        char2 = text[i + 1]
        pos1 = get_position(matrix, char1)
        pos2 = get_position(matrix, char2)
        if pos1[0] == pos2[0]:
            result.append(matrix[pos1[0]][(pos1[1] - 1) % 5])
            result.append(matrix[pos2[0]][(pos2[1] - 1) % 5])
        elif pos1[1] == pos2[1]:
            result.append(matrix[(pos1[0] - 1) % 5][pos1[1]])
            result.append(matrix[(pos2[0] - 1) % 5][pos2[1]])
        else:
            result.append(matrix[pos1[0]][pos2[1]])
            result.append(matrix[pos2[0]][pos1[1]])
    
    return ("".join(result)).replace("X","")

# Hill Cipher
import numpy as np

def encodeHill(text, key):
    text = [ord(c) - ord('A') for c in text.upper()]
    blocks = [text[i:i + key.shape[0]] for i in range(0, len(text), key.shape[0])]
    result = []
    for block in blocks:
        block = np.pad(block, (0, key.shape[0] - len(block)), mode='constant')
        block = np.dot(key, block) % 26
        result.extend(block)
    return ''.join([chr(c + ord('A')) for c in result])

def decodeHill(text, key):
    text = [ord(c) - ord('A') for c in text.upper()]
    # Inverse matriks pakai linalg jadi float64. Ga bisa dipakai. Masih bingung mau gunakan apa
    inv_key = np.linalg.inv(key) % 26
    blocks = [text[i:i + key.shape[0]] for i in range(0, len(text), key.shape[0])]
    result = []
    for block in blocks:
        block = np.pad(block, (0, key.shape[0] - len(block)), mode='constant')
        block = np.dot(inv_key, block) % 26
        result.extend(block)
    return ''.join([chr(c + ord('A')) for c in result])

# test extended vigenere
'''text = "Ghebyon ganteng bet xi!@#'"
key = "awok"
encoded = encodeExtendedVigenere(text, key)
print(encoded)
decoded = decodeExtendedVigenere(encoded, key)
print(decoded)'''

# test affine
'''m = 7
b = 10
text = "kripto"
encoded = encodeAffine(text, m, b)
print(encoded)
decoded = decodeAffine(encoded, m, b)
print(decoded)'''

# test playfair
'''key = "JALAN GANESHA SEPULUH"
text = "temui ibu nanti malam"
encoded = encodePlayfair(text, key)
print(encoded)
decoded = decodePlayfair(encoded, key)
print(decoded)'''

# test hill
'''key = np.array([[17, 17, 5], [21, 18, 21], [2, 2, 19]])
text = "PAYMOREMONEYC"
encoded = encodeHill(text, key)
print("Encoded:", encoded)
decoded = decodeHill(encoded, key)
print("Decoded:", decoded)'''
