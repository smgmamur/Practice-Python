'''
Created on Oct 31, 2017

@author: mhossain
'''
def divisors(num):
    i = 0
    num = int(input("Enter a number to find its divisors:"))
    nums_less_than_num = list(range(1,num+1))
    divisor_array = []
    
    while nums_less_than_num[i]<num:
        if num%nums_less_than_num[i]==0:
            divisor_array.append(nums_less_than_num[i])
        i=i+1
    
    return (divisor_array,num)

array = divisors(int)
array_of_divisors = array[0]
num = array[1]

if len(array_of_divisors)>1:
    print(num," is NOT a prime number")
else:
    print(num,"is a prime number")


