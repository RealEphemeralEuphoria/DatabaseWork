import sqlite3
import csv

connection = sqlite3.connect("data.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Population 
               (City TEXT, Country TEXT, Pop_Number INT)''')

file = open ('population_data.csv')
city_data = csv.reader(file)
city_data.__next__()
cursor.executemany('''INSERT INTO Population VALUES (?, ?, ?)''', city_data)

country = 'Spain'
pop = 1000000

cursor.execute('''SELECT * FROM Population WHERE Country =? AND Pop_Number>?''', ('country', pop))
print(cursor.fetchall())

connection.commit()
connection.close()