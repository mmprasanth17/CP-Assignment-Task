# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored 
# in a user profile. Make a method called describe_user() that prints a summary 
# of the user’s information. Make another method called greet_user() that prints 
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.

class User:
    def __init__(self,first_name,last_name,email,phone_no) -> None:
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.phone_no=phone_no
        
    def describe_user(self):
        print(f'user profile \n Name : {self.first_name} {self.last_name}\n Email : {self.email}\n Phone No:{self.phone_no}')
    
    def greet_user():
        print(f'Hey guys Above details are my user profile')
def main():      
    profile1=User("Prasanth","Mani","prasanth@gmail.com","942316345")
    profile2=User("Mani","Kanniyappan","mani@gmail.com","842316345")
    profile3=User("Roja","Mani","roja@gmail.com","742316345")

    User.greet_user()
    profile1.describe_user()
    profile2.describe_user()
    profile3.describe_user()
    
if __name__=="__main__":
    main()