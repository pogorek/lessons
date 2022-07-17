def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    values_count = 0

    for item in aDict:
        if isinstance(aDict[item], list):
            values_count += len(aDict[item])
        else:
            values_count += 1

    return values_count
