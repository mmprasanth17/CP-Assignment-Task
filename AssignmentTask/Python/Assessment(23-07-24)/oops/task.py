class Demo:
    def __init__(self,value1,value2):
        self.value1=value1
        self.value2=value2
        
    def Fun(self):
        print(f'{self.value1} {self.value2}')
        
    def Gun(self):
        print(f'{self.value1} {self.value2}')
        
obj1=Demo(17,11)
obj2=Demo(27,10)

obj1.Fun()
obj1.Gun()
obj2.Gun()
obj2.Gun()

        