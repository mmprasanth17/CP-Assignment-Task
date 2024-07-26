

# file_read = open('calculator.py','r')
# print(file_read.read())

import os 
def Createfile(filename):
    #filename=fileread.py
    if(os.path.exists(filename)):
        print("file already exist")
    else:
        file_create=open(filename,'w')
    pass

def main():
    print("Enter the file you need to create ")
    file_name=input()
    
    Createfile(file_name)
    
if __name__=="__main__":
    main()