def add(menu_card):
    add_item = input("Enter the item to add: ")
    add_price = int(input("Add a price: "))
    menu_card[add_item] = add_price
    print(menu_card)
    return menu_card

def update(menu_card):
    update_item = input('Enter dish name to update: ')

    if update_item in menu_card:
        update_price = int(input("Enter the new price of the dish: "))
        menu_card[update_item] = update_price
        print(menu_card)
    else:
        print(f"{update_item} not found in the menu.")

    return menu_card

def remove(menu_card):
    remove_item = input("Enter the dish name to remove: ")

    if remove_item in menu_card:
        menu_card.pop(remove_item)
        print(f"{remove_item} has been removed.")
    else:
        print(f"{remove_item} not found in the menu.")

    print(menu_card)
    return menu_card

def main():
    menu_card = {
        "Biriyani": 120,
        "Chicken Pepper": 100,
        "Veg Salad": 80,
        "French Fries": 90,
        "Burger": 50
    }
    while True:
        print("\nMenu Card:")
        for item, price in menu_card.items():
            print(f"{item}: {price}")

        print("\nOptions:")
        print("1. Display menu card")
        print("2. Add item to menu card")
        print("3. Update item in menu card")
        print("4. Remove item from menu card")
        print("5. Exit")

        choice = int(input("Enter the choice to do: "))
        if choice == 1:
            # Display menu card (already displayed above)
            continue
        elif choice == 2:
            menu_card = add(menu_card)
        elif choice == 3:
            menu_card = update(menu_card)
        elif choice == 4:
            menu_card = remove(menu_card)
        elif choice == 5:
            print("Exit.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
