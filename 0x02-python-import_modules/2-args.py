#!/usr/bin/python3


if __name__== "__main__":

    import sys

    s = len(sys.argv) - 1

    h = sys.argv

    if s ==0:
        print("{} arguments.".format(s))

    elif s == 1:
        print("{} arguments:".format(s))

    else:
        print("{} arguments:".format(s))

    if s >= 1:
        s = 0
        for arg in h:
            if s != 0:
                print("{}: {}".format(s,arg))

            s += 1
