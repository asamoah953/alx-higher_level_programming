#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    my_result = 0

    for argument in sys.argv:
        if argument != sys.argv[0]:

            my_result += int(argument)

    print(my_result)
