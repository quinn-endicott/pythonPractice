import pickle

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

    while menuChoice < 1 or menuChoice > 5
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
    
