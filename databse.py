import sqlite3

class database:
    def connect(self):
        con=sqlite3.connect("library.db")
        cursor=con.cursor()

        return con, cursor

    def register_user(self,name,email,password):
        con, cursor=self.connect()
        cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        mail=cursor.fetchone()
        if mail:
            return False
        else:
            cursor.execute("INSERT into users(name, email, password) VALUES (?,?,?)",(name,email,password))
            con.commit()
            return True

        con.close()

    def login_user(self,email,password):
        con ,cursor=self.connect()
        cursor.execute("SELECT password FROM users WHERE email=?",(email,))
        pas=cursor.fetchone()
        if not pas:
            return False
        return pas[0]==password

        con.close()

