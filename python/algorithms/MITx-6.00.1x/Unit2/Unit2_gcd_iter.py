def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a > b:
        a, b = b, a

    for i in range(b, 1, -1):
        if b % i == 0 and a % i == 0:
            return i

    return 1
