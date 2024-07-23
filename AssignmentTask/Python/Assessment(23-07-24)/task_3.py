# 3 Question:Create a simple calculator which will take two input number from the
# user and give following option
# 1)Addition
# 2) Subtraction
# 3)Multiplication
# 4)Division
# (you can solve above question using normal function )
# (also try to solve using dictionary)

def add(x,y):
    return(x+y)

def sub(x,y):
    return(x-y)

def mul(x,y):
    return(x*y)

def div(x,y):
    return(x/y)

def main():
    x=int(input("Enter the number:"))
    y=int(input("Enter the number:"))
    print('1.add\n2.sub\n3.mul\n4.div')

    choice=int(input("Enter the choice: "))
    if choice == 1:
        print("The Addition of",x,"and",y,"is",add(x,y))
    elif choice == 2:
        print("The Subtraction of",x,"and",y,"is",sub(x,y))
    elif choice == 3:
        print("The Subtraction of",x,"and",y,"is",sub(x,y))
    elif choice == 4:
        print("The Subtraction of",x,"and",y,"is",div(x,y))
    else:
        print("wrong choice")
        
if __name__ == "__main__":
    main()
    