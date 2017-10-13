'''
Created on Oct 12, 2017

@author: mhossain
'''

word_original = input("Insert a word to check for palendrome:")
word = word_original.lower()

halfsize = int((len(word))/2)
last_element = len(word)-1
i=0
word_last_half = ""

word_first_half = word[0:halfsize]
while i < halfsize:
   word_last_half=word_last_half+word[last_element-i]
   i=i+1

if word_first_half==word_last_half:
    print(word_original, "is a palendrome!")
else:
    print("Nahhhhhh,", word_original, "is NOT a palendrome.")
 
