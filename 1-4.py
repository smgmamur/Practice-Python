'''
Created on Oct 11, 2017

@author: mhossain
'''
i = 0
num = int(input("Enter a number to find its divisors:"))
nums_less_than_num = list(range(1,num+1))
divisors = []

while nums_less_than_num[i]<num:
    if num%nums_less_than_num[i]==0:
        divisors.append(nums_less_than_num[i])
    i=i+1
print(divisors)

