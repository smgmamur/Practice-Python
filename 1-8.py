'''
Created on Oct 13, 2017

@author: mhossain
'''
while True:

    input_user1 = input("Player1:::: Type one - Rock/Paper/Scissors:")
    input_user2 = input("Player2:::: Type one - Rock/Paper/Scissors:")
    
    if (input_user1 == input_user2):
        print("Tie! Try different words for different users.")
    elif ((input_user1 == "Rock") and (input_user2 == "Scissors")):
          print("User1 WINS!")
    elif ((input_user1 == "Rock") and (input_user2 == "Paper")):
          print("User2 WINS!")
    elif ((input_user1 == "Scissors") and (input_user2 == "Paper")):
          print("User1 WINS!")
    elif ((input_user1 == "Scissors") and (input_user2 == "Rock")):
          print("User2 WINS!")
    elif ((input_user1 == "Paper") and (input_user2 == "Rock")):
          print("User1 WINS!")
    elif ((input_user1 == "Paper") and (input_user2 == "Scissors")):
          print("User2 WINS!")
    else:
        print("WRONG INPUT! BUT YOU FIGURE OUT USER1 OR USER2 MADE THIS MESS! BOO!")
     
    terminate = input("Type 'quit' to quit from the game / Enter to continue:")
     
    if (terminate == "quit"):
        break

print("Game Over!")

