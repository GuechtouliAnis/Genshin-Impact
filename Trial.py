import sqlite3

# Connect to the database
conn = sqlite3.connect('GI_auto.db')

# Create a cursor called c
c = conn.cursor()

# Execute a query to retrieve data from the "Characters" table
c.execute("SELECT * FROM Characters ORDER BY Name ASC")

# Fetch all rows and print the "Names" column values
rows = c.fetchall()
for row in rows:
    print(row[0], row[1],"\t", row[2],"\t",row[3],"\t",row[4])

# Close the connection
conn.close()
