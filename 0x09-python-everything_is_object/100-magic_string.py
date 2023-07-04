#!/usr/bin/python3
iter = 0
def magic_string():
    global iter
    iter += 1
    return "BestSchool" + (", BestSchool" * (iter - 1))
