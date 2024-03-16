#creta a atm system

''' 1)rupaee
    2)visa
    3)mastercard
    1-->> display the remaining amount
   2-->> authentication of user username and password
   3-->>if the user is authenticated  the given the following options:
   1)check balance
   2)cash withdrawal
   3) cash deposit
   4)mini statement of last three transcation
   
   
'''
def login():
        while True:
            username=input("enter the username:")
            password=input("enter the password:")
            if username==password:
                print("login successfully")
                break
            else: 
                print("try again")
login()
