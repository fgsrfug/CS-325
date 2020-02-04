#!/usr/bin/python3
############################################
# Jesus Narvaez
# CS 325 Homework 3
# knapsack.py
# February 3rd, 2020
# This file determines the largest value that
# can be placed into a knapsack of weight W.
# There is a recursive solution and a dynamic
# solution. Both are timed and compared.
############################################

#Import modules for use
from random import randint
from random import seed
import time

############################################
# Function name: randomizeArray
# Description: Given an array, it's size,
#   and the max allowable random integer, the
#   array is filled with random values
############################################
def randomizeArray(array, sizeOfArray, maxRandInt):
    for i in range(0, sizeOfArray):
        array.append(randint(0,maxRandInt))

############################################
# Function name: recursive
# Description: Given value and weight arrays,
#   the size of the arrays and max weight,
#   a max value is determined. This method
#   uses recursion to find a solution.
############################################
def recursive(val, weight, n, W):
    #Check if we're out of items or if there
    #is no room in the knapsack
    if (n < 0 or W == 0):
        return 0

    #If the current item weight exceeds max
    #weight, move on to the next item
    if (weight[n] > W):
        return recursive(val, weight, n - 1, W)
    #Else, check if it's best to put the item in
    #the knapsack or proceed without it
    else:
        maxValue = max(val[n] + recursive(val, weight, n - 1, W - weight[n]), recursive(val, weight, n - 1, W))
        return maxValue

def dynamic(val, weight, n, W):
    #table = [[0] * n] * n
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]

    print(table)
############################################
# Function name: main
# Description: The driver of this file.
#   The number of elements, max weight, max
#   random integer is set, and the val and
#   weight arrays are created. recursive() and
#   dynamic() are timed and printed to stdout.
############################################
if __name__ == '__main__':
    #Set the number of items and max weight here!
    n = 5
    W = 15

    #Set max random integer
    maxRandInt = 10

    #Seed random number generator
    seed()

    #Create and fill arrays with random values
    val = []
    weight = []
    randomizeArray(val, n, maxRandInt)
    randomizeArray(weight, n, maxRandInt)
    #print("Value: {0}, Weight: {1}".format(val, weight))

    #Time the recursive function
    startTime = time.process_time()
    recResult = recursive(val, weight, n - 1, W)
    totalTime = time.process_time() - startTime

    dynResult = dynamic(val, weight, n, W)

    print("n = {0}, W = {1}, Rec time = {2}, Max Rec = {3}".format(n, W, round(totalTime, 4), recResult))


