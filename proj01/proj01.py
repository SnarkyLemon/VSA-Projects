# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!


user_name = raw_input("Please enter your name.")
print "Thank you."
user_age = raw_input("Now, "+user_name+", could you please enter your age?")
print "You are "+user_age+", "+user_name+"?"
birthyear = 2017 - int(user_age)
year100 = birthyear + 100
user_birthday = raw_input("If you have already had a birthday this year, enter Y. If you have not, enter N.)
if user_birthday == "Y":
    print "You will be 100 in "+ str(year100) + "."
if user_birthday == "N":
    year100b = birthyear + 99
    print "You will be 100 in "+ str(year100b)) + "."

