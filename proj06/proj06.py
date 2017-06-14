# Name:
# Date:


# proj06: Hangman
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
#    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
#    print "  ", len(wordlist), "words loaded."
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere






def hangman():
    wordlist = load_words()
    word = choose_word(wordlist)
    l = len(word)
#    print l
    ans_list = ["_"]*l
    print ans_list
    numguess = 6
    print l, "letters long."
    print word
    while numguess > 0:
        guess = raw_input("Guess a letter or word ")

        for letter in guess:
            if letter in word:
                for num in range(len(word)):
                    if guess == word[num]:
                        ans_list[num] = guess
                        print "You've guessed correctly."
                        print ans_list
                        print str(ans_list)

        if guess == word:
            print("Wow I'm impressed")

        if str(ans_list) == word:
            print "You've correctly guessed the word. Also, this took like 6 hours to make, so no big deal."

        elif guess not in word:
            numguess -= 1
            print ("Sorry, that's incorrect")
    if numguess == 0:
        print "sorry, out of tries"

    if ans_list == word:
        print "You win"


    print ans_list
    print str(ans_list), "is the string answer list"
hangman()