#include <stdio.h>

#define MAXZ_STACK_SIZE 100

typedef struct {
  int key;
} element;

element stack[MAX_STACK_SIZE];
int top = -1;

void push(element item) {
  if (top >= MAX_STACK_SIZE-1) {
    stackFull();
  }
  stack[++top] = item;
}

element pop() {
  if (top == -1) { 
    return stackEmpty();
  }
  return stack[top--];
}

void stackFull() {
  fprintf(stderr, "Stack is full, cannot add element");
  exit(-1);
}


