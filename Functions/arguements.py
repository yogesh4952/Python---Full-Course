#In python there are 4 types of arguement
# -->Default arguments
# -->Postional Arguements
# -->Keyword arguements
# -->arbitary
#    -->A.P 
#    -->A.K


# def greet(name,dept,subject = "physics"):
#     print(f'Hi {name}')
#     print(f'Are you from {dept} department?')
#     print(f'You chooose {subject}?')

#Positional arguements
# greet("Yogesh","CS");

#KEYWORDS arguments
# greet(dept="CS",name="Yogesh",subject="Mathematics")
# greet("Yogesh","cs",subject="Mathematics")


#NOTE: if we add ,/ in function we allow pass only postional argument



#---------------------------------------------------------------------------------------



from itertools import tee


def greet(x ,/):
    print(f'Name is {x}');

greet("Yogesh")
# greet(x="Yogesh"); #This gives error

def greet1(*,x):
    print(f'Name is {x}');

# greet1("Yogesh")# greet1() only take keyword arguments
greet1(x="Yogesh")



#---------------------------------------------------------------------------------------


#Combine Positional-Only and Keyword-Only
# before  / , are positional-only, and any argument after the *, are keyword-only.

def greet2(a,b,c,/,*,y,z):
    print(a,b,c,y,z);

greet2("Yogesh",'Shah','Thakuri',z='Lamki',y = 'Kailali')


