#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3 as sql


# In[2]:


#connect to SQLite
con = sql.connect('assignment3.db')

#Create a Connection
cur = con.cursor()

#Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS student")

#Create users table  in db_web database
sql ='''CREATE TABLE "student" (
	"student_id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"first_name"	TEXT,
	"last_name"	TEXT,
    "dob"	TEXT,
    "amount_due"	TEXT
)'''
cur.execute(sql)

#commit changes
con.commit()

#close the connection
con.close()


# In[ ]:





# In[ ]:




