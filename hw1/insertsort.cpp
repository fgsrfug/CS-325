/*******************************************
 * Jesus Narvaez
 * CS 325 Homework 1
 * insertsort.cpp
 * January 15th, 2020
 * This file uses insertion sort to sort a list
 * of integers from a file called data.txt.
*******************************************/

#include <iostream>
#include <fstream>
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
    for (int i = 1; i < size + 1; i++)
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
    for (int i = 1; i < size + 1; i++){

        //Set key as the element to compare and j as the previous index
        int key = dataset[i];
        int j = i - 1;

        //ensure we don't reach the start of the array or the previous
        //element is not smaller than key
        while ((j >= 1) && (dataset[j] > key)){
            dataset[j+1] = dataset[j];
            j--;
        }

        //Re-adjust the array
        dataset[j+1] = key;
    }
    return;
}


/*******************************************
* Function name: main
* Description: Function in charge of executing
* the other functions and tasked in regards to
* creating insertion sort
*******************************************/
int main(){
    //Open data.txt and get the size
    ifstream text_file;
    int data_size;
    text_file.open("data.txt");
    text_file >> data_size;
    text_file.close();

    //Create array of size data_size and read data.txt to fill our array
    int data[data_size];
    text_file.open("data.txt");
    int i = 0;
    while (!text_file.eof()){
        text_file >> data[i];
        i++;
    }
    text_file.close();

    //Sort the array and print to file
    insert_sort(data, data_size);
    print_to_file(data, data_size);

    return 0;
}
