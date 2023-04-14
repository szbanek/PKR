import hashlib
import matplotlib.pyplot as plt
import sys
import time


def main():
    # message = sys.argv[1]
    # md5 = hashlib.md5(message.encode())
    # sh1 = hashlib.sha1(message.encode())
    # sh2 = hashlib.sha512(message.encode())
    # print("MD5: " + md5.hexdigest())
    # print("SHA-1: " + sh1.hexdigest())
    # print("SHA-2 (512): " + sh2.hexdigest())

    test_files = ["1M.txt", "5M.txt", "10M.txt"]
    algorythms = ["md5", "sha1", "sha512"]
    times = {}
    lenghts = {}
    for file in test_files:
        f = open(file, "r")
        t1 = time.time()
        md5 = hashlib.md5(f.read().encode())
        t2 = time.time()
        time_md5 = t2-t1
        f.seek(0)
        t1 = time.time()
        sh1 = hashlib.sha1(f.read().encode())
        t2 = time.time()
        time_sh1 = t2-t1
        f.seek(0)
        t1 = time.time()
        sh2 = hashlib.sha512(f.read().encode())
        t2 = time.time()
        time_sh2 = t2-t1
        times[file] = [time_md5, time_sh1, time_sh2]
        lenghts[file] = [len(md5.hexdigest()), len(sh1.hexdigest()), len(sh2.hexdigest())]
        print(md5.hexdigest())
        f.close()

    fig, (ax1, ax2) = plt.subplots(2)
    for i in range(len(times[test_files[0]])):
        i_times = [x[i] for x in times.values()]
        i_lenghts = [x[i] for x in lenghts.values()]
        ax1.plot(i_times, label=algorythms[i])
        ax2.plot(i_lenghts, label=algorythms[i])
    ax1.legend(loc="upper left")
    ax1.set_title("time")
    ax2.legend(loc="upper left")
    ax1.set_title("length")
    plt.show()


if __name__ == "__main__":
    main()
