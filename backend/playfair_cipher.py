import sys


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

if __name__ == '__main__' :
    method = sys.argv[1]
    text = sys.argv[2]
    key = sys.argv[3]

    if(method == "encrypt"):
        print(encodePlayfair(text, key))
    else:
        print(decodePlayfair(text, key))