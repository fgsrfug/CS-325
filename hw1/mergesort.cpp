/*******************************************
 * Jesus Narvaez
 * CS 325 Homework 1
 * mergesort.cpp
 * January 15th, 2020
 * This file uses mergeion sort to sort a list
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
*   called "merge.txt".
*******************************************/
void print_to_file(int dataset[], int size){

    //Open the file to output
    ofstream out_file;
    out_file.open ("merge.txt");
    //Iterate through the array and print each element to our file
    for (int i = 1; i < size + 1; i++)
        out_file << dataset[i] << " ";
    out_file << endl;

    //Close the file
    out_file.close();
    return;
}


void merge(int dataset[], int l_index, int r_index, int midpoint, int data_size){
    //Determine the size of temp arrays to create using indexes
    //that were passed in
    int l_array_size = midpoint - l_index + 1;
    int r_array_size = r_index - midpoint;

    //Create temp arrays and initialize them to 0
    int l_array[l_array_size];
    for (int k = 0; k < l_array_size; k++)
        l_array[k] = 0;

    int r_array[r_array_size];
    for (int k = 0; k < r_array_size; k++)
        r_array[k] = 0;

    //Fill the temp arrays with actual values from dataset
    for (int i = 0; i < l_array_size; i++)
        l_array[i] = dataset[i + l_index];
    for (int j = 0; j < r_array_size; j++){
        r_array[j] = dataset[j + midpoint + 1];
    }

    //Create new indices to to iterate temp arrays and dataset array
    int left = 0;
    int right = 0;
    int main = l_index;

    //While there is an element in both arrays, keep comparing them
    //Which ever element is smaller between the two arrays get placed
    //into the dataset array.
    while ((left < l_array_size) && (right < r_array_size)){
        if (l_array[left] <= r_array[right]){
            dataset[main] = l_array[left];
            left++;
        }
        else {
            dataset[main] = r_array[right];
            right++;
        }
        main++;
    }

    //Make sure that any leftovers in either array gets placed last
    //in dataset.
    while (left < l_array_size){
        dataset[main] = l_array[left];
        left++;
        main++;
    }
    while (right < r_array_size){
        dataset[main] = r_array[right];
        right++;
        main++;
    }
}

/*******************************************
* Function name: merge_sort
* Description: Given an array and the size of
*   the array, the algorithm grabs an element
*   and compares it to the elements that came
*   before it to place it in the correct.
*******************************************/
void merge_sort(int dataset[], int l_index, int r_index, int data_size){
    if (l_index < r_index){
        int midpoint = (l_index + r_index)/2;
        merge_sort(dataset, l_index, midpoint, data_size);
        merge_sort(dataset, midpoint + 1, r_index, data_size);

        merge(dataset, l_index, r_index, midpoint, data_size);
    }
}
/*******************************************
* Function name: main
* Description: Function in charge of executing
* the other functions and tasked in regards to
* creating mergeion sort
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

    //Set the indices, call merge_sort, and print to file
    int l_index = 1;
    int r_index = data_size;
    merge_sort(data, l_index, r_index, data_size);
    print_to_file(data, data_size);

    return 0;
}
