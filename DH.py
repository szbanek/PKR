import sys
import random

def main():
    n = int(sys.argv[1])
    g = int(sys.argv[2])

    x = random.randrange(n, 10*n)
    X = pow(g, x, n)

    y = random.randrange(n, 10*n)
    Y = pow(g, y, n)

    Ak = pow(Y, x, n)
    Bk = pow(X, y, n)

    print(Ak)
    print(Bk)
    print(Ak==Bk)

if __name__ == "__main__":
    main()