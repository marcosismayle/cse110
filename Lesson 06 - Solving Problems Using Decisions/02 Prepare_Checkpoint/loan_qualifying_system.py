print()
print('To verify if you are qualified for a loan, answer for a rating from 1–10.')
print()

loan_size = int(input('How large is the loan? '))
credit = int(input('How good is your credit history? '))
income = int(input('How high is your income? '))
down_payment = int(input('How large is your down payment? '))

if loan_size >= 5:
    if credit >= 7 and income >= 7:
        decision = "yes"

    elif credit >= 7 or income >= 7:
        if down_payment >= 5:
            decision = "yes"
        else:
            decision = "no"
    elif credit < 7 and income < 7:
        decision = "no"
else:
    if credit < 4:
        decision = "no"
    else:
        if income >= 7 or down_payment >=  7:
            decision = "yes"
        elif income >= 4 and down_payment >= 4:
            decision = "yes"
        else:
            decision = "no"

print(f'Decision: {decision}')