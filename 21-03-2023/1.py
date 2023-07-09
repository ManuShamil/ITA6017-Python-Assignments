# 1. You throw two dice, one black and one green. What is the probability that the number 
# of eyes on the black die is larger than the number of eyes on the green die?
#  Note: We can simulate N throws of two dice in a program. For each throw we see if the 
# event is successful, and if so, increase M by one


import random

N = int(input("Enter the number of throws: "))
M = 0

for i in range(N):
    black = random.randint(1,6)
    green = random.randint(1,6)
    if black > green:
        M += 1

print(M/N)
