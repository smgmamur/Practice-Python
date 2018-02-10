'''
Created on Oct 31, 2017

@author: mhossain
'''
def fibonibo(how_many_numbs):
    fibo_array = []
    a,b = 0,1
    
    while b<=how_many_numbs:
        
        fibo_array.append(b)
        b = a + b
        a = b - a
                   
    return fibo_array

x = fibonibo(200)
print(x)
