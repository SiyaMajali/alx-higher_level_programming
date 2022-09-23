#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argu_len = len(sys.argv) - 1
    if argu_len == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(argu_len))
    for i, j in enumerate(sys.argv):
        if i >= 1:
            print("{}: {}".format(i, j))
