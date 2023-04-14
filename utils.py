import random

f = open("10M.txt", "w")
for _ in range(10000000):
    f.write(str(hex(random.randint(0, 16))))
f.close()
