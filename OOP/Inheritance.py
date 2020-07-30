class Rectangle():
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Square(Rectangle):
    def __init__(self,length):
        super(Square,self).__init__(length,length)
        # Rectangle(self).__init__(length,length)
    
s = Square(5)
print(isinstance(s,Square))
print(s.area())
