import os

def remove(filename1):
        os.remove(filename1)
        print("removed")

def main():
    file1=input("Enter the filename1:")
    remove(file1)
    
if __name__=="__main__":
    main()