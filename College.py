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
    stuOptions()
    contVar = 'y'
    while contVar == 'y':
        #5 options each
        choice = int(input('Choose your option from the menu.'))
        if choice == 1:
            name, depID, majID = newStuInfo()
            print(f'New Student: {name}, Department: {depID}, Major: {majID} ')
            proVar = input('Add new student (y/n)?').lower()
            if proVar == 'y':
                insertStu(name, depID, majID)
        elif choice == 2:
            name = input('Enter the name of the student you want to find: ').lower()
            findStu(name)
        elif choice == 3:
            stuID = int(input('Enter the Student ID: '))
            name, depID, majID = newStuInfo()
            changeStu(stuID, name, depID, majID)
        elif choice == 4:
            stuID = int(input('Enter the ID of the Student you wish to Delete: '))
            delStu(stuID)
            
        elif choice == 5:
            showAllStu()
        else:
            print('Pick an option from the menu.')
        contVar = input('Perform another action on this table (y/n)?').lower()
        
def showAllStu():
    conn = None
    try:
        conn = sqlite3.connect('college.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Students''')
        results = cur.fetchall()
        print('Results: ')
        for row in results:
            print(f'ID: {row[0]}, Name: {row[1]}, Department: {row[2]}, Major: {row[3]}')
    except sqlite3.Error as err:
        print(err)
    except Exception as err:
        print(err)
    finally:
        if conn != 0:
            conn.close()

def delStu(stuID):
    conn = None
    try:
        conn = sqlite3.connect('college.db')
        cur = conn.cursor()
        cur.execute('''DELETE FROM Students
                    WHERE StuID == ?''',
                    (stuID,))
        conn.commit()
    except sqlite3.Error as err:
        print(err)
    except Exception as err:
        print(err)
    finally:
        if conn != None:
            conn.close()
def changeStu(stuID, name, depID, majID):
    conn = None
    try:
        conn = sqlite3.connect('college.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Students
                    SET Name = ?, DepID = ?, MajorID = ?
                    WHERE StuID == ?''',
                    (name, depID, majID, stuID))
        conn.commit()
    except sqlite3.Error as err:
        print(err)
    except Exception as err:
        print(err)
    finally:
        if conn != None:
            conn.close()
    

def findStu(name):
    conn = None
    try:
        conn = sqlite3.connect('college.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Students
                    WHERE lower(Name) == ?''',
                    (name.lower(),))
        results = cur.fetchall()
        print('Search Results: ')
        for row in results:
            print(f'ID: {row[0]}, Name: {row[1]}, Department: {row[2]}, Major: {row[3]}')
    except sqlite3.Error as err:
        print(err)
    except Exception as err:
        print(err)
    finally:
        if conn != None:
            conn.close()

def newStuInfo():
    #name, depID, majID
    name = input("Enter the student's name: ")
    depID = int(input("Enter the student's Department ID: "))
    majID = int(input("Enter the student's Major ID: "))
    return name, depID, majID

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
    print('1. Add a Student')
    print('2. Search for a Student')
    print('3. Change Student information')
    print('4. Delete Student Records')
    print('5. Show all Students')
def depOptions():
    print('Options:')
    print('1. Add a Department')
    print('2. Search for a Department')
    print('3. Change Department information')
    print('4. Delete Department Records')
    print('5. Show all Departments')
def majOptions():
    print('Options:')
    print('1. Add a Major')
    print('2. Search for a Major')
    print('3. Change Major information')
    print('4. Delete Major Records')
    print('5. Show all Majors')