#the largerThan function will evaluate the numbers in numList for being > user 
#value n
def largerThan(numList, usrN):
    #list to store larger numbers
    largeList = []
    #for each numberin the numList
    for num in numList:
        #is num > than user n value
        if num > usrN:
            #if it is, append to large numbers list
            largeList.append(num)
    #return filled larger list to main
    return largeList

#my main function will prompt user for their n value and the values for the list
def main():
    #opening screen to explain what user is doing
    print('This program will evaluate which numbers you entered are greater than n.')
    #user enters the value n
    usrLimit = float(input('Enter your value for n: '))
    #continue variable for while loop, set to y
    contVar = 'y'
    #empty list for user values
    usrList = []
    #explain step to user
    print('Please create a list of numbers.')
    #while user enters y for continue
    while contVar == 'y':
        #take input for iteration
        listVal = float(input('Add a value to the list: '))
        #add value to list
        usrList.append(listVal)
        #keep entering numbers?
        contVar = input('Would you like to add another value (y/n): ').lower()
    #largerThan for usrList and usrLimit
    returnList = largerThan(usrList, usrLimit)
    #print the number list too 
    print(f'Your numbers are: {usrList}')
    #print list of grater values
    print(f'The values greater than {usrLimit} are: {returnList}')

main()
    
    