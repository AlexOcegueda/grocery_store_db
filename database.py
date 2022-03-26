"""

This program was created to test out functions with a dummy database. It includes functions
to add random customers with an API and also to display the full customers table.

"""
import sqlite3
import requests

# connect to customer database
con = sqlite3.connect("customer.db")
# cursor to make changes in database
cur = con.cursor()

__program_name__ = "Al-ex Grocery Mart"
__author__ = 'Alex Ocegueda'
__version__ = '1.0'

def search_customers_table(name=None, id=None):
    """
    
    This will search for a customer by their name or by their unique primary key.
    If the name or key is not found, it will return an error message.
    
    format: search_customers_table(name, id)  -> make sure to put 'None' for name or id if you don't want to search by name or id
    
    """
    if name != None:
        cur.execute("SELECT * FROM customers WHERE full_name= ?", (name,))

        if(cur.fetchone() == None):
            print("Customer not found")

    elif id != None:
        cur.execute("SELECT * FROM customers WHERE rowid = ?", (id,))
    else:
        print("Error - Please enter a name or id to search for.")
        return

    for customer in cur.fetchall():
        print(customer)

def display_customers_with_id():
    """
    
    Displays the customer with their unique primary key.

    """
    cur.execute("SELECT rowid, * FROM customers")  # Retrieves everything from customers table

    for customer in cur.fetchall():
        full_name = customer[0]
        email = customer[1]

        print(f"{full_name} \t - \t {email}")

def display_customers_table():
    """

    This shows everything that is store in the 'customers' database

    """
    cur.execute("SELECT * FROM customers")  # Retrieves everything from customers table
    
    for customer in cur.fetchall():
        full_name = customer[0]
        email = customer[1]

        print(f"{full_name} \t - \t {email}")


def add_new_customer():
    """

    This will use a fake person generator API to create and add new person to the database.
    This will include their name and an url to their email.

    """

    response = requests.get('https://api.namefake.com/')

    add_customer = [
        (response.json()['name'], response.json()['email_url']),
    ]

    cur.executemany("INSERT INTO customers VALUES (?,?)", add_customer)


def main():
    
    search_customers_table(name='Jane Doe')
    
    con.commit()  # Commit changes in database

    con.close()  # Closes out of database


if __name__ == "__main__":
    main()
