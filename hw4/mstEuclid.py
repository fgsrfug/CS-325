#!/usr/bin/python3
"""
######################################################
Jesus Narvaez
CS 325 Homework 4
mstEuclid.py
February 5th, 2020
Description:
    mst.py reads in a file from the command line
    (or in this case the makefile), reads the points
    in the file, then finds a minimum spanning tree of
    the graph made up of the points in the file. Once
    computed, the results are printed to the terminal,
    with the edges taken and the total weight printed.
######################################################
"""

import sys
import math

"""
######################################################
Class name: edge
Description:
    Object used to fill the 2-D adjacency matrix (technically
    list). The edge class stores a weight and the vertex it
    connects to. The other vertex does not need to be tracked
    because that can be referenced by the row of the matrix.
######################################################
"""
class edge():
    #Intialize attributes to unreachable values
    def __init__(self):
        self.weight = -1
        self.toVertex = -1

    #Helper function to update values
    def updateData(self, weight, vertex):
        self.weight = weight
        self.toVertex = vertex

"""
######################################################
Function name: readFile
Description:
    Passing a file to read, this file reads the first line
    to see how many pairs to read. A while loop then iterates
    through the file and appends the ordered pairs into a
    list. That list and the number of vertices in the list
    are returned
######################################################
"""
def readFile(fileToRead):
    #Open the file for reading
    f = open(fileToRead, "r")

    #Get the number of vertices
    numVertices = f.readline()

    #Create a list to read the pairs
    readPairs = []

    #Iterate through file the number of vertices there are present
    i = 0
    while (i < int(numVertices)):

        #Add each pair to the list and split on spaces
        readPairs.append(f.read().splitlines())
        i += 1

    #Get the first element in this array, the rest are spaces
    orderedPairs = readPairs[0]

    #Return the ordered pairs and number of vertices
    return orderedPairs, numVertices

"""
######################################################
Function name: distanceBetweenPoints
Description:
    Given two points, the distance between them on the x-y
    plane is calculated and rounded to the nearest integer.
######################################################
"""
def distanceBetweenPoints(point1, point2):
    #Get x and y components of points, which are passed in as strings
    p1x, p1y = point1.split()
    p2x, p2y = point2.split()

    #Do the calculation and return the value
    distance = round(math.sqrt(((int(p2x) - int(p1x))**2) + ((int(p2y) - int(p1y))**2)))

    return distance

"""
######################################################
Function name: printAdjMatrix
Description:
    Helper function used to print out the attributes of the
    adjacency matrix.
######################################################
"""
def printAdjMatrix(matrix, numVertices):
    #Iterate through the entire matrix
    for i in range(numVertices):
        for j in range(numVertices - 1):
            #Print the current entry's attributes
            print("Vertex {0} to {1} with weight {2}".format(i, matrix[i][j].toVertex, matrix[i][j].weight))

"""
######################################################
Function name: createAdjMatrix
Description:
    Given the ordered pairs and the number of vertices, update
    each entry in the matrix with an edge object and values for
    the attributes.
######################################################
"""
def createAdjMatrix(numVertices, orderedPairs):
    #Create the matrix to hold everything
    adjMatrix = []

    #For each vertex, create a list to store each edge's info.
    for i in range(numVertices):
        vertexAdjList = []
        j = 0

        #Fill out each entry for the vertex
        while (j < (numVertices)):

            #But not itself
            if (i == j):
                j += 1

            #Otherwise calculate and update the edge attributes
            else:
                curEdge = edge()
                weight = distanceBetweenPoints(orderedPairs[i], orderedPairs[j])
                curEdge.updateData(weight, j)
                vertexAdjList.append(curEdge)
                j += 1

        #Append each vertex list to the final matrix and return it
        adjMatrix.append(vertexAdjList)

    return adjMatrix

"""
######################################################
Function name: findMinimum
Description:
    Finds the minimum value in a list (usually key for this scenario),
    given a set of indices to check from.
######################################################
"""
def findMinimum(listToSearch, indicesToCheck):
    #Initialize values to work with key
    minVal = 100000
    minIndex = 0

    #Go through the list
    for i in range(1, len(listToSearch)):
        #If the value is 100000, we skip over it
        if (listToSearch[i] == 100000):
            continue

        #Otherwise, check it is a valid index and smaller than
        #current minVal
        if (listToSearch[i] < minVal):
            for j in indicesToCheck:
                if i == j:
                    minVal = listToSearch[i]
                    minIndex = i
                else:
                    continue

    return minIndex

"""
######################################################
Function name: findMST
Description:
    Given the adjacency matrix and the number of vertices,
    findMST finds a minimum spanning tree using a method
    based off of Prim's algorithm.
######################################################
"""
def findMST(adjMatrix, numVertices):
    #Create the lists to use
    key = []
    verticesInMST = []
    verticesNotInMST = []
    changedWeightVer = []

    #Initalize key, with 0 for the first entry
    for i in range(numVertices):
        verticesNotInMST.append(i)
        if i == 0:
            key.append(0)
        else:
            key.append(100000)

    #Initialize the list used to keep track of which vertex
    #most recently changed the value in the key array, to -1
    for i in range(numVertices):
        changedWeightVer.append(-1)

    #Run until all vertices are in the MST
    while(len(verticesNotInMST) > 0):

        #Find vertex with lowest key value not in MST
        curVer = findMinimum(key, verticesNotInMST)
        for curEdge in adjMatrix[curVer]:

            #If the weight of the current edge to an adjacent vertex is less than the value in the key
            #array, and that adjacent vertex is not in the MST, update key and changedWeightVer
            if ((curEdge.toVertex in verticesNotInMST) and (curEdge.weight < key[curEdge.toVertex])):
                key[curEdge.toVertex] = curEdge.weight
                changedWeightVer[curEdge.toVertex] = curVer

        #Move curver from vertices not in MST to vertices in MST
        verticesNotInMST.remove(curVer)
        verticesInMST.append(curVer)

    #Return lists with weights and changes
    return key, changedWeightVer

"""
######################################################
Function name: printResults
Description:
    Given all the neccessary information, printResults...
    prints the final results of the MST to the terminal.
######################################################
"""
def printResults(numVertices, weights, vertices, orderedPairs):
    #Initialize totalWeight to 0
    totalWeight = 0

    #Print labels
    print("Edges in MST")
    print("Point (x, y)     Distance")

    #Print the connections and their weights
    for i in range(1, numVertices):
        p1x, p1y = orderedPairs[vertices[i]].split()
        p2x, p2y = orderedPairs[i].split()
        p2ylen = len(p2y)
        print("({0},{1}) - ({2},{3})".format(p1x, p1y, p2x, p2y), end='')
        print("       {0}".format(weights[i]))
        totalWeight += weights[i]

    #Print total distance
    print("     Total Distance {0}".format(totalWeight))

"""
######################################################
Function name: main
Description:
    Driver of the file. Reads in the file to read from the command
    line, has that file read, creates the adjacency matrix
    determines the MST and has the results printed.
######################################################
"""
if __name__ == '__main__':
    #Determine the file to read
    fileToRead = sys.argv[1]

    #Read the file
    orderedPairs, numVertices = readFile(fileToRead)
    numVertices = int(numVertices)

    #Create adjacency matrix and determine MST
    adjMatrix = createAdjMatrix(numVertices, orderedPairs)
    treeWeights, treeVertices = findMST(adjMatrix, numVertices)

    #Print results of MST
    printResults(numVertices, treeWeights, treeVertices, orderedPairs)

