#################################
# Jesus Narvaez
# Makefile for CS 325 Homework 2
# January 24th, 2020
# Compiles and creates executables
# for mergesort3.cpp merge3Time.cpp
#################################

CXX = g++
#CXXFLAGS = -std=c++0x -Wall -pedantic-errors -g

SRC_1 = mergesort3.cpp
SRC_2 = merge3Time.cpp

OBJ_1 = ${SRC_1:.cpp=.o}
OBJ_2 = ${SRC_2:.cpp=.o}

all: clean sort time
	@echo All files made

sort: clean
	${CXX} ${CXXFLAGS} ${SRC_1} -o ${OBJ_1}
	@clear
	${CXX} ${SRC_1} -o ${OBJ_1}
	@echo mergesort3 compiled

time: clean
	#${CXX} ${CXXFLAGS} ${SRC_2} -o ${OBJ_2}
	@clear
	${CXX} ${SRC_2} -o ${OBJ_2}
	@echo mergetime compiled

clean:
	rm -f *.o
