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
