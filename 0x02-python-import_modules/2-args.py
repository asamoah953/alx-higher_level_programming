#!/usr/bin/python3

import sys

if __name__== "__main-__":

    s = len(sys.argv) - 1

    h = sys.argv

    if s ==0:
        print("{} arguments.".format(s))

    elif s == 1:
        print("{} arguments:".format(s))

    else:
        print("{} arguments:")

    if s >= 1:
        s = 0
        for arg in h:
            if i != 0:
                print("{}: {}".format(s,arg))

                s += 1
