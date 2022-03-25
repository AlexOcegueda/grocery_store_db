import sqlite3

# customer database
con = sqlite3.connect("customer.db")

cur = con.cursor()

cur.execute("SELECT * FROM CUSTOMERS")

print(cur.fetchall())

con.commit()

con.close()
