'''
Created on Oct 30, 2017

@author: mhossain
'''
import random
x = random.sample(range(100),10)
y = random.sample(range(100),12)

commons = []
final = []
i = 0

commons = [i for i in x for j in y if i==j]

while i < len(commons):
    if commons[i] not in final:
        final.append(commons[i])
    i += 1

print("",x,"\t\n",y,"\t\n",final)

