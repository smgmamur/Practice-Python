'''
Created on Oct 13, 2017

@author: mhossain
'''

import random
terminate = ""

while True:
    
    num_attempt = 1
    
    num_compy = random.randint(1,9)
    print("Compy has generated an integer from 1 to 9 including the numbers.")
    
    while True:
      
        num_user = int(input("Your new guess:"))
        
        if (num_compy == num_user):
            print("CONGRATULATIONS! You Won! Compy had:", num_compy, "You put:", num_user)
        elif (abs(num_compy-num_user) == 1):
            print("SUPER HOT!!!")
        elif (abs(num_compy-num_user) in range(2,3)):
            print("HOT!")
        else:
            print("ZZZ ... cold!")
            
        if (num_compy == num_user):
            print("You took ***", num_attempt, "*** attempts to find the number.")
            break
            
        num_attempt += 1
        
    terminate = input("Type 'exit' to quit the game, enter to continue:")
    if terminate == "exit" or "quit":
        break
    else:
        continue

