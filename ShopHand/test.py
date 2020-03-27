import sqlite3

conn = sqlite3.connect("testShop.db")
c = conn.cursor()

c.execute("SELECT * FROM Repair_Job")
print(c.fetchall())

conn.commit()
conn.close()