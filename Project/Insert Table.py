import sqlite3
import webscrapping

conn=sqlite3.connect("ProjectDB.db")

conn.execute('''
               insert into Project
               values(?,?)
            ''',(website,keyword)
             )
conn.commit()

print("Data inserted successfully")




