/*******************************************
 * Jesus Narvaez
 * CS 325 Homework 1
 * insertTime.cpp
 * January 15th, 2020
 * This program uses insertion sort to sort an
 * array of random numbers from 1 to 10000 of
 * size n and times it.
*******************************************/

#include <iostream>
#include <stdio.h>
#include <fstream>
#include <ctime>
#include <stdlib.h>

using namespace std;

/*******************************************
* Function name: print_array
* Description: Given an array and the size of
*   the array, the elements of the array are
*   printed to the terminal. This function was
*   used mainly in debugging.
*******************************************/
void print_array(int dataset[], int size){
    //Iterate through for the size of the array
    for (int i = 0; i < size; i++)
        cout << dataset[i] << " ";
    cout << endl;
    return;
}

/*******************************************
* Function name: print_to_file
* Description: Given an array and the size of
*   the array, it uses the output stream class
*   to print the elements of the array into a file
*   called "insert.txt".
* This function is not used in this program
*******************************************/
void print_to_file(int dataset[], int size){

    //Open the file to output
    ofstream out_file;
    out_file.open ("insert.txt");

    //Iterate through the array and print each element to our file
    for (int i = 1; i < size + 1; i++)
        out_file << dataset[i] << " ";
    out_file << endl;

    //Close the file
    out_file.close();
    return;
}

/*******************************************
* Function name: insert_sort
* Description: Given an array and the size of
*   the array, the algorithm grabs an element
*   and compares it to the elements that came
*   before it to place it in the correct.
*******************************************/
void insert_sort(int dataset[], int size){

    //Iterate starting at second element
    for (int i = 1; i < size; i++){

        //Set key as the element to compare and j as the previous index
        int key = dataset[i];
        int j = i - 1;

        //ensure we don't reach the start of the array or the previous
        //element is not smaller than key
        while ((j >= 0) && (dataset[j] > key)){
            dataset[j+1] = dataset[j];
            j--;
        }

        //Re-adjust the array
        dataset[j+1] = key;
    }
    return;
}

/*******************************************
* Function name: random_array
* Description: Takes an array of size "size"
*   and fills each index with a random number
*   from 1 to 10000
*******************************************/
void random_array(int dataset[], int size){
    for (int i = 0; i < size; i++)
        dataset[i] = rand() % 10001;
    return;
}

/*******************************************
* Function name: main
* Description: Creates and calls random_array
*   to fill an array of size n. The array is
*   sorted using insertion sort and timed.
*   The time is reported at the end.
*******************************************/
int main(){
    //Seed random number generator and init start_time
    srand(time(NULL));
    clock_t start_time;

    //Input size of array here!
    int n = 140000;
    int data[n];

    //Fill the array with random numbers
    random_array(data, n);

    //Time insertion sort
    start_time = clock();
    insert_sort(data, n);
    start_time = clock() - start_time;

    //Divide the CPU ticks by clock cycles per second
    double total_time = ((float) (start_time)) / CLOCKS_PER_SEC;
    cout << "Array size: " << n << endl;
    cout << "Total time inserting: " << total_time << " seconds" << endl;
    return 0;
}
