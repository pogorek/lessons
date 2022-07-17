# Paste your code into this box
prevBalance = balance

monthlyInterestRate = annualInterestRate / 12.0

for i in range(12):
    minimumMonthlyPayment = monthlyPaymentRate * prevBalance

    monthlyUnpaidBalance = prevBalance - minimumMonthlyPayment

    updatedBalanceEachMonth = monthlyUnpaidBalance + \
        (monthlyInterestRate * monthlyUnpaidBalance)
    prevBalance = updatedBalanceEachMonth


state = round(prevBalance, 2)
print("Remaining balance: {}".format(state))
