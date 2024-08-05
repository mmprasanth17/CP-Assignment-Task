
class Bank:
    Bank_Name="State Bank of India"
    ROI_On_FD=8.9
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
        print("Your Bank Account :",self.Bank_Name)
        print("Your ROI_On_FD :",self.ROI_On_FD)
    @classmethod   
    def DisplayBankInformation(cls):
        print("Name of the Bank :",cls.Bank_Name)
        print("Your Rate of intrest :",cls.ROI_On_FD)
def main():
    user1=Bank()
    print("Create Account")
    user1.CreateAccount()
    print()
    print("---Your Account Details---")
    user1.DisplayAccountInfo()
    print()
    print("---DisplayBankInformation---")
    user1.DisplayBankInformation()
    print()
    
if __name__=="__main__":
    main()
    