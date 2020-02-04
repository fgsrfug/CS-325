/*******************************************
 * Jesus Narvaez
 * CS 325 Homework 2
 * mergesort3.cpp
 * January 24th, 2020
 * This file uses a 3 way version of merge sort to sort a list
 * of integers from a file called data.txt.
*******************************************/
#include <iostream>
#include <sstream>
#include <fstream>
#include <string.h>
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
*   called "merge3.txt".
*******************************************/
void print_to_file(int dataset[], int size){

    //Open the file to output
    ofstream out_file;
    out_file.open ("merge3.txt");
    //Iterate through the array and print each element to our file
    for (int i = 0; i < size; i++)
        out_file << dataset[i] << " ";
    out_file << endl;

    //Close the file
    out_file.close();
    return;
}


/*******************************************
* Function name: merge3
* Description: Given an array subdivided into
*   3 subsections, merge3 sorts the section
*   of the array that was passed in.
*******************************************/
void merge3(int dataset[], int l_index, int r_index, int mid1, int mid2, int dataset2[], int datasize){

    //Set the 3 indices for the original array,
    //and set the index for the sorted array
    int a1i = l_index;
    int a2i = mid1;
    int a3i = mid2;
    int d_index = l_index;

    //Go through all 3 subsections of the original array
    while ((a1i < mid1) && (a2i < mid2) && (a3i < r_index)){
        if (dataset[a1i] < dataset[a2i]){
            if (dataset[a1i] < dataset[a3i]){
                //Current a1i element is the smallest
                //Place that element in sorted array
                dataset2[d_index] = dataset[a1i];
                a1i++;
                d_index++;
            }
            else {
                //Current a3i element is the smallest
                //Place that element in sorted array
                dataset2[d_index] = dataset[a3i];
                a3i++;
                d_index++;
            }
        }
        else {
                //Current a2i element is the smallest
                //Place that element in sorted array
            if (dataset[a2i] < dataset[a3i]){
                dataset2[d_index] = dataset[a2i];
                a2i++;
                d_index++;
            }
            else{
                //Current a3i element is the smallest
                //Place that element in sorted array
                dataset2[d_index] = dataset[a3i];
                a3i++;
                d_index++;
            }
        }
    }

    //Go through second and third subsections of the original array
    while ((a2i < mid2) && (a3i < r_index)){
        if (dataset[a2i] < dataset[a3i]){
            //Current a2i element is the smallest
            //Place that element in sorted array
            dataset2[d_index] = dataset[a2i];
            a2i++;
            d_index++;
        }
        else {
            //Current a3i element is the smallest
            //Place that element in sorted array
            dataset2[d_index] = dataset[a3i];
            a3i++;
            d_index++;
        }
    }

    while ((a1i < mid1) && (a3i < r_index)){
        if (dataset[a1i] < dataset[a3i]){
            //Current a1i element is the smallest
            //Place that element in sorted array
            dataset2[d_index] = dataset[a1i];
            a1i++;
            d_index++;
        }
        else {
            //Current a3i element is the smallest
            //Place that element in sorted array
            dataset2[d_index] = dataset[a3i];
            a3i++;
            d_index++;
        }
    }

    while ((a1i < mid1) && (a2i < mid2)){
        if (dataset[a1i] < dataset[a2i]){
            //Current a1i element is the smallest
            //Place that element in sorted array
            dataset2[d_index] = dataset[a1i];
            a1i++;
            d_index++;
        }
        else {
            //Current a3i element is the smallest
            //Place that element in sorted array
            dataset2[d_index] = dataset[a2i];
            a2i++;
            d_index++;
        }
    }

    //Place whatever elements remain in the subsections
    //into the sorted array at the end
    while (a1i < mid1){
        dataset2[d_index] = dataset[a1i];
        a1i++;
        d_index++;
    }

    while (a2i < mid2){
        dataset2[d_index] = dataset[a2i];
        a2i++;
        d_index++;
    }

    while (a3i < r_index){
        dataset2[d_index] = dataset[a3i];
        a3i++;
        d_index++;
    }
}

/*******************************************
* Function name: merge_sort3
* Description: Given an array and the boundaries
*   to sort for, keep reducing the boundaries
*   of the subsection until the boundaries
*   cannot get any smaller.
*******************************************/
void merge_sort3(int dataset[], int l_index, int r_index, int dataset2[], int datasize){

    //If the boundaries are too small, return
    if (r_index - l_index <= 1){
        return;
    }

    //Set the midpoints of section to sort
    int mid1 = l_index + ((r_index - l_index) / 3);
    int mid2 = l_index + (2 * ((r_index - l_index) / 3)) + 1;

    //Continuously split the array into thirds
    merge_sort3(dataset, l_index, mid1, dataset2, datasize);
    merge_sort3(dataset, mid1, mid2, dataset2, datasize);
    merge_sort3(dataset, mid2, r_index, dataset2, datasize);

    //Merge sort sections that have been split
    merge3(dataset, l_index, r_index, mid1, mid2, dataset2, datasize);

    //Once part of the sorted array is filled in,
    //update the original.
    for (int i = l_index; i < r_index; i++)
        dataset[i] = dataset2[i];
}
/*******************************************
* Function name: main
* Description: Function in charge of executing
*   the other functions and tasked in regards to
*   creating mergeion sort
*******************************************/
int main(){
    //Open data.txt and get the size
    ifstream text_file;
    int data_size;
    text_file.open("data.txt");
    text_file >> data_size;
    text_file.close();

    //Create a temp array to collect all data from data.txt
    int temp[data_size + 1];

    //data[] array will hold all data from data.txt sans the first element
    int data[data_size];

    //data2[] array will hold the sorted array
    int data2[data_size];

    //Open data.txt and collect all data
    text_file.open("data.txt");
    int i = 0;
    while (!text_file.eof()){
        text_file >> temp[i];
        i++;
    }
    text_file.close();

    //Give data[] elements to sort
    //Initialize all data2[] elements to -1
    for (int j = 0; j < data_size; j++) {
        data[j] = temp[j + 1];
        data2[j] = -1;
    }

    //Set the indices, call merge_sort3, and print to file
    int l_index = 0;
    int r_index = data_size;

    merge_sort3(data, l_index, r_index, data2, data_size);

    print_to_file(data2, data_size);

    return 0;
}
