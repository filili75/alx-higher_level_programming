#!/usr/bin/python3
for s in range(97, 123):
    if (s == 101) or (s == 113):
        continue
    print(chr(s).format(), end="")
