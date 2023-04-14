import sys
import random


def main():
    p = int(sys.argv[1])
    q = int(sys.argv[2])
    message = sys.argv[3].lower()

    n = p*q
    phi = (p-1)*(q-1)
    e = phi-1
    phi_divisors = divisors(phi)
    for x in range(2, phi-1):
        if x not in phi_divisors:
            e = x
            break
    for x in range(phi-1):
        tmp = (x*phi + 1)/e 
        if tmp == int(tmp):
            d = int(tmp)
            break
    else:
        print("no valid d")
        return 1

    print(f"public key: e={e}, n={n}")
    print(f"private key: d={d}, n={n}")
    
    print(f"message: {message}")
    print("message lenght: {len(message)}")

    encoded = encode(e, n, message)
    print(f"encoded: {encoded}")

    decoded = decode(d, n, encoded)
    print(f"decoded: {decoded}")

    if message == decoded:
        print("succes!")
    else:
        print("failure!")

def divisors(n):
    res = []
    for i in range(1, int(n/2)):
        if n % i == 0:
            res.append(i)
    return res

def encode(e, n, message):
    res = []
    for x in message:
        res.append(pow(ord(x)-95, e, n))
    return res

def decode(d, n, encoded):
    res = []
    for x in encoded:
        tmp = pow(x, d, n)
        res.append(chr(tmp+95))
    return "".join(res)

if __name__ == "__main__":
    main()