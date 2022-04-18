x = 'print(55)'
eval(x)

def calculator(num1, operator, num2):
    if operator == '/' and num2 == 0:
        return "Can't divide by 0!"
    return eval('num1 ' + operator + 'num2')

print(calculator(2, "/", 0))