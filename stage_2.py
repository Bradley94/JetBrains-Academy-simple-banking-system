"""
Stage 2 is very similar except that now we need to ensure the 16th digit (checksum) passes the Luhn algorithm.

I chose to generate 15 digits and then create the checksum rather than generating 16 digits card numbers and testing each one
until a number is valid.
"""

import random

def luhn_checksum(card_number):
    """Apply Luhn Algorithm to obtain the checksum for 15 digit card"""
    
    # Convert number into a list so we can edit each index value
    num = [int(x) for x in str(card_number)]
    
    # Step 1: multiply each odd index by 2   
    for i in range(0, 15, 2): #  len(num) was falling one short so resorted to using int
        num[i] *= 2
    
    # Step 2: subtract 9 from any numbers greater than 9
    for i in range(0, 15):
        if num[i] > 9:
            num[i] -= 9
        else:
            continue
    
    # Step 3: total the 15 digits 
    total = 0
    for i in range(0, 15):
        total += num[i]
    
    # Step 4: multiply total by 9 and take the last digit which is our checksum
    total_2 = total * 9
    string_total_2 = str(total_2)
    checksum = string_total_2[-1]
    
    return checksum    

def create_account(customer):
    """Create a card and pin and then return these values as a list"""
    random.seed()
    
    a = random.randint(000000000, 999999999) # now 9 digits for checksum algorithm to work
    card_number = str(400000) + str(a)
    user_password = random.randint(0000, 9999)
    user_password = str(user_password).zfill(4) # ensures password is 4 digits long even with zeroes
    
    # find and add checksum
    checksum = luhn_checksum(card_number)
    card_number_final = str(card_number) + str(checksum)
    
    txt = "Your card has been created \nYour card number: \n{cardnum}"\
          "\nYour card PIN: \n{cardpin}".format(cardnum = card_number_final, cardpin = user_password)
    print(txt)
          
    customer = [card_number_final, user_password]  
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
