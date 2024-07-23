#4 question:Write a program which will count the frequency of letters of the string


def frequency(string,word):
    count=0
    for k in string:
        if(k==word):
            count+=1
    return count

def main():
    string=input("Enter the string name:")
    word=input("Enter the word to check:")
    count=frequency(string,word)
    print(word,"is repeating",count,"times")
    
if __name__=="__main__":
    main()