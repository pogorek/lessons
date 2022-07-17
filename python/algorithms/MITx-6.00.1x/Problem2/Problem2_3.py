# Paste your code into this box
prevBalance = balance

monthlyInterestRate = annualInterestRate / 12.0

minimumFixedMonthlyPayment = 0

mfmp_min = 0
mfnp_max = balance
mfnp_mid = (mfmp_min + mfnp_max) / 2

done = True

while done:
    for i in range(12):
        monthlyUnpaidBalance = prevBalance - mfnp_mid

        updatedBalanceEachMonth = monthlyUnpaidBalance + \
            (monthlyInterestRate * monthlyUnpaidBalance)

        prevBalance = updatedBalanceEachMonth

    if prevBalance <= -0.04:
        mfnp_max = mfnp_mid
        mfnp_mid = (mfmp_min + mfnp_max) / 2
        prevBalance = balance

    elif prevBalance > 0:
        mfmp_min = mfnp_mid
        mfnp_mid = (mfmp_min + mfnp_max) / 2
        prevBalance = balance

    else:
        done = False

#  print(mfnp_mid)

mfnp_mid = round(mfnp_mid, 2)

print("Lowest Payment: {}".format(mfnp_mid))
