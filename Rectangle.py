class rectangle:
    def __init__(self,length, width):
        self.length = length
        self.width = width

    def area(self):
            return self.length*self.width

    def perimeter(self):
            return (self.length+self.width)*2
        
Length = float(input("Input length: "))
Width = float(input("Input width: "))
rec1 = rectangle(Length,Width)

print("Area:", rec1.area())
print("Perimeter:", rec1.perimeter())
    