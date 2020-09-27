"""
***WORK IN PROGRESS, UNFINISHED***


In this stage, create a database named card.s3db with a table titled card. It should have the following columns:

id INTEGER
number TEXT
pin TEXT
balance INTEGER DEFAULT 0
Pay attention: your database file should be created when the program starts, if it hasn’t yet been created. 
And all created cards should be stored in the database from now.
"""

import random
import sqlite3


def create_table():
    """Initiliase the table only if it doesn't already exist"""
    conn = sqlite3.connect('card.s3db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS card (
        id INTEGER PRIMARY KEY,
        number TEXT,
        pin TEXT,
        balance INTEGER DEFAULT 0
    )""")


    # Commit and close
    conn.commit()
    conn.close()


# TODO Keep balance as default for now but change this in later part
def add_customer(number, pin):
    """Add customer details permanently to the table and database"""
    conn = sqlite3.connect('card.s3db')
    c = conn.cursor()
    c.execute("INSERT INTO card VALUES (?,?)", (number, pin))
    # Commit and close
    conn.commit()
    conn.close()


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
    a = str(a).zfill(9) # ensures second part of card number is 9 digits long even with zeroes
    card_number = str(400000) + str(a)
    user_password = random.randint(0000, 9999)
    user_password = str(user_password).zfill(4) # ensures password is 4 digits long even with zeroes

    print("TESTING CARDNUM BEFORE LUHN:")
    print(card_number)
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

# Initialise table
create_table()


while looping:
    choice = input("1. Create an account \n2. Log into account \n0. Exit\n")
    
    if choice == '1':
        customer_details = create_account(customer_details)
    elif choice == '2':
        log_in(customer_details)
    elif choice == '0':
        print("You have successfully logged out!")
        looping = False
