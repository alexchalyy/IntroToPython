''' This is the program to generate race between hare and tortoise.

    Written by Alex Chalyy on 9/24/2021. '''

import time
import random

h = 0   # Hare counter
t = 0   # Tortoise counter

print("BANG!!! AND THEY'RE OFF!!!")

while (h < 69 and t < 69):
    track = ""
    rh = random.randrange(0, 10)
    rt = random.randrange(0, 10)
    r = 0
    if rt < 5:
        t = t + 3
    elif rt == 5 or rt == 6:
        t = t - 6
    else:
        t = t + 1
    if t < 0:
        t = 0
    if rh == 2 or rh == 3:
        h = h + 9
    elif rh == 4:
        h = h - 12
    elif rh == 5 or rh == 6:
        h = h + 1
    elif rh == 8 or rh == 9:
        h = h - 2
    if h < 0:
        h = 0
    time.sleep(1)
    for c in range(10):
        print("\n")
    print("_______________________________________________________________________")
    if h >= 69 and t >= 69:
        print("IT'S A TIE!")
    elif h >= 69:
        print("Hare wins!")
    elif t >= 69:
        print("Tortoise wins!")
    elif t == h:
        while r < 70:
            if r != t:
                track += " "
            else:
                track += "OUCH!"
                r = r + 4
            r = r + 1
    else:
        while r < 70:
            if r != t and r != h:
                track += " "
            elif r == h:
                track += "H"
            else:
                track += "T"
            r = r + 1
    print(track)
    print("_______________________________________________________________________")

    