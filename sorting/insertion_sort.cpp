#include <iostream>
#define MAX_SIZE 101

void insertion_sort(int *list, int n) {
  int key = 0;
  int i = 0;
  int j = 0;

  for (int i = 1; i < n; i++) {
    key = list[i];
    j = i - 1;
    while (j >= 0 && list[j] > key) {
      list[j+1] = list[j];
      j = j - 1;
    }
    list[j+1] = key;
  }
}

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
  printf("\n");

  insertion_sort(list, n);
  printf("\nSorted array:\n");

  for (i = 0; i < n; i++)
    printf("%d  ", list[i]);
  printf("\n");

  return 0;
}
