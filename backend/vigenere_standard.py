import sys

alphabet26 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def makeKeyStream(key : str, textLength : int):
    keyStream = key
    keyLength = len(key)

    for i in range(textLength-keyLength):
        keyStream += key[i % keyLength]
    
    return keyStream


def preprocessingPlaintext(plaintext : str):
    preProcessing = ''.join([element for element in plaintext if element.isalpha()])
    preProcessing = preProcessing.upper()
    return preProcessing

def encrypt(plaintext:str, key:str):
    cipher = ""

    plaintext = preprocessingPlaintext(plaintext)
    plaintextLength = len(plaintext)
    keyStream = makeKeyStream(key, plaintextLength)
    keyStream = keyStream.upper()

    for i in range(plaintextLength):
        plaintextOrd = ord(plaintext[i]) - 65
        keyStreamOrd = ord(keyStream[i]) - 65

        cipherOrd = (plaintextOrd + keyStreamOrd) % 26
        cipher += alphabet26[cipherOrd]

    return cipher

def decrypt(cipher:str, key:str):
    plaintext = ""

    cipherLenght = (len(cipher))
    keyStream = makeKeyStream(key, cipherLenght)
    keyStream = keyStream.upper()

    for i in range(cipherLenght):
        cipherOrd = ord(cipher[i]) - 65
        keyStreamOrd = ord(keyStream[i]) - 65

        plaintextOrd = (cipherOrd - keyStreamOrd) % 26
        plaintext += alphabet26[plaintextOrd]

    return plaintext

if __name__ == '__main__' :
    method = sys.argv[1]
    text = sys.argv[2]
    key = sys.argv[3]
    path = sys.argv[4]

    if(method == "encrypt"):
        cipher = encrypt(text, key)
        print(cipher)
        f = open(path, "w")
        f.write(cipher)
        f.close()
    else:
        plain = decrypt(text, key)
        print(plain)
        f = open(path, "w")
        f.write(plain)
        f.close()
