#ifndef SORT_H
#define SORT_H

#define MAX 2000

#include <stdlib.h>
#include <stdio.h>

/**
 * merge_sort - sorts an array in ascending order using Merge Sort.
 * @array:    [*int] pointer to the head of the array
 * @size:     [size_t] size of the array
 **/
void merge_sort(int *array, size_t size);

/**
 * print_array - prints an array of integers.
 * @array:    [*const int] pointer to the head of the array
 * @size:     [size_t] size of the array
 **/
void print_array(const int *array, size_t size);

#endif /* SORT_H */
