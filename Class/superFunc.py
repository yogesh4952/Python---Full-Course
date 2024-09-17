class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
    
    def Area(self):
        return self.length*self.width;

class Cube(Rectangle):
    def __init__(self, length, width,height):
        super().__init__(length, width)
        self.height =height
    
    def volume(self):
        return self.length*self.width*self.height;

s = Square(2,4)
v = Cube(2,2,4);

print(s.Area());
print(v.volume());