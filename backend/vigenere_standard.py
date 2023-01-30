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

def encrypt():
    plaintext = input("Masukan Plain Text : ")
    key = input("Key : ")
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

def decrypt():
    cipher = input("Masukkan Cipher Text : ")
    key = input("Key : ")
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
