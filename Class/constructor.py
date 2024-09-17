#whenever the objectis created the construcotr run at first we use __intit__() to dclare construcotr

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age= age;

# p1 = Person("Yogesh",17)
# print(p1.name);
# print(p1.age)

#NOTE: The __init__() function is called automatically every time the class is being used to create a new object. 


#-------------------------------------------------------------------------------


# __str__() -> return k garne when the class object is represneted as string
#basically output kun format ma dekhaune teigarxa

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self) :
        return f'{self.name}({self.age})'
    
p1 = Person("Yogesh Shah",17);
print(p1)#output: Yogesh Shah(17)


         
        
