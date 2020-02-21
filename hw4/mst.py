#!/usr/bin/python3
############################################
# Jesus Narvaez
# CS 325 Homework 3
# shopping.py
# February 5th, 2020
# This file essentially solves the knapsack
#   problem for n people in a family, while
#   keeping track of what items they grabbed.
#   This file reads inputs from "shopping.txt"
#   and writes the out to "results.txt"
############################################

import sys
import math

############################################
# Function name: dynamic
# Description: Given value and weight arrays,
#   the size of the arrays and max weight,
#   a max value is determined. This method
#   uses dynamic programming to find a solution.
#   This method is altered to also keep track
#   of which values are used in solution.
#   Returns a list of the max value and the
#   items in the solution.
#   The item tracking portion was modeled off
#   of the GeeksforGeeks algorithm for printing
#   out items in knapsack problem, with adjustments
#   to solve this particular problem. Their page
#   can be found here:
#   https://www.geeksforgeeks.org/printing-items-01-knapsack/
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

    #Save result to total variable
    total = table[n][W]

    #Create list for when function returns and
    #append the total to the start
    returnList = []
    returnList.append(total)

    #Create a list to hold the items used
    totalItemsList = []

    #Iterate through the table to find items used
    w = W
    for i in range(n, 0, -1):

        #Create list to hold items
        itemsList = []

        #If total is <= 0, no items were used
        if total <= 0:
            break

        #If we find total, that item column corresponds
        #to the item used
        if total == table[i - 1][w]:
            continue

        #So add the item number and reduce the value and weight totals
        else:
            itemsList.append(i)
            total = total - val[i - 1]
            w = w - weight[i - 1]

        #Add the entire list to the original list
        totalItemsList.append(itemsList)

    #Append items list to returnList and return
    returnList.append(totalItemsList)
    return returnList

############################################
# Function name: writeFile
# Description: Called within main to write
#   the results of a test case to a file called
#   "results.txt". It's passed in a list of
#   all the results and the case number.
############################################
def writeFile(listToWrite, caseNum):
    #Determine how many people to account for
    numPeople = len(listToWrite)

    #Open file for writing and write the case number
    f = open("results.txt", "a")
    f.write("Test Case {0}\n".format(caseNum + 1))

    #Add the first value of each list in listToWrite
    #to get total value and write it to file
    value = 0
    for i in range(numPeople):
        value += listToWrite[i][0]

    f.write("Total Price {0}\n".format(value))

    #Write "Member Items as well the item numbers
    f.write("Member Items\n")

    #For each family memeber
    for i in range(numPeople):
        #Write the member numer
        f.write("{0}: ".format((i + 1)))

        #And write each item number in the list
        for j in range(len(listToWrite[i][1])):
            f.write("{0} ".format((listToWrite[i][1][j][0])))

        f.write("\n")

    #Close the file
    f.close()

############################################
# Function name: shopping
# Description: Called by main to find the max
#   value each family member can carry. Calls
#   dynamic (from knapsack problem) to find
#   max each family member can carry. Returns
#   total of list of family totals and items.
############################################
def shopping(itemsPrice, itemsWeight, maxWeights):

    #Get number of people and items
    numPeople = len(maxWeights)
    numItems = len(itemsPrice)

    #For each person, call dynamic and append result to peopleTotals
    peopleTotals = []
    for i in range(numPeople):
        peopleTotals.append(dynamic(itemsPrice, itemsWeight, numItems, maxWeights[i]))

    #Return list with totals of every case
    return peopleTotals

class edge():
    def __init__(self):
        self.weight = 0
        self.toVertex = -1

    def updateData(self, weight, vertex):
        self.weight = weight
        self.toVertex = vertex

############################################
# Function name: readFile
# Description: Called within main to read
#   input file called "shopping.txt". Sorts
#   each of the values into the appropriate
#   list and then returns all the lists.
############################################
def readFile(fileToRead):

    #Open shopping.txt for reading
    f = open(fileToRead, "r")

    #Get the number of cases
    numVertices = f.readline()

    #Create arrays to hold all data from file
    readPairs = []

    #Iterate through file the number of cases there are present
    i = 0
    while (i < int(numVertices)):

        #Create lists that will case data
        readPairs.append(f.read().splitlines())
        i += 1

    orderedPairs = readPairs[0]
    print(orderedPairs)
    #Return all the lists
    return orderedPairs, numVertices

def distanceBetweenPoints(point1, point2):

    #print("Point 1: {0}, Point 2: {1}".format(point1, point2))
    p1x, p1y = point1.split()
    p2x, p2y = point2.split()
#    print("p1x: {}".format(p1x))
#    print("p1y: {}".format(p1y))
#    print("p2x: {}".format(p2x))
#    print("p2y: {}".format(p2y))

    distance = round(math.sqrt(((int(p2x) - int(p1x))**2) + ((int(p2y) - int(p1y))**2)))
    #print(distance)

    return distance

def printAdjMatrix(matrix, numVertices):
    i = 0
    for i in range(numVertices):
        #curList = matrix[i][0]
        j = 0
        for j in range(numVertices - 1):
            #curEdge = edge()
            #curEdge = curList[j]
            #print(curEdge.weight)
            print("Vertex {0} to {1} with weight {2}".format(i, matrix[i][j].toVertex, matrix[i][j].weight))

def createAdjMatrix(numVertices):
    i = 0
    adjMatrix = []
    for i in range(numVertices):
        vertexAdjList = []
        j = 0
        while (j < (numVertices)):
            if (i == j):
                j += 1
            else:
                curEdge = edge()
                weight = distanceBetweenPoints(orderedPairs[i], orderedPairs[j])
                curEdge.updateData(weight, j)
                #print("From {0} to {1} with weight {2}".format(i, curEdge.toVertex, curEdge.weight))
                vertexAdjList.append(curEdge)
                #print(vertexAdjList)
                j += 1

        adjMatrix.append(vertexAdjList)

    return adjMatrix

def findMinimum(listToSearch, indicesToCheck):

    minVal = 100000
    minIndex = 0
    for i in range(1, len(listToSearch)):
        if (listToSearch[i] == 100000):
            continue
        if (listToSearch[i] < minVal):
            for j in indicesToCheck:
                if i == j:
                    minVal = listToSearch[i]
                    minIndex = i
                else:
                    continue

    print("minVal and Index: {0}, {1}".format(minVal, minIndex))

    return minIndex

def findMST(adjMatrix, numVertices):
    i = 0
    key = []
    verticesInMST = []
    verticesNotInMST = []
    for i in range(numVertices):
        verticesNotInMST.append(i)
        if i == 0:
            key.append(0)
        else:
            key.append(100000)

    changedWeightVer = []
    for i in range(numVertices):
        changedWeightVer.append(-1)
    print(key)
    print(verticesInMST)
    print(verticesNotInMST)


    while(len(verticesNotInMST) > 0):

        #Find vertex with lowest key value
        curVer = findMinimum(key, verticesNotInMST)
        print("curVer: {}".format(curVer))

        for curEdge in adjMatrix[curVer]:

            print("adjv weight: {0}, and other vertex: {1}".format(curEdge.weight, curEdge.toVertex))

            print("keyval at curEdge: {}".format(key[curEdge.toVertex]))
            if ((curEdge.toVertex in verticesNotInMST) and (curEdge.weight < key[curEdge.toVertex])):
                print("ADJUSTING KEY VALUE")
                key[curEdge.toVertex] = curEdge.weight
                changedWeightVer[curEdge.toVertex] = curVer

        if((curVer in verticesNotInMST) and (curVer not in verticesInMST)):
            verticesNotInMST.remove(curVer)
            verticesInMST.append(curVer)

        print("Not in MST: {}".format(verticesNotInMST))
        print("In MST: {}".format(verticesInMST))
        print("CWV: {}".format(changedWeightVer))
        print("key: {}\n".format(key))

############################################
# Function name: main
# Description: The driver of this file.
#   The number of elements, max weight, max
#   random integer is set, and the val and
#   weight arrays are created. recursive() and
#   dynamic() are timed and printed to stdout.
############################################
if __name__ == '__main__':

    fileToRead = sys.argv[1]
    orderedPairs, numVertices = readFile(fileToRead)

    numVertices = int(numVertices)

    adjMatrix = createAdjMatrix(numVertices)
    #printAdjMatrix(adjMatrix, numVertices)
    findMST(adjMatrix, numVertices)

    #numbers = [2, 4, -100, 3232, 69, 1]
    #findMinimum(numbers)
"""
    #Initialize lists to hold input data
    itemsPrice = []
    itemsWeight = []
    maxWeights = []
    caseDetails = []

    #Get input data from file
    itemsPrice, itemsWeight, maxWeights, caseDetails = readFile()

    #Get the number of cases  in file
    numCases = len(caseDetails)

    #For each case, call shopping and print results to file
    for i in range(numCases):
        results = shopping(itemsPrice[i], itemsWeight[i], maxWeights[i])
        writeFile(results, i)
"""
