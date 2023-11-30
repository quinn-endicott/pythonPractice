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

def stuCRUD():
    pass

def newStuInfo():
    #name, depID, majID
    name = input("Enter the student's name: ")
    depID = int(input("Enter the student's Department ID: "))
    majID = int(input("Enter the student's Major ID: "))
    return name, depID, majID
     
    pass
def insertStu(name, depID, majID):
    conn = None
    try:
        conn = sqlite3.connect('college.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO Students(Name, DepID, MajorID)
                    VALUES (?, ?, ?)''',
                    (name, depID, majID))
        conn.commit()
    except sqlite3.Error as err:
        print(err)
    except Exception as err:
        print(err)
    finally:
        if conn != 1:
            conn.close()
            
def depCRUD():
    pass
def majCRUD():
    pass

def stuOptions():
    print('Options:')
    print('Add a Student')
    print('Search for a Student')
    print('Change Student information')
    print('Delete Student Records')
    print('Show all Students')
def depOptions():
    print('Options:')
    print('Add a Department')
    print('Search for a Department')
    print('Change Department information')
    print('Delete Department Records')
    print('Show all Departments')
def majOptions():
    print('Options:')
    print('Add a Major')
    print('Search for a Major')
    print('Change Major information')
    print('Delete Major Records')
    print('Show all Majors')