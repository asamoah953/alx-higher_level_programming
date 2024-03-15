#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    arg = sys.argv
    m = len(arg) - 1 

    if m >= 1:

        print("{}: arguments.".format(m))
        for i in range(1,m + 1):

            print("{}: {} ".format(i,arg[i]))

    elif m==0:

        print("{}: arguments.".format(m))
    
    else:
        print("{} arguments.".format(m))
        print("{}: {}".format(m,arg[1]))
