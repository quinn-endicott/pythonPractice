import pickle

def printCurrent(curOB):
    print(curOB.__str__())

#the deleteEmp function will pop the employee object out of the dictionary by the 
#key the user enters
def deleteEmp(empDic):
    #input the key of the value to delete
    delKey = int(input('Enter the ID of the employee to delete: '))
    #while the key provided is not in the dictionary
    while delKey not in empDic:
        #if there are no items in the dictionary
        if len(empDic) == 0:
            #return 'no result'
            return None
            #break loop
            break
        else:
            #prompt for a valid key to delete
            delKey = int(input('Employee ID must exist, try again: '))
    #pop object from dictionary by key, assign to variable
    popOB = empDic.pop(delKey)
    #return object that was removed
    return popOB



    

def saveDic(empDic, FILE):
    with open(FILE, 'wb') as savFile:
        pickle.dump(empDic, savFile)




#changeEmp is a function that allows the user to replace the name, department, and
#job_title values in a selected employee onject
def changeEmp(empDic):
    #enter the key for the employee to modify
    chKey = int(input('Enter the ID of the employee you want to modify: '))
    #while the entered key is not in the dictionary
    while chKey not in empDic:
        # if there is nothing in the dictionary
        if len(empDic) == 0:
            #return 'no result'
            return None
            #break out of loop
            break
        #else the search term is not one of the present values
        else:
            #does user want to search again?
            contVar = input('Employee not found, search again (y/n)?').lower()
            #if user wants to continue
            if contVar == 'y':
                #enter a valid id
                chKey = int(input('Enter employee ID: '))
            #if user did not choose to continue
            else:
                #return 'abort'
                return None
                #break loop
                break
    #assign object at chKey to emOB            
    emOB = empDic[chKey]
    #context
    print('Current employee information: ')
    #print current state of emOB
    printCurrent(emOB)
    print()
    #do you want to change the name?
    nVar = input("Change the employee's name (y/n)?").lower()
    #if nVar is yes
    if nVar == 'y':
        #enter new name
        nName = input('Enter new name: ')
        #call set_name method for emOB
        emOB.set_name(nName)
    #do you want to change department, works like above
    dVar = input("Change the employee's department (y/n)?").lower()
    if dVar == 'y':
        nDep = input('Enter the new department: ')
        #uses set_department method
        emOB.set_department(nDep)
    #do you want to change job_title, works like above
    tVar = input("Change the employee's job title (y/n)?").lower()
    if tVar == 'y':
        nTit = input('Enter the new job title: ')
        #uses set_job_title method
        emOB.set_job_title(nTit)
    # return employee object
    return emOB















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
    newEmp = Employee(empName, empInt, empDepartment, empTitle)
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
    print()
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
            contVar = input('Invalid input, would you like to try again(y/n): ').lower()
            if contVar == 'y':
                searchKey = int(input('Enter a valid ID: '))
            else:
                break
        
        empOB = empDic[searchKey]
        return empOB
    except:
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
    
        
    
