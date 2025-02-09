#include "sort.h"

/**
 * unite - Combines left and right arrays into the original one
 * @size:     [int] size of the array
 * @array:    [*int] pointer to the head of the array
 * @left:     [*int] pointer to left array
 * @right:    [*int] pointer to right array
 **/
void unite(size_t size, int *array, int *left, int *right)
{
    int i, j, k, l_length, r_length;

    i = j = k = 0;
    l_length = size / 2;
    r_length = size - l_length;

    printf("Merging...\n");
    printf("[left]: ");
    print_array(left, l_length);
    printf("[right]: ");
    print_array(right, r_length);

    while (i < l_length && j < r_length)
        array[k++] = (left[i] < right[j]) ? left[i++] : right[j++];

    while (i < l_length)
        array[k++] = left[i++];

    while (j < r_length)
        array[k++] = right[j++];

    printf("[Done]: ");
    print_array(array, size);
}

/**
 * merge_sort - sorts in ascending order using Merge Sort method.
 * @array:    [*int] pointer to the head of the array
 * @size:     [int] size of the array
 **/
void merge_sort(int *array, size_t size)
{
    size_t middle, i;
    int left[MAX], right[MAX];

    if (!array || size < 2)
        return;

    for (i = 0, middle = size / 2; i < middle; i++)
        left[i] = array[i];

    for (i = middle; i < size; i++)
        right[i - middle] = array[i];

    merge_sort(left, middle);
    merge_sort(right, size - middle);
    unite(size, array, left, right);
}
