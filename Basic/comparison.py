# temperature = 30

# if temperature>30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")


#------------------------Assignment---------------------------

name = input("Enter your name? ")
if len(name)<3:
    print("Your name must be at least 3 characters")
elif len(name)>50:
    print("Name must be can have maximum 50 characters")
elif len(name)>3 and len(name)<50: 
    print("Name looks good")

