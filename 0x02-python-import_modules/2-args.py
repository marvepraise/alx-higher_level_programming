#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ArgLen = len(argv)

    if ArgLen == 1:
        print("0 arguments.")
    elif ArgLen == 2:
        print("{} argument:".format(ArgLen - 1))
    else:
        print("{} arguments:".format(ArgLen - 1))
    for index, var in enumerate(argv):
        if index == 0:
            continue
        print("{}: {}".format(index, var))
