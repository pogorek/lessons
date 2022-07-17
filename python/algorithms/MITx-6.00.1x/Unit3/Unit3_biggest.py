def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    big = 0
    longest_key = ""
    for idx, val in enumerate(aDict):
        if len(aDict[val]) >= big:
            big = len(aDict[val])
            longest_key = val

    if len(aDict) > 0:
        return longest_key
    else:
        return None
