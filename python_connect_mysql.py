import mysql.connector
print("hellow world")

# Create a connection object
connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="govind",
  
)

# Create a cursor object
cursor = connection.cursor()
cursor.execute("show databases ;")
# Fetch the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

cursor.execute("use govind ;")
cursor.execute("show tables ;")

# cursor.execute(" ;")
results = cursor.fetchall()
for row in results:
    print(row)
cursor.execute("select * from table1 ;")
results = cursor.fetchall()
for row in results:
    print(row)

# cursor.execute(" ;")
# Close the cursor and connection
cursor.close()
connection.close()