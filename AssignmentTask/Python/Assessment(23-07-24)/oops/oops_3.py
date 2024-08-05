class student:
    graduation="BE" # Class Variable
    def __init__(self,firstname,lastname):
        self.firstname=firstname #instance variable #properties
        self.lastname=lastname
        
obj1=student("prasanth","mani")
print(obj1.graduation) #direct
print(obj1.__class__.graduation) #special


print("======================================================")
#Creating Class
# diff between direct and special in graduation
class Student:
    Gradution = "BE"
    def __init__(self,firstname,lastname):
        self.firstname = firstname      #instance variable  #Properties
        self.lastname = lastname
        self.Gradution = "ME" # when we call graduation , this gives ME in the output

    def Display(self):
        print(f'{self.firstname} {self.lastname}')

obj = Student("Ajith","Kumar")
Student.Display(obj)

print(obj.Gradution) # ME
print(obj.__class__.Gradution) #BE


