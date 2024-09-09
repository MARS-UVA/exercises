def getSkibonacci(n):
    if n <= 2:
        return 1
    else:
        return 2*getSkibonacci(n-2) + getSkibonacci(n-3)