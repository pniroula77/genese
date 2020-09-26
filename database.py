
import pymysql

class Database:
    def connect(self):
        return pymysql.connect(host='dbproject.cy5f1cqlob6l.us-east-1.rds.amazonaws.com',
                             user='admin',
                             password='rootroot',
                              db='dbproject')

    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM student_rec order by name asc")
            else:
                cursor.execute("SELECT * FROM student_rec where id = %s order by name asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self,data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO student_rec(name,email,phone,semester,faculty,address) VALUES(%s, %s, %s,%s,%s,%s)", (data['name'],data['email'],data['phone'],data['semester'],data['faculty'],data['address'],))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE student_rec set name = %s,email = %s, phone = %s, semester = %s, faculty = %s, address = %s where id = %s", (data['name'],data['email'],data['phone'],data['semester'],data['faculty'],data['address'],id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM student_rec where id = %s", (id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()
