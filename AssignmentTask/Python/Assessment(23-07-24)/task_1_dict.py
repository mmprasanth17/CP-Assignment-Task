def add_items(menu_card):
    print('To add a dish:')
    add_dish = input("Enter veg or non-veg: ")
    dish_name = input("Enter your dish name to add: ")
    dish_price = int(input("Enter the price of the dish: "))

    menu_card[add_dish][dish_name] = dish_price
    print(menu_card)
    return menu_card

def remove_items(menu_card):
    print('What item do you want to remove:')
    remove_dish = input("Enter veg or non-veg: ")
    remove_dishname = input("Enter your dish name to remove: ")
    dishes = menu_card[remove_dish]

    dishes.pop(remove_dishname, None)
    menu_card[remove_dish] = dishes
    print(menu_card)
    return menu_card

def update_items(menu_card):
    print('What item do you want to update:')
    select_dish = input('Enter veg or non-veg: ')
    select_dishname = input('Enter dish name to update: ')
    dish_price = int(input("Enter the new price of the dish: "))
    dishes = menu_card[select_dish]

    if select_dishname in dishes:
        dishes[select_dishname] = dish_price
        menu_card[select_dish] = dishes
        print(menu_card)
    else:
        print(f"{select_dishname} not found in {select_dish} menu.")
    return menu_card

def main():
    menu_card = {
        'non-veg': {
            'Biryani': 250,
            'Grill': 400,
            'Prawn fry': 200,
            'Kebab': 300
        },
        'veg': {
            'Sambar-Rice': 100,
            'Curd-Rice': 80,
            'Meals': 150,
            'Parotta': 50
        }
    }

    def print_menu():
        print("\nMenu:")
        for category, items in menu_card.items():
            print(f"{category.capitalize()}:")
            for item, price in items.items():
                print(f"  {item}: {price}")
        print("\n")

    actions = {
        '1': add_items,
        '2': remove_items,
        '3': update_items
    }

    while True:
        print_menu()
        print("Select an action:")
        print("1. Add a dish")
        print("2. Remove a dish")
        print("3. Update a dish")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__== "__main__":
    main()
