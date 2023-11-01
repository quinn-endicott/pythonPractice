import pickle

def printCurrent(curOB):
    print(curOB.__str__())

def deleteEmp(empDic):
    delKey = int(input('Enter the ID of the employee to delete: '))
    while delKey not in empDic:
        if len(empDic) == 0:
            return 'no result'
            break
        else:
            delKey = int(input('Employee ID must exist, try again: '))
    popOB = empDic.pop(delKey)
    return popOB



def changeEmp(empDic):
    chKey = int(input('Enter the ID of the employee you want to modify: '))
    while chKey not in empDic:
        if len(empDic) == 0:
            return 'no result'
            break
        else:
            chKey = int(input('Employee ID must exist, try again: '))
    emOB = empDic[chKey]
    print('Current employee information: ')
    printCurrent(emOB)
    nVar = input("Change the employee's name (y/n)?").lower()
    if nVar == 'y':
        nName = input('Enter new name: ')
        emOB.set_name(nName)
    dVar = input("Change the employee's department (y/n)?").lower()
    if dVar == 'y':
        nDep = input('Enter the new department: ')
        emOB.set_department(nDep)
    tVar = input("Change the employee's job title (y/n)?").lower()
    if tVar == 'y':
        nTit = input('Enter the new job title: ')
        emOB.set_department(nTit)
    
    return 'result', emOB





def addEmp(empDic):
    empName = input("Enter the employee's name:")
    empNum = input('Enter a unique 5 digit employee ID: ')
    empInt = int(empNum)
    while len(empNum) != 5 or empInt in empDic:
        if len(empNum) != 5 and empInt in empDic:
            empNum = input('ID number must be both 5 digits and unique, try again: ')
            empInt = int(empNum)
        elif empNum in empDic:
            empNum = input('ID must be unique, try again: ')
            empInt = int(empNum)
        else:
            empNum = input('ID must be 5 digits, try again: ')
            empInt = int(empNum)
    empDepartment = input('Enter the department the employee works in: ')
    empTitle = input("Enter the employee's job title: ")
    newEmp = employee.Employee(empName, empInt, empDepartment, empTitle)
    empDic[empInt] = newEmp
    return newEmp

def loadEmpDic(FILE):
    try:
        with open(FILE, 'rb') as empFile:
            empOut = pickle.load(empFile)
    except:
        empOut = {}
    return empOut

def getMenuChoice():
    print('Menu Options:')
    print('1: Look up an employee')
    print('2: Add an employee')
    print('3: Change employee information')
    print('4: Delete an employee')
    print('5: Quit')
    menuChoice = int(input('What do you want to do?  '))

    while menuChoice < 1 or menuChoice > 5:
        menuChoice = int(input('Enter one of the choices:  '))

    return menuChoice

def lookUp(empDic):
    contVar = 'y'
    searchKey = int(input('Enter the ID number of the employee to look up: '))
    try:
        while searchKey not in empDic:
            if len(empDic) == 0:
                break
            contVar = input('Would you like to try again(y/n): ').lower()
            if contVar == 'y':
                searchKey = int(input('Enter a valid ID: '))
            else:
                break
        
        empOB = empDic[searchKey]
        return empOB
    except:
        if contVar != 'y':
            return 'abort'
        else:
            return 'fail'


class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title
    def set_name(self, name):
        self.__name = name
    def set_department(self, department):
        self.__department = department
    def set_job_title(self, job_title):
        self.__job_title = job_title
    def get_name(self):
        return self.__name
    def get_id_number(self):
        return self.__id_number
    def get_department(self):
        return self.__department
    def get_job_title(self):
        return self.__job_title
    def __str__(self):
        return f'{self.__name}, {self.__id_number}, {self.__department}, {self.__job_title}'
    
        
    
