#Define with def keyword
def my_function(fname):
    if len(fname)>8:
        print("Please enter shorter name");
    else:
        print(fname + " Hello from the function!");
my_function("Teri");



#NOTE: If we don't know how many arguements are pass through the function use * recieve tuple

def listItem(*list):
    for x in list:
        print(x)

listItem("Yogesh",12,True,False)





#NOTE: We can also pass key-value pairs in the function

def longest(child1, child2,child3):
    print("The value of the key child1 is" + child1);

#Yo chai parameter j xa arguement ni tei huna paarxa
longest(child1="yogesh", child2="Jasmin", child3="sandhya")



#---------------------------------------------------------------------------------------



#If we don't know how vany kyeword are pass we use ***

def dami(**kids):
    for x in kids.items():
        print(x);

dami(over="oii",dami = "kada haita");



#---------------------------------------------------------------------------------------
# if we want to pass nothing or define garna lai kei content xaina vane we use pass keyword

def sakkyo():
    pass;