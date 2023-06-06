#!/usr/bin/python3

for num in range(0, 100):
    if (num != 99):
        print(str(num).zfill(2), end=", ")

    else:
        print("99")
