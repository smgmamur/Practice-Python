'''
Created on Oct 31, 2017

@author: mhossain
'''


def first_n_last (array):
    array = []
    i = 0
    while i<5:
        array.append(int(input("Value:")))
        i+=1
        
    l = len(array)-1
    element1 = array[0]
    element2 = array[l]
    result_array = [element1,element2]
    return result_array

x = first_n_last(str)
print(x)

