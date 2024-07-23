#5 question:Write a program to check if a string contains any special character


def frequency(string):
    special_char="!@#$%^&*()_+{}/*>?<"
    temp=0
    for i in string:
        if i in special_char:
            var=i
            temp=1
    if temp==1:
        print(var,"-> This string  contain specail character")
    else:
        print("Doesn't contain any special character")

def main():
    string=input("Enter the string name:")
    frequency(string)
if __name__=="__main__":
    main()