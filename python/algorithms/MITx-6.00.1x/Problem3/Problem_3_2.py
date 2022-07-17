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
       


"""
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))
#'_ pp_ e'
"""
