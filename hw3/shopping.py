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
# Function name: readFile
# Description: Called within main to read
#   input file called "shopping.txt". Sorts
#   each of the values into the appropriate
#   list and then returns all the lists.
############################################
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

        #Read and place item price and weight in
        #appropriate list
        for j in range(int(numItems)):
            itemLine = f.readline().split()
            casePrices.append(int(itemLine[0]))
            caseWeight.append(int(itemLine[1]))

        #Determine the number of people and add to caseValues
        numPeople = f.readline()
        caseValues.append(int(numPeople))

        #Read the max weight for each person and put
        #into list
        for k in range(int(numPeople)):
            itemLine = f.readline()
            casePeopleWeight.append(int(itemLine))

        #Append each case list to the total list
        itemPrice.append(casePrices)
        itemWeight.append(caseWeight)
        peopleMaxWeight.append(casePeopleWeight)
        casesList.append(caseValues)

        #Increment the case counter
        i = i + 1

    #Return all the lists
    return itemPrice, itemWeight, peopleMaxWeight, casesList

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

############################################
# Function name: main
# Description: The driver of this file.
#   The number of elements, max weight, max
#   random integer is set, and the val and
#   weight arrays are created. recursive() and
#   dynamic() are timed and printed to stdout.
############################################
if __name__ == '__main__':

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

