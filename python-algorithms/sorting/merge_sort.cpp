#include <iostream>
#define MAX_SIZE 101

void merge(int list[], int p, int q, int r) {
  int i = 0;
  int j = 0;

  int n1 = q - p + 1;
  int n2 = r - q - 1;

  int L[MAX_SIZE];
  int R[MAX_SIZE];

  for (i = 0; i < n1; i++) {
    L[i] = list[p+i];
  }

  for (j = 0; j < n2; j++) {
    R[j] = list[q+j];
  }

  i = 0;
  j = 0;

  for (int k = p; k < r; k++) {
    if (L[i] <= R[j]) {
      list[k] = L[i];
      i++;
    } else {
      list[k] =  R[j];
      j++;
    }
  }
}

void merge_sort(int list[], int p, int r) {
  if (p < r) {
    int q = (p + r) / 2;
    merge_sort(list, p, q);
    merge_sort(list, q + 1, r);
    printf("%d %d %d\n", p, q, r);
    merge(list, p, q, r);
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

  merge_sort(list, 0, n);
  printf("\nSorted array:\n");

  for (i = 0; i < n; i++)
    printf("%d  ", list[i]);
  printf("\n");

  return 0;
  return 0;
}
