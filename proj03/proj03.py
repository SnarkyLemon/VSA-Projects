# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""


#user_input = int(raw_input("Enter a number: "))

#prevnum = 0
#fibnum = 1
#while user_input > 0:
#    print user_input,
#    print fibnum
#    newnum = prevnum + fibnum
#    prevnum = fibnum
#    fibnum = newnum
#    user_input -= 1


import random
RNum = random.randint(1,9)
numguesses = 3
while numguesses > 0:
    numguesses -= 1
    guess = int(raw_input("Guess a number between 1 and 9."))
    if guess == RNum:
        print "You've guessed correctly."
        print numguesses
        break
    if guess > RNum:
        print "You've guessed too high"
        print numguesses
    if guess < RNum:
        print "You've guessed too low."
        print numguesses


