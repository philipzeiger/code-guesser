# Code Breaker Game
# Author: Philip Zeiger
# Date: June 26, 2021
# Purpose: Reviewing Python as part of a Django Full Stack course

# The game will generate a 3 digit number and prompt the player
# to guess a 3 digit number. The Game will respond with a hint:
# Nope - Close - Match
# Nope! = none of your numbers are contained in the 3 digit code.
# Close = one of the digits is correct but not in the correct place.
# Match = a digit is correct and in the correct place.

import random   #used for generating the random 3 digit number
def generate_code():    #this is the method that creates a random 3-digit number
    return str(random.randint(100,999))

def check_guess(guess, code): 
    #method that checks a guessed number against the generated code
    #the two paramaters are "guess" and "code"
    #guess = the 3 digit number the user guessed, stored as a string
    #code = the 3 digit number that the computer generated  
    #checks for a exact match, and if it doesnt find one then checks what clues
    #can be given ("Nope!" "Close" "Match") and prints the clues

    if guess == code:   #this terminates the method and returns False to end the program loop if the guess is equal to code
        print("Yes, you got it! Answer: " + code)
        return False

    first_digit = guess[0]
    second_digit = guess[1]
    third_digit = guess[2]
    nope = True

    if first_digit==code[0]:
        print ("Match")
        nope = False
    elif first_digit==code[1] or first_digit==code[2]:
        print("Close")
        nope = False
    if second_digit==code[1]:
        print ("Match")
        nope = False
    elif second_digit==code[0] or second_digit==code[2]:
        print("Close")
        nope = False
    if third_digit==code[2]:
        print ("Match")
        nope = False
    elif third_digit==code[0] or third_digit==code[1]:
        print("Close")
        nope = False
    if nope:
        print("Nope!")


    return True

print("Welcome to Codebreaker!")    #welcome message

code = generate_code()  #calls the method and captures the random 3 digit code
print("Code has been generated!")


u_guess = input("Please enter a 3 digit guess: ")   #grabs the first 3 digit guess

check = True    #value that will be changed to False when the check_guess method finds the guess to be a match

while (check):  #main loop of the program, this continues until check_guess finds a match and returns false
    check = check_guess(u_guess, code) 
    if check == True:
        u_guess = input("Please enter another 3 digit code: ")