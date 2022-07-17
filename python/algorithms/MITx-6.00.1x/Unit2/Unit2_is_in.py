def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    stLen = len(aStr)
    if stLen == 0:
        return False

    if stLen == 1:
        if aStr == char:
            # print("1 jest")
            return True
        else:
            #print("1 nie jest")
            return False

    if aStr[round(stLen/2)] == char:
        return True
    elif aStr[round(stLen/2)] < char:
        #print(f"ch z str: {aStr[round(stLen/2)]}")
        return isIn(char, aStr[(round(stLen/2) + 1):])
    else:
        #print(f"ch z str: {aStr[round(stLen/2)]}")
        return isIn(char, aStr[:round(stLen/2)])
