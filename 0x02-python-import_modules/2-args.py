#!/usr/bin/python3

import sys
if __name__ == "__main__":

    wns = "argument:"
    arg1 = "Hello"
    arg = sys.argv
    len1 = len(sys.argv)
    len2 = len(sys.argv) - 1
    
    i =2
    if i > 1:
        
        

        ws = wns + "s:"
    i =0    
    if( i == 0):
        print("{} {}.".format(i,wns))

    for i in range(1, len1):

        if (i == 1):
            print("{} {}".format(i,wns))
            print("{}: {}".format(i,arg1))

        else:
             while(i < len1):
                 ++i
                 print("{} {}".format(len2,ws))
                 print("{}: {}".format(i,arg))
                 ++arg



