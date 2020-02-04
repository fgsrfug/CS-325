#################################
# Jesus Narvaez
# Makefile for CS 325 Homework 1
# January 15th, 2020
# Compiles and creates executables
# for insertsort.cpp, mergesort.cpp,
# insertTime.cpp and mergeTime.cpp
#################################

CXX = g++
#CXXFLAGS = -std=c++0x -Wall -pedantic-errors -g

SRC_1 = insertsort.cpp
SRC_2 = mergesort.cpp
SRC_3 = insertTime.cpp
SRC_4 = mergeTime.cpp

OBJ_1 = ${SRC_1:.cpp=.o}
OBJ_2 = ${SRC_2:.cpp=.o}
OBJ_3 = ${SRC_3:.cpp=.o}
OBJ_4 = ${SRC_4:.cpp=.o}

all: clean insert merge
	@echo All files made

insert: clean
	#${CXX} ${CXXFLAGS} ${SRC_1} -o ${OBJ_1}
	${CXX} ${SRC_1} -o ${OBJ_1}
	@echo insertsort compiled
	${CXX} ${SRC_3} -o ${OBJ_3}
	@echo insertsort compiled

merge: clean
	#${CXX} ${CXXFLAGS} ${SRC_2} -o ${OBJ_2}
	@clear
	${CXX} ${SRC_2} -o ${OBJ_2}
	${CXX} ${SRC_4} -o ${OBJ_4}
	@echo mergesort compiled

clean:
	rm -f *.o
