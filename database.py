import sqlite3
import requests

# connect to customer database
con = sqlite3.connect("customer.db")
# cursor to make changes in database
cur = con.cursor()


def display_full_table():
    """

    This shows everything that is store in the 'customers' database

    """
    cur.execute("SELECT * FROM customers")  # Retrieves everything from customers table
    print(cur.fetchall())


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

    for _ in range(2):
        add_new_customer()

    display_full_table()

    con.commit()  # Commit changes in database

    con.close()  # Closes out of database


if __name__ == "__main__":
    main()
