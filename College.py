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
            print()
            proVar = input('Proceed to add new student (y/n)?').lower()
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
            print()
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
        print()
    except sqlite3.Error as err:
        print(err)
        print()
    except Exception as err:
        print(err)
        print()
    finally:
        if conn != None:
            conn.close()

def delStu(stuID):
    conn = None
    try:
        conn = sqlite3.connect('college.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''DELETE FROM Students
                    WHERE StuID == ?''',
                    (stuID,))
        conn.commit()
    except sqlite3.Error as err:
        print(err)
        print()
    except Exception as err:
        print(err)
        print()
    finally:
        if conn != None:
            conn.close()
def changeStu(stuID, name, depID, majID):
    conn = None
    try:
        conn = sqlite3.connect('college.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''UPDATE Students
                    SET Name = ?, DepID = ?, MajorID = ?
                    WHERE StuID == ?''',
                    (name, depID, majID, stuID))
        conn.commit()
    except sqlite3.Error as err:
        print(err)
        print()
    except Exception as err:
        print(err)
        print()
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
            print()
    except sqlite3.Error as err:
        print(err)
        print()
    except Exception as err:
        print(err)
        print()
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
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''INSERT INTO Students(Name, DepID, MajorID)
                    VALUES (?, ?, ?)''',
                    (name, depID, majID))
        conn.commit()
    except sqlite3.Error as err:
        print(err)
        print()
    except Exception as err:
        print(err)
        print()
    finally:
        if conn != None:
            conn.close()


    
            


def majCRUD():
    majOptions()
    contVar = 'y'
    while contVar == 'y':
        #5 options each
        choice = int(input('Choose your option from the menu.'))
        if choice == 1:
            name = newMajInfo()
            print(f'New Major: {name}')
            print()
            proVar = input('Proceed to add new Major (y/n)?').lower()
            if proVar == 'y':
                insertMaj(name)
        elif choice == 2:
            name = input('Enter the name of the Major you want to find: ').lower()
            findMaj(name)
        elif choice == 3:
            majID = int(input('Enter the Major ID: '))
            name= newMajInfo()
            changeMaj(majID, name)
        elif choice == 4:
            majID = int(input('Enter the ID of the Major you wish to Delete: '))
            delMaj(majID)
            
        elif choice == 5:
            showAllMaj()
        else:
            print('Pick an option from the menu.')
        contVar = input('Perform another action on this table (y/n)?').lower()

def newMajInfo():
    name = input("Enter the Major's name: ")
    return name

def insertMaj(name):
    conn = None
    try:
        conn = sqlite3.connect('college.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''INSERT INTO Majors(Name)
                    VALUES (?)''',
                    (name,))
        conn.commit()
    except sqlite3.Error as err:
        print(err)
        print()
    except Exception as err:
        print(err)
        print()
    finally:
        if conn != None:
            conn.close()

def findMaj(name):
    conn = None
    try:
        conn = sqlite3.connect('college.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Majors
                    WHERE lower(Name) == ?''',
                    (name.lower(),))
        results = cur.fetchall()
        print('Search Results: ')
        for row in results:
            print(f'ID: {row[0]}, Name: {row[1]}')
            print()
    except sqlite3.Error as err:
        print(err)
        print()
    except Exception as err:
        print(err)
        print()
    finally:
        if conn != None:
            conn.close()


def changeMaj(majID, name):
    conn = None
    try:
        conn = sqlite3.connect('college.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''UPDATE Majors
                    SET Name = ?
                    WHERE MajorID == ?''',
                    (name, majID))
        conn.commit()
    except sqlite3.Error as err:
        print(err)
        print()
    except Exception as err:
        print(err)
        print()
    finally:
        if conn != None:
            conn.close()
def delMaj(majID):
    conn = None
    try:
        conn = sqlite3.connect('college.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''DELETE FROM Majors
                    WHERE MajorID == ?''',
                    (majID,))
        conn.commit()
    except sqlite3.Error as err:
        print(err)
        print()
    except Exception as err:
        print(err)
        print()
    finally:
        if conn != None:
            conn.close()

def showAllMaj():
    conn = None
    try:
        conn = sqlite3.connect('college.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Majors''')
        results = cur.fetchall()
        print('Results: ')
        for row in results:
            print(f'ID: {row[0]}, Major: {row[1]}')
        print()
    except sqlite3.Error as err:
        print(err)
        print()
    except Exception as err:
        print(err)
        print()
    finally:
        if conn != None:
            conn.close()

def depCRUD():
    depOptions()
    contVar = 'y'
    while contVar == 'y':
        #5 options each
        choice = int(input('Choose your option from the menu.'))
        if choice == 1:
            name = newDepInfo()
            print(f'New Department: {name}')
            print()
            proVar = input('Proceed to add new Department (y/n)?').lower()
            if proVar == 'y':
                insertDep(name)
        elif choice == 2:
            name = input('Enter the name of the Department you want to find: ').lower()
            findDep(name)
        elif choice == 3:
            depID = int(input('Enter the Department ID: '))
            name= newDepInfo()
            changeDep(depID, name)
        elif choice == 4:
            depID = int(input('Enter the ID of the Department you wish to Delete: '))
            delDep(depID)
            
        elif choice == 5:
            showAllDep()
        else:
            print('Pick an option from the menu.')
            print()
        contVar = input('Perform another action on this table (y/n)?').lower()

def newDepInfo():
    name = input("Enter the Department's name: ")
    return name

def insertDep(name):
    conn = None
    try:
        conn = sqlite3.connect('college.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''INSERT INTO Departments (Name)
                    VALUES (?)''',
                    (name,))
        conn.commit()
    except sqlite3.Error as err:
        print(err)
        print()
    except Exception as err:
        print(err)
        print()
    finally:
        if conn != 1:
            conn.close()

def FindDep(name):
    conn = None
    try:
        conn = sqlite3.connect('college.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Departments
                    WHERE lower(Name) == ?''',
                    (name.lower(),))
        results = cur.fetchall()
        print('Search Results: ')
        for row in results:
            print(f'ID: {row[0]}, Name: {row[1]}')
            print()
    except sqlite3.Error as err:
        print(err)
        print()
    except Exception as err:
        print(err)
        print()
    finally:
        if conn != None:
            conn.close()

def changeDep(depID, name):

    conn = None
    try:
        conn = sqlite3.connect('college.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''UPDATE Departments
                    SET Name = ?
                    WHERE DepID == ?''',
                    (name, depID))
        conn.commit()
    except sqlite3.Error as err:
        print(err)
        print()
    except Exception as err:
        print(err)
        print()
    finally:
        if conn != None:
            conn.close()
def delDep(depID):

    conn = None
    try:
        conn = sqlite3.connect('college.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''DELETE FROM Departments
                    WHERE DepID == ?''',
                    (depID,))
        conn.commit()
    except sqlite3.Error as err:
        print(err)
        print()
    except Exception as err:
        print(err)
        print()
    finally:
        if conn != None:
            conn.close()
def showAllDep():
    conn = None
    try:
        conn = sqlite3.connect('college.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Departments''')
        results = cur.fetchall()
        print('Results: ')
        for row in results:
            print(f'ID: {row[0]}, Department: {row[1]}')
        print()
    except sqlite3.Error as err:
        print(err)
        print()
    except Exception as err:
        print(err)
        print()
    finally:
        if conn != 0:
            conn.close()


def stuOptions():
    print('Options:')
    print('1. Add a Student')
    print('2. Search for a Student')
    print('3. Change Student information')
    print('4. Delete Student Records')
    print('5. Show all Students')
    print()
def depOptions():
    print('Options:')
    print('1. Add a Department')
    print('2. Search for a Department')
    print('3. Change Department information')
    print('4. Delete Department Records')
    print('5. Show all Departments')
    print()
def majOptions():
    print('Options:')
    print('1. Add a Major')
    print('2. Search for a Major')
    print('3. Change Major information')
    print('4. Delete Major Records')
    print('5. Show all Majors')
    print()
def mainOptions():
    print('Choose a table to operate on: ')
    print('1. Students')
    print('2. Departments')
    print('3. Majors')
    print()