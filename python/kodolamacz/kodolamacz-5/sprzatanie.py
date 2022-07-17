import os
import datetime


def main():
    sciezka_do_pliku = "/mnt/d/PROGRAMOWANIE/GIT/kodolamacz/kodolamacz-5/kawa.txt"
    sciezka_do_folderu = "/mnt/d/PROGRAMOWANIE/GIT/kodolamacz/kodolamacz-5/"
    print(os.path.exists(sciezka_do_pliku))
    print(os.listdir(sciezka_do_folderu))
    # for i in os.listdir(sciezka_do_folderu):
    #     print(i)

    (mode, ino, dev, nlink, uid, gid, size, atime,
     mtime, ctime) = os.stat(sciezka_do_pliku)
    data1 = datetime.datetime.fromtimestamp(mtime)
    print(data1)
    # data2 = datetime.datetime.fromtimestamp(ino)
    # print(data2)
    # data3 = datetime.datetime.fromtimestamp(nlink)
    # print(data3)
    # data4 = datetime.datetime.fromtimestamp(uid)
    # print(data4)
    # data5 = datetime.datetime.fromtimestamp(gid)
    # print(data5)
    # data6 = datetime.datetime.fromtimestamp(mode)
    # print(data6)
    data7 = datetime.datetime.fromtimestamp(atime)
    print(data7)
    data9 = datetime.datetime.fromtimestamp(ctime)
    print(data9)
    print(size)
    print(mode)
    print(ino)
    print(dev)
    print(nlink)
    print(uid)
    print(gid)
    print(size)
    print(atime)
    print(mtime)
    print(ctime)


if __name__ == "__main__":
    main()
