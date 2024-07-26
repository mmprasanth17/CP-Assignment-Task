#
# create dummy text file append data 

import os


def insert(file):
    if (not os.path.exists(file)):
        print("Not exists")
    else:
        add=input("Text to add :")
        append=open(file,'a')
        append.writelines([add])
        print("sucess")

def main():
    user=input("File to insert or append:")
    insert(user)

    
    
if __name__=="__main__":
    main()