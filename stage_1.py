"""
You should allow customers to create a new account in our banking system.

Once the program starts, you should print the menu:

1. Create an account
2. Log into account
0. Exit
If the customer chooses ‘Create an account’, you should generate a new card number which satisfies all the conditions described above. 
Then you should generate a PIN code that belongs to the generated card number. A PIN code is a sequence of any 4 digits. PIN should be 
generated in a range from 0000 to 9999.

If the customer chooses ‘Log into account’, you should ask them to enter their card information. Your program should store all generated 
data until it is terminated so that a user is able to log into any of the created accounts by a card number and its pin. You can use an 
array to store the information.

After all information is entered correctly, you should allow the user to check the account balance; right after creating the account, 
the balance should be 0. It should also be possible to log out of the account and exit the program.
"""

import random

def create_account(customer):
    """Create a card and pin and then return these values as a list"""
    random.seed()
    
    a = random.randint(0000000000, 9999999999)
    card_number = str(400000) + str(a)
    user_password = random.randint(0000, 9999)
    user_password = str(user_password).zfill(4) # ensures password is 4 digits long even with zeroes
    
    txt = "Your card has been created \nYour card number: \n{cardnum}"\
          "\nYour card PIN: \n{cardpin}".format(cardnum = card_number, cardpin = user_password)
    print(txt)
          
    customer = [card_number, user_password]  
    return customer

def log_in(customer):
    """Verify if user details exist and are correct"""
    card_check = input("Enter your card number: ")
    password_check = input("Enter your PIN:")
    
    if card_check == customer[0] and password_check == customer[1]:
        print("You have successfully logged in!")
    else:
        print("Wrong card number or PIN!")


customer_details = [] # initialise empty array to store user details
looping = True # define while loop condition

while looping:
    choice = input("1. Create an account \n2. Log into account \n0. Exit\n")
    
    if choice == '1':
        customer_details = create_account(customer_details)
    elif choice == '2':
        log_in(customer_details)
    elif choice == '0':
        print("You have successfully logged out!")
        looping = False
