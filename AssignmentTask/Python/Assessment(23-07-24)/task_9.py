import os
import filecmp

def remove(filename1,filename2):
    if (not os.path.exists(filename1)):
        print("not exists")
    elif (not os.path.exists(filename2)):
        print("not exists")
    else:
        compare=filecmp.cmp(filename1,filename2)
        print(compare)
        if compare==True:
           os.remove(filename1)
           print("sucess")


def main():
    file1=input("Enter filename1:")
    file2=input("Enter filename2:")
    remove(file1,file2)
if __name__=="__main__":
    main()