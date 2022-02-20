# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 04:55:31 2022

@author: Coding
"""
import math

def is_prime(x):
    if x > 1 and x!=4:
        for i in range(2,math.ceil(x/2)):
            if(x % i) == 0:
                return False
        return True
    return False

Testlist = []
temp = 0
while True:
    temp = int(input("Set the List Before Test,enter any number smaller than 1 to quit:"))
    if temp <1:
        break
    Testlist.append(temp)
Result = []
for i in Testlist:
    if(is_prime(i)):
        Result.append(i)
        print(i,"is a prime in the list")
print("The primes in the list are:")
for i in Result:
    print(i,end=(','))