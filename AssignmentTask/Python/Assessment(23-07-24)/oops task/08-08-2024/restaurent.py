# 9-1. Restaurant: Make a class called Restaurant. The init() method for 
# Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
# different instances from the class, and call describe_restaurant() for each 
# instance.



class Restaurent:
    def __init__(self,restaurent_name,cuisine_type) -> None:
        self.restaurent_name=restaurent_name
        self.cuisine_type=cuisine_type
        
    def describe_restaurent(self):
        print(f'Restaurent Name : {self.restaurent_name}')
        print(f'Cuisine Type : {self.cuisine_type}')
        
    def open_restaurent(self):
        print(f'{self.restaurent_name} is open now.....')
        
restaurent=Restaurent("Prasanth Kitchen","Indian dish")

print(f'Restaurent Name: {restaurent.restaurent_name}')
print(f'Cuisine Type : {restaurent.cuisine_type}')
print()
restaurent.describe_restaurent()
restaurent.open_restaurent()
print()
#9-2

restaurent1=Restaurent("Mani Taste","South Dish")
restaurent2=Restaurent("Tom Restaurent","Sushi ")
restaurent3=Restaurent("Burger King","Burger")

restaurent1.describe_restaurent()
restaurent2.describe_restaurent()
restaurent3.describe_restaurent()
        

    