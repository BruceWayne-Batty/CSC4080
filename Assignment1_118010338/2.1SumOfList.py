# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 04:44:14 2022

@author: Coding
"""
sum = 0
TestList1 = [1, 2, 3, 4, 5 ]
print("the test list is:", end=' ')
for i in TestList1:
    print(i, end=',')
    sum+=i
print("\nthe sum of the test list is",sum)