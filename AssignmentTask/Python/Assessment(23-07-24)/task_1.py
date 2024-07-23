# 1) Create a menu_card list
# veg_starter = ['paneer 65','chilly paneer','veg crispy']
# 1) Display menu card
# 2)Add Starter in the menu card
# 3)Update Starter in the menu card
# 4)Remove Starter in the menu card
 
# Example:
# Add : Which starter you want to add in menu?
# paneer roll
# ['Paneer 65','Chilly paneer','Veg crispy','Paneer roll']
# Added Successfully


def main():
    print('Enter the size of the menu')
    size = int(input())
    data_input = []
    print('Enter the menu list : ')
    for i in range(size):
        menu = input()
        data_input.append(menu)
    print('List : ', data_input)
    print()
    data_input=add(data_input)
    data_input=update(data_input)
    data_input=remove(data_input)
    
def add(data_input):
    print("Which starter you want to add in menu?")
    add_item=input("Enter the item:")
    data_input.append(add_item)
    print(add_item,"add successfully")
    print()
    print("list:",data_input)
    return data_input
    
def update(data_input):
    print("Which item do you want to update in the menu?")
    print("Current menu items:", data_input)
    update_menu = input("Enter the item to update: ")
    if update_menu in data_input:
        new_menu = input("Enter the new item: ")
        index = data_input.index(update_menu)
        data_input[index] = new_menu
        print(f"Updated {update_menu} to new {new_menu}")
    else:
        print("Item not found")
    return data_input
        
def remove(data_input):
        print("Which starter you want to remove in menu?")
        remove_item=input("Enter the remove item:")
        data_input.remove(remove_item)
        print(remove_item,"successfully removed")
        print()
        print("After removed menu:",data_input)
        return data_input


    
if __name__ == "__main__":
    main()
