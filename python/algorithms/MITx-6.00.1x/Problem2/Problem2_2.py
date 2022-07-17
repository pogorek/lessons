# Paste your code into this box
prevBalance = balance

monthlyInterestRate = annualInterestRate / 12.0
#print(f"monthlyInterestRate: {monthlyInterestRate * prevBalance}")


minimumFixedMonthlyPayment = 0

done = True

while done:

    for i in range(12):
        monthlyUnpaidBalance = prevBalance - minimumFixedMonthlyPayment

        updatedBalanceEachMonth = monthlyUnpaidBalance + \
            (monthlyInterestRate * monthlyUnpaidBalance)

        prevBalance = updatedBalanceEachMonth

    if prevBalance <= 0:
        done = False
    else:
        minimumFixedMonthlyPayment += 10
        prevBalance = balance


print("Lowest Payment: {}".format(minimumFixedMonthlyPayment))
