# class Base:
#     def setFirstName(self,fname):
#         self.fname = fname
#     def setLastName(self,lname):
#         self.lname = lname
#     def __init__(self):
#         print("Constructor is called")

#     def print(self):
#         print(self.fname,self.lname);

# class Derived(Base):
#     pass;


# x = Derived();
# x.setFirstName("Yogesh");
# x.setLastName("Shah Thakuri");
# x.print();

        


class Base:
    def setFirstName(self,fname):
        self.fname = fname
    def setLastName(self,lname):
        self.lname = lname
    def __init__(self):
        print("Constructor is called")

    def print(self):
        print(self.fname,self.lname);

class Derived(Base):
    def __init__(self):
        pass;


x = Derived();
x.setFirstName("Yogesh");
x.setLastName("Shah Thakuri");
x.print();