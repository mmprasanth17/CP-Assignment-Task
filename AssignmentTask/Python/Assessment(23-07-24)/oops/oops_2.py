#Instance variable : Name,Amount,Address,AccountNo
#Instance Method : CreateAccount, DisplayAccountInfo()

# class Bank:
#     def __init__(self,Name,Amount,Address,AccountNo) -> None:
#         self.Name=Name
#         self.Amount=Amount
#         self.Address=Address
#         self.AccountNo=AccountNo
        
#     def CreateAccount(self):
#         print(f'{self.Name} {self.AccountNo}')
#     def DisplayAccountInfo(self):
#         print(f'{self.Name} {self.Address} {self.AccountNo} {self.Amount}')
    
# obj1=("Prasanth",1234567)
# obj2=("mani","chennai",1234567,14000)
# obj1.CreateAccount()
# obj2.DisplayAccountInfo()

class Bank:
    def __init__(self) -> None:
        self.Name=""
        self.Amount=0
        self.Address=""
        self.AccountNo=""
        
    def CreateAccount(self):
        self.Name=input("Enter the Name :")
        self.Amount=int(input("Enter the Amount :"))
        self.Address=input("Enter the Adress :")
        self.AccountNo=int(input("Enter the Account No :"))
        
    def DisplayAccountInfo(self):
        print("Name of Account Holder :",self.Name)
        print("Amount you Entered :",self.Amount)
        print("Adress of Account Holder :",self.Address)
        print("Account No :",self.AccountNo)
        
def main():
    user1=Bank()
    print("Create Account")
    user1.CreateAccount()
    print()
    print("---Your Account Details---")
    user1.DisplayAccountInfo()
    print()
    
if __name__=="__main__":
    main()
    
        