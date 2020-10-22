#!/bin/python3

import sys

def caesarCipher(s, k):
    abl = "abcdefghijklmnopqrstuvwxyz"
    abu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c_map_lower = { abl[index] : index  for index in range(len(abl)) }
    c_map_upper = { abu[index] : index for index in range(len(abu)) }
    list = []
    for c in s:
        if c.isalpha():
            index = c.islower() and c_map_lower[c] or c_map_upper[c]
            k %= 26
            index += k
            if index > 25:
                index = index - 25 - 1
            list.append(c.islower() and abl[index] or abu[index])
        else:
            list.append(c)
    return "".join(list)


if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)
