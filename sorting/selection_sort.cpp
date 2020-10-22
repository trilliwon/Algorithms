#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define MAX_SIZE 101

void swap(int *, int *);
void selection_sort(int [], int);

int main(void) {
  int i, n;
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

  selection_sort(list, n);
  printf("\nSorted array:\n");

  for (i = 0; i < n; i++)
    printf("%d  ", list[i]);
  printf("\n");

	return 0;
}

void swap(int *x, int *y) {
  int temp  = *x;
  *x = *y;
  *y = temp;
}

void selection_sort(int list[], int n) {
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
