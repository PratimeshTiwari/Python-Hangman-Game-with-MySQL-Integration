import mysql.connector
try:
connection = mysql.connector.connect(host='localhost',
database='#',
user='root',
password='root')
sql_select_Query = "select distinct * from Record"
cursor = connection.cursor()
cursor.execute(sql_select_Query)

records = cursor.fetchall()
print("Total number of rows in table: ", cursor.rowcount)

print("\nPrinting each row")
for row in records:
    print("SNO = ", row[0], )
    print("USER = ", row[1])
    print("STATUS  = ", row[2])
    print()
except mysql.connector.Error as e:
print("Error reading data from MySQL table", e)
finally:
if connection.is_connected():
connection.close()
cursor.close()
print("MySQL connection is closed")
