#!/usr/bin/env python3
import sys
import random
import csv
from turtle import pd 
from BinMessage import generateByteString

# Task 1 - Easy
#Hello
def returnStuff(num, boolean):
    if num > 5:
        if boolean == True:
           return 2
        else:
           return 3
    if num <= 5:
        return 1

# Task 2 - Easy
def celsiusToFahr(cel):
    return int(cel * 1.8 + 32)

# Task 3 - Easy
def getSkibonacci(n):
    f = [1, 1]
    for i in range(2, n):
       f.append(2 * f[i - 2] + f[i - 3])
    return f[n - 1]

# Task 4 - Easy
def weatherDataParser():
    with open('weather_long.csv') as x:
        reader = csv.reader(x)
        df = pd.DataFrame(reader, columns=['City', 'Month', 'Type', 'Value'])
    pass

# Task 5 - Easy
def parseMessageArray(msgArr):
    
    pass

# Task 6 - Easy/Med
def countAllPossiblePaths(grid):
    # You code goes here
    pass

# Task 7 - Easy/Med
def consolidateDuplicateEntries():
    # Your code goes here
    pass

# Task 8 - Easy/Med
def checkCurrentAndVoltages():
    # Your code goes here
    pass

# Task 9 - Regex Parser - Easy/Med
def parseWithRegEx():
    # Your code goes here
    pass

# ------------------------------- Runner Code, do not implement below this --------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
def getRandomizedGrid(min_size=3, max_size=10, zero_ratio=0.2):
    rows = random.randint(min_size, max_size)
    cols = random.randint(min_size, max_size)

    grid = [[1 for _ in range(cols)] for _ in range(rows)]

    total_cells = rows * cols
    num_zeros = int(total_cells * zero_ratio)

    flat_grid = [1] * total_cells
    zero_positions = random.sample(range(total_cells), num_zeros)

    for pos in zero_positions:
        flat_grid[pos] = 0

    grid = [flat_grid[i * cols:(i + 1) * cols] for i in range(rows)]
    return grid

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception("Must pass the task number to run")

    functions = [returnStuff, celsiusToFahr, getSkibonacci, weatherDataParser, parseMessageArray, countAllPossiblePaths, consolidateDuplicateEntries, checkCurrentAndVoltages]

    taskNo = int(sys.argv[1])  # Read the task number
    if taskNo > len(functions):
        raise Exception(f"The task number {taskNo} is not associated with a task yet")
    if taskNo == 1 and len(sys.argv) == 4:
        try:
            num = int(sys.argv[2])
            boolean = sys.argv[3].lower() == "true"
            returnValue = functions[taskNo - 1](num, boolean)
            print("Task 1 output: ", returnValue)
        except:
            raise Exception("For Task 1, pass an integer for 'num' and 'true/false' for boolean")
    elif taskNo == 2 and len(sys.argv) == 3:
        try:
            cel = float(sys.argv[2])
            returnValue = functions[taskNo - 1](cel)
            print("Task 2 output: ", returnValue)
        except:
            raise Exception("For Task 2, pass a number for 'cel'")
    elif taskNo == 3 and len(sys.argv) == 3:
        try:
            n = int(sys.argv[2])
            returnValue = functions[taskNo - 1](n)
            print("Task 3 output: ", returnValue)
        except:
            raise Exception("For Task 3, pass an integer for 'n'")
    elif taskNo == 4 and len(sys.argv) == 3:
        try:
            msgArr = sys.argv[2].split(',')
            returnValue = functions[taskNo - 1](msgArr)
            print("Task 4 output: ", returnValue)
        except:
            raise Exception("For Task 4, pass a comma-separated string for 'msgArr'")
    elif taskNo == 5:
        generateByteString()
        file_path = "../robot_data.bin"
        with open(file_path, 'rb') as file:
            binary_data = file.read()
        returnValue = functions[taskNo - 1](binary_data)
        print("Task 5 output: ", returnValue)
    elif taskNo == 6:
        grid = getRandomizedGrid()
        returnValue = functions[taskNo - 1](grid)
        print("Task 6 output: ", returnValue)
    elif taskNo == 7:
        returnValue = functions[taskNo - 1]()
        print("Task 7 output: ", returnValue)
    elif taskNo == 8:
        returnValue = functions[taskNo - 1]()
        print("Task 8 output: ", returnValue)



