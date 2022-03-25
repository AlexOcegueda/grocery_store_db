import sqlite3

# customer database
con = sqlite3.connect("customer.db")

cur = con.cursor()

init_customers = [
    ('John Brown', 'JohnBro@gmail.com'),
    ('James Blue', 'Blue93@yahoo.com'),
    ('Mary Lorean', 'maryLor@gmail.com'),
]

cur.executemany("INSERT INTO customers VALUES (?,?)", init_customers)

con.commit()

con.close()
