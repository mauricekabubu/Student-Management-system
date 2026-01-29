from tkinter import messagebox
import sqlite3



conn = sqlite3.connect('student.db')  # This will create student.db in your project folder
cursor = conn.cursor()

# Create a sample table
def create_table(conn):
        query = '''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                grade TEXT
            )
        '''
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()


def insert(conn):
    query = 'INSERT VALUES INTO students(??)'
    password = int()
    email_address = ''
    cur = conn.cursor()
    cur.execute(query,password,email_address)
    conn.commit()
    row = 3
    conn.fetchone(row)
    if row.count>0:
        messagebox.showerror('SMS',message='invalid input')
