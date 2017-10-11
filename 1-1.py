'''
Created on Jul 19, 2017

@author: mhossain
'''

import datetime
now = datetime.datetime.now()

name = input("Enter name:")
ageY = int(input("Now enter age:\n Years:"))
ageM = int(input("\nMonths:"))

NowY = now.year
NowM = now.month

Birth_Year = int(((NowY*12+NowM)-(ageY*12+ageM))/12)
Cent_Year = Birth_Year + 100

i=0

print("Name:", name)
print("Age: ", ageY, "Years ", ageM, "Months")

numcopy = int(input("Enter how many times you want to watch the answer:"))

while i<numcopy:
    print("Year you will turn 100: \n", Cent_Year)
    i=i+1
    
    
  
 
