"""
Practice run for part 3 of simple banking project where the code needs to integrate SQLite to create a persistent database
"""

import sqlite3


# print our table
def show_all():
	conn = sqlite3.connect('card.db')
	c = conn.cursor()	

	c.execute("SELECT rowid, * FROM card")
	items = c.fetchall()

	for item in items:
		print(item)

	# Commit and close 
	conn.commit()
	conn.close()


# create table if it doesn't already exist
def create_table():
	conn = sqlite3.connect('card.db')
	c = conn.cursor()
	c.execute("""CREATE TABLE IF NOT EXISTS card (
					id INTEGER,
					number TEXT,
					pin TEXT,
					balance INTEGER DEFAULT 0
		)""")

	# Commit and close 
	conn.commit()
	conn.close()


# mock 'generation' of a customer
def customer_creator():
	id = 1
	card = "1234567890123456"
	pin = "9999"
	balance = 475

	conn = sqlite3.connect('card.db')
	c = conn.cursor()
	c.execute("INSERT INTO card VALUES (?,?,?,?)", (id, card, pin, balance))
	# Commit and close 
	conn.commit()
	conn.close()

def delete_one(id):
	conn = sqlite3.connect('card.db')
	c = conn.cursor()	
	c.execute("DELETE from card WHERE rowid = (?)", id)
	# Commit and close 
	conn.commit()
	conn.close()

def delete_all():
	conn = sqlite3.connect('card.db')
	c = conn.cursor()	
	c.execute("DROP TABLE card")
	conn.commit()
	conn.close()
			
# ensure table exists
create_table()
customer_creator()
show_all()
