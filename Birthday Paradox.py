# Write a program that simulates the classic birthday paradox. Given 'n' people in a room, calculate the probability
# that at least two people share the same birthday. Vary the value of 'n' and observe how the probability changes.

import random

n = int(input("Enter the number of people in the room: "))
count = 0

for i in range(10000): # repeat the experiment 1000 times
    lis = []

    for j in range(n):
        lis += [random.randint(0, 365)]

    k = [x for x in lis if lis.count(x) > 1]

    if len(k) > 0:
        count += 1

pr = count / 10000

print(f"Out of {n} people, the probability of two people having the same birthdate is {pr}.")
