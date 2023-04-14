import numpy as np
import sys

def main():
    global mtx

    KEY = sys.argv[1]
    message = sys.argv[2]

    alphabet = "abcdefghiklmnopqrstuvwxyz"

    for i in range(len(KEY)):
        if KEY.count(KEY[i])>1:
            print("key contain same letter more than once!")
            exit(1)
        if KEY[i] == "j":
            KEY[i] = "i"

    for x in KEY : 
        alphabet = alphabet.replace(x,"")

    mtx = np.array(list(KEY + alphabet)).reshape(5,5)

    if len(message)%2==1:
        message += "x"
    message = [message[i:i+2] for i in range(0, len(message), 2)]

    print(mtx)
    encoded = ""
    decoded = ""

    # Encode
    for x, y in message:
        encoded += Encode(x, y)
    print(encoded)

    # Decode
    if encoded != "":
        encoded = [encoded[i:i+2] for i in range(0, len(encoded), 2)]
    else: 
        encoded = message
    for x, y in encoded:
        decoded += Decode(x, y)
    print(decoded)

def Encode(a, b):
    index_a = (lambda x: (x[0][0], x[1][0]))(np.where(mtx==a))
    index_b = (lambda x: (x[0][0], x[1][0]))(np.where(mtx==b))
    if index_a[0] == index_b[0]:
        return mtx[index_a[0]][(index_a[1]+1)%5] + mtx[index_b[0]][(index_b[1]+1)%5]
    if index_a[1]==index_b[1]:
        return mtx[(index_a[0]+1)%5][index_a[1]] + mtx[(index_b[0]+1)%5][index_b[1]]
    else:
        return mtx[index_a[0]][index_b[1]] + mtx[index_b[0]][index_a[1]]

def Decode(a, b):
    index_a = (lambda x: (x[0][0], x[1][0]))(np.where(mtx==a))
    index_b = (lambda x: (x[0][0], x[1][0]))(np.where(mtx==b))
    if index_a[0] == index_b[0]:
        return mtx[index_a[0]][(index_a[1]-1)%5] + mtx[index_b[0]][(index_b[1]-1)%5]
    if index_a[1]==index_b[1]:
        return mtx[(index_a[0]-1)%5][index_a[1]] + mtx[(index_b[0]-1)%5][index_b[1]]
    else:
        return mtx[index_a[0]][index_b[1]] + mtx[index_b[0]][index_a[1]]

if __name__ == "__main__":
    main()

