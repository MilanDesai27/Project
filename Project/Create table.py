import sqlite3

conn=sqlite3.connect('ProjectDB.db')
conn.execute('''
                create table project
                (
                  name text,
                  keywords text
                 )
             ''')

print("Database and table created successfully!!!")
