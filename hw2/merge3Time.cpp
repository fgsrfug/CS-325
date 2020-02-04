/*******************************************
 * Jesus Narvaez
 * CS 325 Homework 2
 * merge3Time.cpp
 * January 24th, 2020
 * This file uses a 3 way version of merge sort to sort a list
 * of integers from a file records time elapsed
*******************************************/
#include <iostream>
#include <fstream>
#include <ctime>
#include <stdio.h>
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
*   called "merge.txt".
*******************************************/
void print_to_file(int dataset[], int size){

    //Open the file to output
    ofstream out_file;
    out_file.open ("merge.txt");
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
void merge3(int dataset[], int l_index, int r_index, int mid1, int mid2, int dataset2[]){

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
void merge_sort3(int dataset[], int l_index, int r_index, int dataset2[]){

    //If the boundaries are too small, return
    if (r_index - l_index <= 1){
        return;
    }

    //Set the midpoints of section to sort
    int mid1 = l_index + ((r_index - l_index) / 3);
    int mid2 = l_index + (2 * ((r_index - l_index) / 3)) + 1;

    //Continuously split the array into thirds
    merge_sort3(dataset, l_index, mid1, dataset2);
    merge_sort3(dataset, mid1, mid2, dataset2);
    merge_sort3(dataset, mid2, r_index, dataset2);

    //Merge sort sections that have been split
    merge3(dataset, l_index, r_index, mid1, mid2, dataset2);

    //Once part of the sorted array is filled in,
    //update the original.
    for (int i = l_index; i < r_index; i++)
        dataset[i] = dataset2[i];
}

/*******************************************
* Function name: random_array
* Description: Takes an array of size "size"
*   and fills each index with a random number
*   from 1 to 10000
*******************************************/
void random_array(int dataset[], int size){
    for (int i = 0; i < size; i++){
        dataset[i] = rand() % 10001;
    }

    return;
}
/*******************************************
* Function name: main
* Description: Function in charge of executing
*   the other functions and tasked in regards to
*   creating mergeion sort
*******************************************/
int main(){
    //Seed random number generator and init start_time
    srand(time(NULL));
    clock_t start_time;

    //Set the size of the array here!
    int n = 900000;
    int data[n];
    int data2[n];

    //Fill the array with random numbers
    random_array(data, n);

    //Set indices for use in merge sort
    int l_index = 0;
    int r_index = n;

    //Time merge sort
    start_time = clock();
    merge_sort3(data, l_index, r_index, data2);
    start_time = clock() - start_time;

    //Divide CPU ticks by CLOCKS_PER_SEC and present results
    double total_time = ((float) (start_time)) / CLOCKS_PER_SEC;
    cout << "Array size: " << n << endl;
    cout << "Total time merging: " << total_time << " seconds" <<  endl;

    return 0;

}
