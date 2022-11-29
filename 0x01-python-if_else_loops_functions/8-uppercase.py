#!/usr/bin/python3
def uppercase(str):
    low = [i for i in range(97, 123)]
    up = [j for j in range(65, 91)]
    new_str = ""
    for letter in str:
        for upper, lower in zip(up, low):
            if letter == chr(lower):
                letter = chr(upper)
        new_str += letter
    print("{}".format(new_str))
