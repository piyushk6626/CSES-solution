#include <stdio.h>

#define MAX_SIZE 100

int Q[MAX_SIZE];
int f = -1, r = -1;

void enqueue(int value) {
    if (r == MAX_SIZE - 1) {
        printf("Queue is full. Cannot enqueue.\n");
    } else {
        if (f == -1) {
            f = 0;
        }
        r++;
        Q[r] = value;
        printf("%d enqueued to queue.\n", value);
    }
}

void dequeue() {
    if (f == -1 || f > r) {
        printf("Queue is empty. Cannot dequeue.\n");
    } else {
        printf("%d dequeued from queue.\n", Q[f]);
        f++;
    }
}

void display() {
    if (f == -1 || f > r) {
        printf("Queue is empty.\n");
    } else {
        printf("Queue elements: ");
        for (int i = f; i <= r; i++) {
            printf("%d ", Q[i]);
        }
        printf("\n");
    }
}

int main() {
    enqueue(10);
    enqueue(20);
    enqueue(30);
    display();
    dequeue();
    display();
    return 0;
}
