'''
Created on Jan 25, 2018

@author: mhossain
'''
import random
import string
   
def strong_PW():

    i = 0
    j = 0
    k = 0
    l = 0
    
    PW_Uppers_Array = []
    PW_Lowers_Array = []
    PW_Digits_Array = []
    PW_Special_Array = []
    
    Uppers = string.ascii_uppercase
    Lowers = string.ascii_lowercase
    Digits = string.digits
    Special = string.punctuation
    
    PW_Uppers = random.choice(Uppers)
    PW_Lowers = random.choice(Lowers)
    PW_Digits = random.choice(Digits)
    PW_Special = random.choice(Special)
    
    for i in range (0,3):
        PW_Uppers_Array.append(random.choice(Uppers))
    for j in range (0,5):
        PW_Lowers_Array.append(random.choice(Lowers))
    for k in range (0,2):
        PW_Digits_Array.append(random.choice(Digits))
    for l in range (0,1):
        PW_Special_Array.append(random.choice(Special))
    
    PW_Array = PW_Uppers_Array+PW_Lowers_Array+PW_Digits_Array+PW_Special_Array
    PW = ''.join(random.sample(PW_Array,len(PW_Array)))
    
    return PW


def weak_PW():
    names = ["TRIton387", "GANymede32", "CALlisto08", "ARIel007"]
    
    return random.choice(names)


user_input = str(input("Enter 'S' for strong PW, 'W' for weak PW:"))

if (user_input == 's' or user_input == 'S'):
    x = strong_PW()
    print(x)
elif (user_input == 'w' or user_input == 'W'):
    y = weak_PW()
    print(y)
else:
    print("Wrong Input!")


