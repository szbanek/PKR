import random
import sys
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

def main():

    seed = int(sys.argv[1])
    n = int(sys.argv[2])
    
    path = "XDD.jpg"

    delta = 5

    image = Image.open(path).convert("L")
    image = np.array(image)
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] > 255-delta:
                image[i][j] = 255-delta
            if image[i][j] < delta:
                image[i][j] = delta

    random.seed(seed)

    s = 2*delta*n

    for i in range(n):

        point1 = (random.randrange(0, len(image)), random.randrange(0, len(image[0])))
        point2 = (random.randrange(0, len(image)), random.randrange(0, len(image[0])))

        s += image[point1] - image[point2]

        image[point1] += delta
        image[point2] -= delta

    print(s)

    plt.imshow(image, cmap="gray")
    plt.show()

    random.seed(seed)
    s = 0

    for i in range(n):

        point1 = (random.randrange(0, len(image)), random.randrange(0, len(image[0])))
        point2 = (random.randrange(0, len(image)), random.randrange(0, len(image[0])))

        s += image[point1] - image[point2]

        image[point1] -= delta
        image[point2] += delta

    print(s)

    plt.imshow(image, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()