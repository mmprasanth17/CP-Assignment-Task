 
# 2 Question:Write a program which will take input from the user and Returns(Using function)
# 1)Addition on the list
# Example: [2,3,4,5,6,7]  --> 27
# Note: don't use sum()
# 2)Maximum from the list
# Example: [2,3,4,5,6,7]  --> 7
# Note: don't use max()


def Addition(value):
    total = 0
    for num in value:
        total += num
    return total

def Maximum(value):
    max_value = value[0]
    for num in value:
        if num > max_value:
            max_value = num
    return max_value

def main():
    size = int(input("Enter the size of the list: "))
    input_user = []
    
    for i in range(size):
        num = int(input("Enter number: "))
        input_user.append(num)
    
    print("The list of numbers is:", input_user)
    
    Add_result = Addition(input_user)
    print("Addition on list:", Add_result)
    
    max_result = Maximum(input_user)
    print("Maximum number in list:", max_result)

if __name__ == "__main__":
    main()
