#!/usr/bin/env python3
import sys
import random
import numpy as np
import pandas as pd
import json
from BinMessage import generateByteString

# Task 1 - Easy
def returnStuff(regolith, construction):
    return [1,[2,3][construction]][regolith>5]

# Task 2 - Easy
def celsiusToFahr(cel):
    return int(round(cel*1.8+32))

# Task 3 - Easy
def getSkibonacci(n):
    arr = [1,1,1]
    while len(arr)<n:
        arr.append(2*arr[-2]+arr[-3])
    return arr[n]

# Task 4 - Easy
def weatherDataParser():
    weatherArr = pd.read_csv("/../resources/weather_long.csv")
    res = weatherArr.pivot(index=['City','Month'],columns='Type', values='Value')
    res.to_csv("weather_wide.csv",index=True)

# Task 5 - Easy
def parseMessageArray(msgArr):
    # You code goes here
    pass

# Task 6 - Easy/Med
def countAllPossiblePaths(grid):
    cts = [[0 for j in grid[i]]for i in range(len(grid))]
    countHelper(grid,0,0,cts)
    print(cts)
    return cts[len(grid)-1][len(grid[0])-1]

def countHelper(grid,i,j,cts):
    m,n = len(grid)-1,len(grid[0])-1
    if(i>m or j>n or not grid[i][j]): return
    if i==0 and j==0: cts[i][j]=1
    elif i==0: cts[i][j] = cts[i][j-1]
    elif j==0: cts[i][j] = cts[i-1][j]
    else: cts[i][j] = cts[i-1][j]+cts[i][j-1]
    countHelper(grid,i+1,j,cts)
    countHelper(grid,i,j+1,cts)

# Task 7 - Easy/Med
def consolidateDuplicateEntries():
    file = open('events.json')
    dct = json.load(file)
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



