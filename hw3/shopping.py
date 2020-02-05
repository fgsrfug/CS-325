#!/usr/bin/python3
############################################
# Jesus Narvaez
# CS 325 Homework 3
# shopping.py
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

############################################
# Function name: recursive
# Description: Given value and weight arrays,
#   the size of the arrays and max weight,
#   a max value is determined. This method
#   uses dynamic programming to find a solution.
############################################
def dynamic(val, weight, n, W):
    #Create and initialize the table
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]

    #Iterate through the entire table
    for i in range(n + 1):
        for w in range(W + 1):

            #If in the first row or column of the table
            #set it to 0. It is not used
            if i == 0 or w == 0:
                table[i][w] = 0

            #If the item can be fit in the knapsack,
            #Check if it's better to include it or not
            elif weight[i - 1] <= w:
                table[i][w] = max(val[i - 1] + table[i - 1][w - weight[i - 1]], table[i - 1][w])

            #The item doesn't fit, so don't include it
            else:
                table[i][w] = table[i - 1][w]

    return table[n][W]

def readFile():

    #Open shopping.txt for reading
    f = open("shopping.txt", "r")

    #Get the number of cases
    numCases = f.readline()

    #Create arrays to hold all data from file
    itemPrice = []
    itemWeight = []
    peopleMaxWeight = []
    casesList = []

    #Iterate through file the number of cases there are present
    i = 0
    while (i < int(numCases)):

        #Create lists that will case data
        caseValues = []
        casePrices = []
        caseWeight = []
        casePeopleWeight = []

        #Determine the number of items and add to caseValues
        numItems = f.readline()
        caseValues.append(int(numItems))
        #print("numItems: {0}".format(int(numItems)))

        #Read and place item price and weight in
        #appropriate list
        for j in range(int(numItems)):
            itemLine = f.readline().split()
            casePrices.append(int(itemLine[0]))
            caseWeight.append(int(itemLine[1]))

        #print("casePrices: {0}".format(casePrices))
        #print("caseWeight: {0}".format(caseWeight))

        #Determine the number of people and add to caseValues
        numPeople = f.readline()
        caseValues.append(int(numPeople))
        #print("numPeople: {0}".format(int(numPeople)))

        #Read the max weight for each person and put
        #into list
        for k in range(int(numPeople)):
            itemLine = f.readline()
            casePeopleWeight.append(int(itemLine))

        #print("casePeopleWeight: {0}".format(casePeopleWeight))
        #print("caseValues: {0}".format(caseValues))

        #Append each case list to the total list
        itemPrice.append(casePrices)
        itemWeight.append(caseWeight)
        peopleMaxWeight.append(casePeopleWeight)
        casesList.append(caseValues)

        #Increment the case counter
        i = i + 1

#    print("casesList: {0}".format(casesList))
#    print("itemPrice: {0}".format(itemPrice))
#    print("itemWeight: {0}".format(itemWeight))
#    print("peopleMaxWeight: {0}".format(peopleMaxWeight))

    #Return all the lists
    return itemPrice, itemWeight, peopleMaxWeight, casesList

#    print("numCases: {0}".format(numCases))
#    line = f.readlines()
#    for i in line:
#        if i == 1:
#            print("i is zero. Also value is: {0}".format(i))
#        print(i)

def shopping(itemsPrice, itemsWeight, maxWeights):
    print("IN SHOPPING FUNCTION\n")
    print("itemsPrice: {0}".format(itemsPrice))
    print("itemsWeight: {0}".format(itemsWeight))
    print("maxWeights: {0}".format(maxWeights))

    densities = []
    numPeople = len(maxWeights)
    numItems = len(itemsPrice)

    for i in range():
        densities.append(round((itemsPrice[i] / itemsWeight[i]), 2))

    print("Densities: {0}".format(densities))
    print("numPeople: {0}".format(numPeople))

    peopleItems = []
    peopleValues = []

    for i in range(numPeople):
        personItems = []
        personValues = []
        personWeights = []
        densitiesCarried = [0]
        #Go through each item
        for j in range(numItems):
            #Check if it can be carried
            if maxWeights[i] >= itemsWeight[j]:
                #Check if it is worth carrying over current
                #payload
                if densities[i] > sum(densitiesCarried):
                    personItems.append(j + 1)
                    personValues.append(itemsPrice[j])



############################################
# Function name: main
# Description: The driver of this file.
#   The number of elements, max weight, max
#   random integer is set, and the val and
#   weight arrays are created. recursive() and
#   dynamic() are timed and printed to stdout.
############################################
if __name__ == '__main__':

    itemsPrice = []
    itemsWeight = []
    maxWeights = []
    caseDetails = []
    itemsPrice, itemsWeight, maxWeights, caseDetails = readFile()

    print("caseDetails: {0}".format(caseDetails))
    print("itemsPrice: {0}".format(itemsPrice))
    print("itemsWeight: {0}".format(itemsWeight))
    print("maxWeights: {0}".format(maxWeights))

    shopping(itemsPrice[0], itemsWeight[0], maxWeights[0])

    #Set the number of items and max weight here!
    n = 25
    W = 10

    #Set max random integer
    maxRandInt = 10

    #Seed random number generator
    seed()

    #Create and fill arrays with random values
    val = []
    weight = []
    randomizeArray(val, n, maxRandInt)
    randomizeArray(weight, n, maxRandInt)

    #Time the recursive function
    recStartTime = time.process_time()
    recResult = recursive(val, weight, n - 1, W)
    recTime = time.process_time() - recStartTime

    #Time the dynamic function
    dpStartTime = time.process_time()
    dynResult = dynamic(val, weight, n, W)
    dpTime = time.process_time() - dpStartTime

    #print("\nn = {0}, W = {1}, DP time = {2}, Rec time = {3}, Max DP = {4}, Max Rec = {5}\n".format(n, W, round(dpTime, 4), round(recTime, 4), dynResult, recResult))


