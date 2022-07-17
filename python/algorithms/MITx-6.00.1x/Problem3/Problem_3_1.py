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
    
    

"""
secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
lettersGuessed2 = ['e', 'i', 'l', 'p', 'r', 's']
lettersGuessed3 = ['a', 'p', 'l', 'p', 'r', 'e']


print(isWordGuessed(secretWord, lettersGuessed3))
"""