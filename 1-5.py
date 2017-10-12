'''
Created on Oct 12, 2017

@author: mhossain
'''
import random

x=random.sample(range(0,100),6)
y=random.sample(range(0,100),9)

print(x,y)

''''a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]'''

c = []
i,j = 0,0
  
for i in range (0, len(x)):
    for j in range (0, len(y)):
        if x[i]==y[j] and x[i] not in c:
            c.append(x[i])
        j=j+1
    i=i+1

print("Array with common items:", c)
