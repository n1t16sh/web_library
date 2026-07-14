import sqlite3

class database:
    def connect(self):
        con=sqlite3.connect("library.db")
        cursor=con.cursor()

        return con, cursor

    def register_user(self,name,email,password,role,roll_number,department,year):
        con, cursor=self.connect()
        cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        mail=cursor.fetchone()
        if mail:
            cursor.close()
            con.close()
            return False
        
        cursor.execute("INSERT into users(name,email,password,role,roll_number,department,year) VALUES (?,?,?,?,?,?,?)",(name,email,password,role,roll_number,department,year))
        con.commit()
        con.close()
        return True

    def login_user(self,email,password):
        con ,cursor=self.connect()
        cursor.execute("SELECT * FROM users WHERE email=?",(email,))
        pas=cursor.fetchone()
        if not pas:
            con.close()
            return pas
        else:
            con.close()
            if pas[3]==password:
                return pas
            else :
                return None
