import sqlite3
con=sqlite3.connect("taskrecord.db")
print("Database created")
con.execute("create table record(Date_t TEXT DEFAULT CURRENT_TIMESTAMP,aid INTEGER PRIMARY KEY,qid INTEGER NOT NULL,State INTEGER NOT NULL,Amount INTEGER,Reason TEXT,Task_Count FLOAT )")
print("Table created successfully")
con.close()
