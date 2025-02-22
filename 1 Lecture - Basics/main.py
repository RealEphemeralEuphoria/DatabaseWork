import sqlite3

# name = input ("Name? ")
# position = input ("Position? ")


connection = sqlite3.connect ("hr.db")
cursor = connection.cursor ()
cursor.execute('''CREATE TABLE IF NOT EXISTS Employees 
               (Emp_ID INT, Name TEXT, Position TEXT)''')


cursor.execute ('''update Employees set Position = 'Meep Morp!' where name = "Kaya"''')

connection.commit()
connection.close()