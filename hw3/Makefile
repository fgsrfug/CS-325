#################################
# Jesus Narvaez
# Makefile for CS 325 Homework 3
# February 4th, 2020
# Executes both knapsack.py and
# shopping.py
#################################

PYTHON = python3

SRC_1 = knapsack.py
SRC_2 = shopping.py

knapsack:
	clear
	${PYTHON} ${SRC_1}

shopping:
	clear
	rm -f results.txt
	${PYTHON} ${SRC_2}

all: knapsack shopping
