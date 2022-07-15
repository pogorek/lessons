import pyinputplus as pyip

print("Welcome to Sandwitch Maker! \n")

bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], 'Choose bread type: \n',  numbered=True)

protein = pyip.inputMenu(['chicken', 'turkey', 'tofu'], 'Choose protein type: \n',  numbered=True)

cheese = pyip.inputYesNo('Would you like some cheese?\n')

if cheese == 'yes':
    cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], 'Choose cheese type: \n',  numbered=True)

number = pyip.inputInt('How many sandwiches you want?\n', min=1, max=7)

result = f'Your order is ready!\nSandwich on {bread} bread, with {protein} and {cheese + " cheese" if cheese != "no" else "no cheese"}.\n{number} of those waiting for you!'

print('response: ', result)
