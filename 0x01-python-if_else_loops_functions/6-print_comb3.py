#!/usr/bin/python3
for s in range(9):
    for j in range(s + 1, 10):
        if s * 10 + j < 89:
            print("{:d}{:d}".format(s, j), end=", ")
print("{:d}".format(89))
