'''
Created on Nov 1, 2017

@author: mhossain
'''

def rev_string(given_string):
    
    given_string = str(input("Insert a sentence to reverse:"))
    
    print(given_string)
    
    words_list = given_string.split()
    
    '''print(words_list)'''
    
    i = len(words_list)-1
    reverse_list = []
    
    while i >= 0 :
        
        reverse_list.append(words_list[i])
        i -= 1
    
    '''print(reverse_list) '''
    
    final_string = " ".join(reverse_list)
    
    return final_string



x = rev_string(str)
print(x)

k=input("press close to exit") 


