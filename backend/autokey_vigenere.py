import sys

alphabet26 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def preprocessingPlaintext(plaintext : str):
    preProcessing = ''.join([element for element in plaintext if element.isalpha()])
    preProcessing = preProcessing.upper()
    return preProcessing


def encrypt(plaintext:str, key:str):
    cipher = ""

    plaintext = preprocessingPlaintext(plaintext)
    plaintextLength = len(plaintext)
    keyLength = len(key)
    keyStream = key
    for i in range(plaintextLength - keyLength):
        keyStream += plaintext[i]
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
    keyStream = key

    for i in range(cipherLenght):
        keyStream = keyStream.upper()
        cipherOrd = ord(cipher[i]) - 65
        keyStreamOrd = ord(keyStream[i]) - 65
        

        plaintextOrd = (cipherOrd - keyStreamOrd) % 26
        plaintext += alphabet26[plaintextOrd]
        keyStream += plaintext[i]

    return plaintext


if __name__ == '__main__' :
    method = sys.argv[1]
    text = sys.argv[2]
    key = sys.argv[3]

    if(method == "encrypt"):
        print(encrypt(text, key))
    else:
        print(decrypt(text, key))