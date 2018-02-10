'''
Created on Nov 1, 2017

@author: mhossain
'''
def und_list(array):

    array = []
    i = 0
    while i<5:
        array.append(str(input("Value:")))
        i+=1
        
    unduplicate_list = []
    i = 0
    j = 0
    
    while i < len(array):
        if array[i] not in unduplicate_list:
            unduplicate_list.append(array[i])
        i += 1
    
    return unduplicate_list



def und_set(array):
    
    array = []
    i = 0
    while i<5:
        array.append(str(input("Value:")))
        i+=1
    
    unduplicate_list = set(array)
    
    return unduplicate_list


def und_comm(array1,array2):
    
    import random

    array1=random.sample(range(0,100),6)
    array2=random.sample(range(0,100),9)
    
    print(array1,array2)
    
    set1 = set(array1)
    set2 = set(array2)
    
    und_comm_set = set1 & set2
    
    return und_comm_set
    
    

x = und_comm(int,int)
print(x)


