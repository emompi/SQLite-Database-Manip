# squlite database manipulation

import sqlite3
db = sqlite3.connect('java_programming_db')
cursor = db.cursor()  # Get a cursor object

cursor.execute('''
    CREATE TABLE java_programming(id INTEGER PRIMARY KEY, name TEXT,
                   	grade INTEGER)
''')
db.commit()

cursor = db.cursor()

# creating list of values to enter into table
to_enter = [[55, 'Carl Davis', 61],
            [66, 'Dennis Fredrickson', 88],
            [77, 'Jane Richards', 78],
            [12, 'Peyton Sawyer', 45],
            [2, 'Lucas Brooke', 99]]


# inserting values into table
cursor.executemany('''INSERT INTO java_programming(id, name, grade)
                  VALUES(?,?,?)''', to_enter)

# printing table to verify values have been inserted successfully
cursor.execute('''SELECT id, name, grade FROM java_programming''')
for row in cursor:
    print('{0} : {1} : {2}'.format(row[0], row[1], row[2]))

print('\n')

# selecting records with grade between 60 and 80
cursor.execute('''SELECT id, name, grade FROM java_programming WHERE grade > 60 AND grade < 80 ''')
for row in cursor:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} : {1} : {2}'.format(row[0], row[1], row[2]))

# changing 'Carl Davis' grade to 65
name = 'Carl Davis'
grade = 65
cursor.execute('''UPDATE java_programming SET grade=? WHERE name=?''', (grade, name))

# Deleting 'Dennis Fredrickson' row
cursor.execute('''DELETE FROM java_programming WHERE name="Dennis Fredrickson"''')

# Changing grades to 50 for IDs lower below 55
cursor.execute('''UPDATE java_programming SET grade=50 WHERE id < 55''')

print('\n')

# printing table final time to check results
cursor.execute('''SELECT id, name, grade FROM java_programming''')
for row in cursor:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} : {1} : {2}'.format(row[0], row[1], row[2]))

# creating new table from first table by taking two rows based on id
cursor.execute('''CREATE TABLE python_programming AS SELECT id, name, grade FROM java_programming WHERE id=77 OR id=2''')
print('\n')

# printing the new table to verifiy proper creation and insertion
cursor.execute('''SELECT id, name, grade FROM python_programming''')
for row in cursor:
    print('{0} : {1} : {2}'.format(row[0], row[1], row[2]))

# dropping both tables
cursor.execute('''DROP TABLE java_programming''')
print('\njava_programming table deleted!')
cursor.execute('''DROP TABLE python_programming''')
print('python_programming table deleted!\n')
