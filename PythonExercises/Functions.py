def returnStuff(num, bool):
    if num > 5 and bool == True:
        return 2
    if num <= 5 and (bool == True or bool == False):
        return 1
    if num > 5 and bool == False:
        return 3
    
def getSkibonacci(n):
    if n <= 2:
        return 1
    else:
        return 2*getSkibonacci(n-2) + getSkibonacci(n-3)
    