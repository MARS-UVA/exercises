#Task 1
def returnStuff(num, bool):
    if num > 5 and bool == True:
        return 2
    if num <= 5 and (bool == True or bool == False):
        return 1
    if num > 5 and bool == False:
        return 3
    
#Task 3
def getSkibonacci(n):
    if n <= 2:
        return 1
    else:
        return 2*getSkibonacci(n-2) + getSkibonacci(n-3)

#Task 5
def parseMessageArray(msgArr):
    #Your code goes here
    pass

#Task 5
def countAllPossiblePaths(grid):
    #Your code goes here
    pass
#Task 6
def consolidateDuplicateEntries():
    #Your code goes here
    pass

#Task 7
def replaceAllReferences():
    #Your code goes here
    pass


