# Traveller System/Subsector/Sector generator
# 2019-10-23 - Start, let's make a system.
import random

def diceroller(dicenum,size):
    dietotal=0
    for dice in range(dicenum):
        dietotal = dietotal + random.randint(1,size)
    return dietotal

for i in range(10):
    print(diceroller(i,6))
