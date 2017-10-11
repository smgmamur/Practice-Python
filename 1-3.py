'''
Created on Oct 11, 2017

@author: mhossain
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
i = 0
num = int(input("Enter an integer to set array element threshold:"))

while i<len(a):
    if a[i]<num:
        b.append(a[i])
    i=i+1

print("Numbers smaller than", num, ":", b)

