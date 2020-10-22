#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define MAX_SIZE 101

void swap(int *, int *);
void sort(int [], int);

int compare(int x, int y) {
  if (x < y) return -1;
  else if (x == y) return 0;
  else return 1;
}

int binarySearch(int list[], int searchnum, int left, int right) {
  int middle;
  while (left <= right) {
    middle = (left + right) / 2;
    switch (compare(list[middle], searchnum)) {
      case -1:
        left = middle + 1;
        // binarySearch(list, searchnum, middle + 1, right); // Recursive
        break;
      case 0: return middle;
      case 1: right = middle - 1;
        // binarySearch(list, searchnum, left, middle - 1); // Recursive
    }
  }
  return -1;
}

int main(void) {

  int searchnum, i, n;
  int list[MAX_SIZE];
  printf("Enter the number of numbers to generate: ");
  scanf("%d", &n);

  if ( n < 1 || n > MAX_SIZE) {
    fprintf(stderr, "Improper value of n\n");
    exit(-1);
  }

  for (i = 0; i < n; i++) {
    list[i] = rand() % 1000;
    printf("%d  ", list[i]);
  }

  sort(list, n);
  printf("\nSorted array:\n");

  for (i = 0; i < n; i++)
    printf("%d  ", list[i]);
  printf("\n");

  // Binary Search
  printf("\nEnter a number to search: ");
  scanf("%d", &searchnum);

  int index = binarySearch(list, searchnum, 0, n);
  printf("\nSearch Result\n");
  printf("index: %d, value: %d\n", index, list[index]);
	return 0;
}

void swap(int *x, int *y) {
  int temp  = *x;
  *x = *y;
  *y = temp;
}

void sort(int list[], int n) {
  int i, j, min;
  for (i = 0; i < n-1; i++) {
    min = i;
    for (j = i+1; j < n; j++) {
      if (list[j] < list[min])
        min = j;
    }
    swap(&list[i], &list[min]);
  }
}
