#!/usr/bin/env python3
import sys
import random

# Merging Exercise Task 1: Easy
def compressingWeightedMatrices(matrix, K, minSignificance = 0.4, maxSignificance = 1):
    # Task 1: On one partner's computer
        # 1) Form a kernel (sub-matrix) of size K x K
        # 2) Compute average weights in the kernel
        # 3) Move kernel from left to right, if the kernel reaches the end matrix in the x-direction, move it down to the next row
        # 4) Return a compressed matrix with just kernel averages
        # Note: Kernel's must not overlap

    # Task 2: On another partner's computer
        # - Build off of the solution you created in Task 1
        # - This time, imagine our robot is standing in the bottom right-hand corner of the matrix. This means that the top left-hand kernel of the matrix is the farthest kernels from the robot
        # - To each kernel's average which you computed, multiply it by a graduated, uniform significant percentage
        # - The farthest kernels should be multiplied by the minSignificance and the closest kernel (bottom right-hand corner kernel) should be multiplied by the maxSignificance. Every kernel
        # in between is multiplied by a significance on a uniform distribution between minSignificance and maxSignificance

    pass

# Merging Exercise Task 2: Med
def shortestPathToDestination(matrix, startingPosition, destination):
    # Yet to come...
    pass


def generateRandomizedMatrix():
    rows = random.randint(5, 10)
    cols = random.randint(5, 10)
    matrix = [[random.random() for _ in range(cols)] for _ in range(rows)]
    return matrix

if __name__ == '__main__':
    matrix = generateRandomizedMatrix()
    K = random.randint(1,3)
    compressingWeightedMatrices(matrix, K)