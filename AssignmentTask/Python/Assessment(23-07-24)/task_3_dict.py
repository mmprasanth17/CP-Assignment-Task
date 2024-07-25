def Addition(value_1, value_2):
    return value_1 + value_2

def Subtraction(value_1, value_2):
    return value_1 - value_2

def Multiplication(value_1, value_2):
    return value_1 * value_2

def Division(value_1, value_2):
        return value_1 / value_2

def main():
    cal = {
        "+": Addition,
        "-": Subtraction,
        "*": Multiplication,
        "/": Division
    }
    
    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice : ")
        
        if choice == '5':
            print("Exiting the program.")
            break
        elif choice in cal:
            num1 = float(input("Enter the number 1: "))
            num2 = float(input("Enter the number 2: "))
            
            result = cal[choice]
            final_result = result(num1, num2)
            print("Result:", final_result)
        else:
            print("Invalid choice. Please enter a correct choice.")

if __name__ == "__main__":
    main()
