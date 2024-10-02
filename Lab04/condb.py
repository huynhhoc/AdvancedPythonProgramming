import psycopg2
from psycopg2 import sql
from tkinter import messagebox
def connect():
    try:
        conn = psycopg2.connect(
            database = "dbtest",
            user="postgres",
            password="123456",
            host="localhost",
            port="5432"
        )
        #messagebox.showinfo("Success", f"Connected to database successfully!")
        return conn
    except Exception as ex:
        messagebox.showerror("Error", f"Error connecting to database")
def selectSV(cur):
    query = sql.SQL("select * from sinhvien")
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
def insertDB(conn, mssv, hoten):
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO sinhvien(mssv, hoten) values(%s, %s)",(mssv, hoten))
        conn.commit()
        print("Them thanh cong")
    except Exception as ex:
        conn.rollback()
        print(f"Error during insert")
if __name__ =="__main__":
    conn = connect()
    cur = conn.cursor()
    selectSV(cur)
    print("Insert sinhvien:-------------")
    insertDB(conn, '1323456789', 'Nguyen Hieu')
    selectSV(cur)
    conn.close()

