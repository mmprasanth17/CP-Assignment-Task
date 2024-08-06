class Numbers:
    var=0
    def __init__(self) -> None:
        self.value1=0
        self.value2=0
    
    def Accept(self):
        self.value1=int(input("Enter the value 1 : "))
        self.value2=int(input("Enter the value 2 : "))
        
    def Addition(self):
        self.Addition=(self.value1+self.value2)
        return self.Addition
    def Subtraction(self):
        self.Addition=(self.value1-self.value2)
        return self.Addition
    def Multiplication(self):
        self.Addition=(self.value1*self.value2)
        return self.Addition
    def Division(self):
        self.Addition=(self.value1/self.value2)
        return self.Addition
obj=Numbers()
obj.Accept()
print("------Value of operator-----")
print("Addition:",obj.Addition())
print("Subtraction:",obj.Subtraction())
print("Multiplication:",obj.Multiplication())
print("Division:",obj.Division())