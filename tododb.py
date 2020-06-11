import sqlite3

class Database:
    def __init__(self, db):
        self.db = ""
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY, tasks text)")
        self.conn.commit()

    
    def insert(self, tasks):
        self.cur.execute("INSERT INTO todo VALUES (NULL, ?)",(tasks, )) 
        self.conn.commit()
    
    def remove(self, id):
        self.cur.execute("DELETE FROM todo WHERE id=?",(id,))
        self.conn.commit()
   
    def get_id(self, task):
        self.execute("SELECT FROM todo WHERE id=?", (task, ))
        slef.conn.commit()
    
    def clear_data(self):
        self.cur.execute("DELETE FROM todo")
        self.conn.commit()
        
    def __del__(self):
        self.conn.close()



