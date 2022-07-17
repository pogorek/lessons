# define the simple_divide function here
def simple_divide(item, denom):
    ans = 0
    try:
        ans = item / denom
    except ZeroDivisionError:
        return 0
    else:
        return ans
