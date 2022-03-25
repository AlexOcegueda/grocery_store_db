import sqlite3

# customer database
con = sqlite3.connect("customer.db")

cur = con.cursor()

# using doc string for readability
cur.execute("""CREATE TABLE customers (
    full_name text, 
    email text
    )""")

con.commit()

con.close()
