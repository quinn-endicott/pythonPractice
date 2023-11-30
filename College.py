import sqlite3
def createCollege():
    conn = None
    try:
        conn = sqlite3.connect('college.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE Majors (MajorID INTEGER PRIMARY KEY NOT NULL,
                    Name TEXT)''')
        cur.execute('''CREATE TABLE Departments (DepID INTEGER PRIMARY KEY NOT NULL,
                    Name TEXT)''')
        cur.execute('''CREATE TABLE Students (StuID INTEGER PRIMARY KEY NOT NULL,
                    Name TEXT,
                    DepID INTEGER,
                    MajorID INTEGER,
                    FOREIGN KEY(MajorID) REFERENCES Majors(MajorID),
                    FOREIGN KEY(DepID) REFERENCES Departments(DepID))''')
        conn.commit()
    except sqlite3.Error as err:
        print(err)
    except Exception as err:
        print(err)
    finally:
        if conn != None:
            conn.close()