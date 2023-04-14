import sys
import random


def main():
    p = int(sys.argv[1])
    q = int(sys.argv[2])
    lenght = int(sys.argv[3])

    if p % 4 != 3 or q % 4 != 3:
        return "p and q should be congruent to 3 mod 4!"

    n = p*q

    x0 = random.randrange(2, min(p, q))
    
    res = []

    for _ in range(lenght):
        x0 = pow(x0, 2, n)
        tmp = x0 % 2
        res.append(tmp)
        # print(tmp, end="")

    if (sum(res) < 9725 or sum(res) > 10275):
        print("first test failed!" + str(sum(res)))
    ones = [0 for _ in range(7)]
    zeros = [0 for _ in range(7)]
    if res[0] == 0:
        one = False
    else:
        one = True
    count = 1
    for x in res:
        if x == 1:
            if one != True:
                if count >= 6:
                    if count>= 26:
                        print("third test failed!")
                    zeros[6] += 1
                else:
                    zeros[count] += 1
                count = 1
                one = True
            else:
                count+=1
            
        else:
            if one != False:
                if count >= 6:
                    if count>= 26:
                        print("third test failed!")
                    ones[6] += 1
                else:
                    ones[count] += 1
                count = 1
                one = False
            else:
                count += 1
        
    
    if ((zeros[1] <2315 or zeros[1] > 2685) or
    (zeros[2] <1114 or zeros[2] > 1386) or
    (zeros[3] <527 or zeros[3] > 723) or
    (zeros[4] <240 or zeros[4] > 384) or
    (zeros[5] <103 or zeros[5] > 209) or
    (zeros[6] <103 or zeros[6] > 209) or
    (ones[1] <2315 or ones[1] > 2685) or
    (ones[2] <1114 or ones[2] > 1386) or
    (ones[3] <527 or ones[3] > 723) or
    (ones[4] <240 or ones[4] > 384) or
    (ones[5] <103 or ones[5] > 209) or
    (ones[6] <103 or ones[6] > 209)):
        print("second test failed!")
        print(zeros)
        print(ones)

    res = [int("".join(str(x) for x in res[i:i+4]), 2) for i in range(0, len(res), 4)]

    sixteen = [0 for _ in range(17)]
    for x in res:
        sixteen[x] += 1
    for i in range(len(sixteen)):
        sixteen[i] = sixteen[i]*sixteen[i]
    test4x = 16/5000*sum(sixteen) -5000
    if (test4x <2.16 or test4x>46.17):
        print("test four failed! " + str(test4x))


def divisors(n):
    res = []
    for i in range(1, int(n/2)):
        if n % i == 0:
            res.append(i)
    return res


if __name__ == "__main__":
    main()
