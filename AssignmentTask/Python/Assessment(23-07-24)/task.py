#using for loop you have create a list of squraea number

def main():
    square = []
    size = int(input("Enter the number: "))
    for i in range(1, size + 1):
        square.append(i ** 2)
    print("After Square value is:",square)
  
if __name__ == "__main__":
    main()