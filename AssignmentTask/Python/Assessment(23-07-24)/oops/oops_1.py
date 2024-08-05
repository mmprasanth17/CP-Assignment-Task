#creating class
# class student:
    
#     def __init__(self,firstname,lastname):
#         self.firstname=firstname #instance variable #properties
#         self.lastname=lastname
    
#     def Display(self):  #instance method
#         print(f'{self.firstname} {self.lastname}')
        
# obj1=student("prasanth","mani")
# obj2=student("mani","roja")
# print(obj1.firstname,obj1.lastname)
# obj2.Display()


class mobile:
    def __init__(self,Brand,Ram):
        self.Brand=Brand
        self.Ram=Ram
    def Display(self):
        print(f'{self.Brand} {self.Ram}')
        
obj1=mobile("Redmi","8gb")
# print(obj1.Brand,obj1.Ram)
obj1.Display()