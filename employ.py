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
        return self.__payRate
    def __str__(self):
        return f'Employee {self._Employee__idNumber}: {self._Employee__name}\nShift: {self.__shiftNumber}\nPayrate: {self.__payRate}'
    
class shiftSupervisor:
    def __init__(self, name, idNumber, salary, bonus):
        Employee.__init__(self, name, idNumber)
        self.__salary = salary
        self.__bonus = bonus
    def setSalary(self, salary):
        self.__salary = salary
    def setBonus(self, bonus):
        self.__bonus = bonus
    def getSalary(self):
        return self.__salary
    def getBonus(self):
        return self.__bonus
    def __str__(self):
        return f'Employee {self._Employee__idNumber}:\
              {self._Employee__name}\nSalary: {self.__salary}\nBonus: {self.__bonus}'
    
