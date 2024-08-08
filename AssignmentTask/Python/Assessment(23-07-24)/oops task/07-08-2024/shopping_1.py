# Create a class representing a shopping cart. 
# Which include methods for adding items , removing items , 
# total items and total price

class shopping_cart:
    cart={}
    def adding_items(self):
           num=int(input("enter the no of items: "))
           for i in range(num):
               item=input("Enter the item to add:")
               price=float(int(input("Enter the price:")))
               shopping_cart.cart[item] = price
               print("Add itens:",shopping_cart.cart)
               
    def removing_items(self):
        remove=input("Enter the remove item:")
        if remove in shopping_cart.cart:
            shopping_cart.cart.pop(remove)
            print("Item",remove,"is successfully removed")
        else:
            print("Item not removed") 
            
    def total_items(self):
        total=len(shopping_cart.cart)
        print("Total items:",total)
        
    def total_price(self):
        total=0
        for i in shopping_cart.cart.values():
            total+=i
            
        print(total)

test=shopping_cart()
test.adding_items()
test.total_items()
test.total_price()
test.removing_items()
test.total_items()
test.total_price()
