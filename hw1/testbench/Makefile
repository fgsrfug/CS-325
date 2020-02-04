CXX = g++
CXXFLAGS = -std=c++0x -Wall -pedantic-errors -g

SRCS =  algo1.cpp
OBJS = ${SRCS:.cpp=.o}
HEADERS = 

MAIN = algo_bin

all: ${MAIN}
	        @echo   File has been compiled

${MAIN}: ${OBJS}
	        ${CXX} ${CXXFLAGS} ${OBJS} -o ${MAIN}

.cpp.o:
	        ${CXX} ${CXXFLAGS} -c $< -o $@

clean:
	        ${RM} ${PROGS} ${OBJS} *.o *~.
