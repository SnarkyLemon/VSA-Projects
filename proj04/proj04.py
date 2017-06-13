# Name:
# Date:

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""
pal = True
user_palindrome = raw_input("Please enter a palindrome, you filthy casual.")
print user_palindrome
user_palindrome = user_palindrome.lower()
while user_palindrome:
    if user_palindrome[0] == user_palindrome[-1]:
        user_palindrome = user_palindrome[1:-1]

    else:
        print "That's not a palindrome, you Hanzo main!"
        pal = False
        break

if pal == True:
    print "This word is a palindrome."

