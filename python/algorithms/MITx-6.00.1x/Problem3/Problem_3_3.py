import string

all_letters = string.ascii_lowercase

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
    
    
"""
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
# abcdfghjlmnoqtuvwxyz
"""
