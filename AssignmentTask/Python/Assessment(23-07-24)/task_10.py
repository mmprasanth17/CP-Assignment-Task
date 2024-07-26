#Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the function call provides,
# should print sandwich that's being ordered

def sandwich(*dish):
    for item in dish:
        print(item)
    
def main():
    toppings_add=[]
    toppings=input("Enter the topings to add :")
    toppings_add=toppings.split(',')
    sandwich(*toppings_add)
    
if __name__=="__main__":
    main()