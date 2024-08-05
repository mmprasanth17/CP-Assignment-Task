# 4) Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount.
# That Class Contains one class variable as ROI which is initialize to 10.5
# Inside init method initialize all name and amount variable by accepting the values from user.
# There are four instance methods inside class as Display() , Deposit (), Withdraw( ), CalculateInterest()
# Deposit( ) method will accept the amount from user and add that value in class instance variable Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
# CalculateInterst() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI
# And Display () method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects

class Bank_Account:
    ROI=10.5
    def __init__(self) -> None:
        self.Name=""
        self.Amount=0

    def user(self):
        self.Name=input("Enter the name :")
        self.Amount=int(input("Enter the Amount:"))
        
    def Deposit(self):
        self.Amount +=int(input("Enter the Amount to Deposit:"))
    def Withdraw(self):
        self.Amount -=int(input("Enter the Amount to Withdraw:"))
        
    def CalculateInterst(self):
        Intrest=Bank_Account.ROI*self.Amount/100
        return Intrest
    def Display(self):
        print("Name:",self.Name)
        print("Amount:",self.Amount)
        print("Intrest:",self.CalculateInterst())
        
obj=Bank_Account()
obj.user()
obj.Deposit()
obj.Display()
obj.Withdraw()
obj.Display()
    