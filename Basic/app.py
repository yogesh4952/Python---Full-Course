# Here we learn how to take input

# a = input("What is your name? ")
# b = input("What is your favorite color? ");

# print("Your name is:" ,a)
# print(a," favorite color is:", b)



#------------------------------------------------------------------



#Here we take input age from the user and calculate the age -->>Type conversion

# birth_year = input("BirthYear: ");
# print(type(birth_year))
# age = 2022 - int(birth_year)
# print(type(age))
# print(age)


#------------------------------------------------------------------


#program to ask a user their weight(in pounds), convert it to kg and print it on the terminal

# _pound  = input("Enter your age in pound: ")
# _kg = int(_pound) * 0.45359237;
# print("Your weight in kg is: ", _kg)



#------------------------------------------------------------------




#Formatted string -->if we want to print yogesh [shah] is a coder then we do followng

# first  = 'Yogesh'
# last = "Shah"
# msg = f'{first} [{last}] is a coder'
# print(msg)



#------------------------------------------------------------------



#string methods

# course = "Python for beginners!"
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find('P'))
# print(course.replace("beginners",'absolute beginners'))
# print('for' in course)



#------------------------------------------------------------------


# print(10**3);  #this is 10 power 2

#MATH FUNCTIONS

# import math

# print(math.ceil(2.9))
# print(math.floor(2.9))

# x = 2.9;
# print(round(x))
# print(abs(-x))



#------------------------------------------------------------------


#    -------> if statement in python

is_hot = True
is_cold = False

if is_hot:
    print("It's a hot day") 
    print("Drink plenty of water")


elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")

else:
    print("It's a lovely day")


