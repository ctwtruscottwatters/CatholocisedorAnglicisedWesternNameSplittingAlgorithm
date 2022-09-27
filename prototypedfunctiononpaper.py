# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 20:46:49 2022

@author: Charles Truscott
"""


def recursive_definition(x = 1, y = 1, z = []):
#    print("{} {} {}".format(x, y, z))
    if x > 10:
        print("\n\n\n{} {}\n\n\n".format(x, y))
        print("{}".format(z))
        L = []
        for x in z:
            L.append(x)
        return L
    if y == 10 and x < (10 + 1):
        x += 1
        y = 1
        z.append(x / y)
        print("Calling recursive call with x: {} y: {}".format(x, y))
        recursive_definition(x,y,z)
    elif y < 10 and x < (10 + 1):
        y += 1
        z.append(x / y)
        print("Calling recursive call with x: {} y: {}".format(x, y))
        recursive_definition(x,y,z)
    
    
def main():
    z = 0
    steps = 0
    for x in range(1, 10 + 1, 1):
        for y in range(1, 10 + 1, 1):
            z = x/y
            steps += 3
            if x == 1 or x == 2 or x == 9:
                print(z)
    print(steps)
    L = recursive_definition(1, 1, z=[])
    print(L)
    for x in range(0, len(L) - 1, 1):
        print(L[x])
            

if __name__ == "__main__": main()