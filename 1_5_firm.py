income = int(input('Input income of the firm '))
exps = int(input('Input expenses of the firm '))
rev = income - exps
if rev < 0:
    print('Your firm is in minus')
elif rev == 0:
    print('Well, you have self-sustaining company, not bad =)')
else:
    print(f"Your firm is profitable and the profit is {income/rev:.2f}")
    stat = int(input('How many employees do you have? '))
    print(f"Income on one employee is {income/stat:.2f}")