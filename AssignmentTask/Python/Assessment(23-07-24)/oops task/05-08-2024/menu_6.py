class Menu:
    items=[]
    def __init__(self):
        self.add_dish=""
        self.update_dish=""
        self.remove_dish=""
        
    def add(self):
        num=int(input("enter the no of items: "))
        for i in range(num):
            self.add_dish=input("Enter the item to add:")
            Menu.items.append(self.add_dish)
        print("Add itens:",Menu.items)
    
    def update(self):
        self.update_dish=input("Enter the update item:")
        if self.update_dish in Menu.items:
            new_update=input("Enter the new update:")
            index=Menu.items.index(self.update_dish)
            Menu.items[index]=new_update
        else:
            print("Item not updated")
            
    def remove(self):
        self.remove_dish=input("Enter the remove item:")
        if self.remove_dish in Menu.items:
            Menu.items.remove(self.remove_dish)
        else:
            print("Item not removed") 
    def display(self):
        print("Add item:",self.add_dish)
        print("update item:",self.update_dish)
        print("remove item:",self.remove_dish)
        print("list of items",Menu.items)

        
obj=Menu()
obj.add()
obj.update()
obj.remove()
print("---------Detail of menu------")
obj.display()
        