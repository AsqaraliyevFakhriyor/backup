import os
import sys

if "-cln" in sys.argv:
    os.environ["MY_DICT_ORD_NUM"] = "0"
    print(sys.argv[1:])
    quit()


while True:

    ord_num = str(os.environ.get("MY_DICT_ORD_NUM", 1))
    f = open("dict_.txt", "a")
    eng, uzb = input("&-->").split()
    f.write("{0}: {1} --- {0}: {2}\n".format(ord_num, eng, uzb))
    f.close()
    os.environ["MY_DICT_ORD_NUM"] = str(int(ord_num) + 1)




