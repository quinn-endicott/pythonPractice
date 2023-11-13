import pickle
class Employee:
    def __init__(self, name, idNumber):
        self.__name = name
        self.__idNumber = idNumber
    def setName(self, name):
        self.__name = name
    def setIdNumber(self, idNumber):
        self.__idNumber = idNumber
    def getName(self):
        return self.__name
    def getIdNumber(self):
        return self.__idNumber
    def __str__(self):
        return f'Employee {self.__idNumber}: {self.__name}'
    
class productionWorker(Employee):
    def __init__(self, name, idNumber, shiftNumber, payRate):
        Employee.__init__(self, name, idNumber)
        self.__shiftNumber = shiftNumber
        self.__payRate = payRate
    def setShift(self, shiftNumber):
        self.__shiftNumber = shiftNumber
    def setPay(self, payRate):
        self.__payRate = payRate
    def getShift(self):
        return self.__shiftNumber
    def getPay(self):
        return f'{self.__payRate:.2f}'
    def __str__(self):
        return f'Employee {self._Employee__idNumber}: {self._Employee__name}\nShift: \
{self.__shiftNumber}\nPayrate: ${self.__payRate:.2f}'
    

    
class shiftSupervisor(Employee):
    def __init__(self, name, idNumber, salary, bonus):
        Employee.__init__(self, name, idNumber)
        self.__salary = salary
        self.__bonus = bonus
    def setSalary(self, salary):
        self.__salary = salary
    def setBonus(self, bonus):
        self.__bonus = bonus
    def getSalary(self):
        return f'{self.__salary:.2f}'
    def getBonus(self):
        return f'{self.__bonus:.2f}'
    def __str__(self):
        return f'Employee {self._Employee__idNumber}: {self._Employee__name}\nSalary: ${self.__salary:.2f}\nBonus: ${self.__bonus:.2f}'
    

def loadEmpDic(dirFile):
    
    #try to open the file in read binary mode
    try:
        with open(dirFile, 'rb') as empFile:
            #unpickle dictionary and assign to empOut
            empOut = pickle.load(empFile)
    #if file fails to open
    except:
        #empOut is an empty dictionary
        empOut = {}
    #return empOut
    return empOut

def saveDic(empDic, dirFile):
    #open the file, write mode so new file supercedes old
    with open(dirFile, 'wb') as savFile:
        #pickle dictionary, save to file
        pickle.dump(empDic, savFile)

def printOptions():
    print('Options: ')
    print("Enter '1' to add a new production worker")
    print("Enter '2' to add a new shift supervisor")
    print("Enter '3' to look up an employee")
    print("Enter '4' to delete an employee")
    
    print()

def makeProd(empDir):
    corVar = 'n'
    while corVar != 'y':
        empName = input('Enter the name of the employee: ')
        empID = int(input('Enter the employee ID number: '))
        while empID in empDir:
            empID = int(input('Employee ID must be unique, try again: '))

        empShift = int(input('Enter the employee shift number: '))
        while empShift < 1 or empShift > 3:
            empShift = int(input('There are three shifts, try again: '))
        empPay = float(input('Enter the employee pay rate: '))
        prodOb = productionWorker(empName, empID, empShift, empPay)
        print('Your entry: ')
        print(prodOb)
        print()
        corVar = input('Is this information correct (y/n)?').lower()
    empDir[empID] = prodOb
    print('You added a new production worker: ')
    print(prodOb)
    print()

def makeSup(empDir):
    corVar = 'n'
    while corVar != 'y':
        empName = input('Enter the name of the employee: ')
        empID = int(input('Enter the employee ID number: '))
        while empID in empDir:
            empID = int(input('Employee ID must be unique, try again: '))

        empSal = float(input('Enter the employee salary: '))
        
        empBonus = float(input('Enter the employee bonus: '))
        supOb = shiftSupervisor(empName, empID, empSal, empBonus)
        print('Your entry: ')
        print(supOb)
        corVar = input('Is this information correct (y/n)?').lower()
        print()
    empDir[empID] = supOb
    print('You added a new shift supervisor: ')
    print(supOb)
    print()

def findEmp(empDir):
    searchKey = int(input('Enter the ID of the employee you want to look up: '))
    if searchKey not in empDir:
        print('Employee not found')
        print()
    else:
        foundEmp = empDir[searchKey]
        print('Your results: ')
        if isinstance(foundEmp, productionWorker):
            print('Employee type: Production Worker')
        elif isinstance(foundEmp, shiftSupervisor):
            print('Employee type: Shift Supervisor')
        print(foundEmp)
        print()

def deleteEmp(empDir):
    #input the key of the value to delete
    delKey = int(input('Enter the ID of the employee to delete: '))
    #while the key provided is not in the dictionary
    while delKey not in empDir:
        delKey = int(input('Employee ID must exist, try again: '))
    delOb = empDir[delKey]
    delVar = 'n'
    print('Employee to delete: ')
    print(delOb)
    print()
    delVar = input('Are you sure you want to delete the employee (y/n)?').lower()
    if delVar == 'y':
    #pop object from dictionary by key, assign to variable
        empDir.pop(delKey)
        print("Employee deleted")
        print()
    
    