#################################
# Jesus Narvaez
# Makefile for CS 325 Homework 4
# February 18th, 2020
# Executes both knapsack.py and
# shopping.py
#################################

PYTHON = python3
CXX = g++

SRC_1 = mst.py
SRC_2 = insertsort.cpp

OBJ_1 = ${SRC_1:.cpp=.o}
#TXT_1 = graph.txt
TXT_1 = graph2.txt

mst:
	clear
	${PYTHON} ${SRC_1} ${TXT_1}

insert:
	${CXX} ${SRC_2} -o ${OBJ_1}

clean:
	rm -f *.o

all: mst
