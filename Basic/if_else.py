price = 1000000;
has_good_credit = True;
has_high_income = True;


if has_good_credit and has_high_income:
    print("You're eligible to taking loan!")
    down_payment  = 0.1*price;

else: 
    down_payment = 0.2*price

print(f'Down Paymen {down_payment}')
