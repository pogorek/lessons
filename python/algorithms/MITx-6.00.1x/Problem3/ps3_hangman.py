# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

all_letters = string.ascii_lowercase
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    secretWord_list = list(secretWord)
    
    for letter in secretWord_list:
        if letter not in lettersGuessed:
            return False
        
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    secretWord_list = list(secretWord)
    
    current_word = ""
    
    for letter in secretWord_list:
        if letter not in lettersGuessed:
            current_word += "_ "
        else:
            current_word += letter
            
    return current_word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    all_letters_list = list(all_letters)
    
    for letter in lettersGuessed:
        all_letters_list.remove(letter)
        
    return "".join(all_letters_list)
    


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))
    
    mistakesMade = 0
    lettersGuessed = list()
    
    while mistakesMade < 8 and not isWordGuessed(secretWord, lettersGuessed):
        print("-------------")
        print("You have {} guesses left.".format(8 - mistakesMade))
        print("Available letters: {}".format(getAvailableLetters(lettersGuessed)), end="")

        guess = input("Please guess a letter: ")
        guess = guess.lower()
        
        if guess not in getAvailableLetters(lettersGuessed):
            print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, lettersGuessed)))
        
        elif guess not in secretWord:
            lettersGuessed += guess
            mistakesMade += 1
            print("Oops! That letter is not in my word: {}".format(getGuessedWord(secretWord, lettersGuessed)))
               
        else:
            lettersGuessed += guess
            print("Good guess: {}".format(getGuessedWord(secretWord, lettersGuessed)))
            
    if mistakesMade >= 8:
        print("-------------")
        print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))
            
    if isWordGuessed(secretWord, lettersGuessed):
        print("-------------")
        print("Congratulations, you won!")
        
        # print(guess)
        
        
""" 
 
# secretWord = chooseWord(loadWords())
#print(secretWord) 

secretWord = "bob" #chooseWord(loadWords())   
hangman(secretWord)  



secretWord: The word to guess.

lettersGuessed: The letters that have been guessed so far.

mistakesMade: The number of incorrect guesses made so far.

availableLetters: The letters that may still be guessed. 
Every time a player guesses a letter, the guessed letter 
must be removed from availableLetters (and if they guess 
a letter that is not in availableLetters, you should print
 a message telling them they've already guessed that - so
 try again!).



Welcome to the game Hangman!
I am thinking of a word that is 4 letters long.
	
    -------------
	You have 8 guesses left.
	Available letters: abcdefghijklmnopqrstuvwxyz
	Please guess a letter: a
	Good guess: _ a_ _
	
    ------------
	You have 8 guesses left.
	Available letters: bcdefghijklmnopqrstuvwxyz
	Please guess a letter: a
	Oops! You've already guessed that letter: _ a_ _
	
    ------------
	You have 8 guesses left.
	Available letters: bcdefghijklmnopqrstuvwxyz
	Please guess a letter: s
	Oops! That letter is not in my word: _ a_ _

	------------
	Congratulations, you won!
    
    -----------
	Sorry, you ran out of guesses. The word was else. 

"""

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
