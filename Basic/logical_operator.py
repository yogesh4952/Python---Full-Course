has_high_income= True
has_good_credit = True;

if has_high_income and has_good_credit:
    print("You're eligible for the top class loan")
elif not has_good_credit and has_high_income:
    print("You're eligible for the basic loan")
elif has_high_income or has_good_credit:
    print("You are onlyy cabale to to open bank account")

else:print("Thank You")