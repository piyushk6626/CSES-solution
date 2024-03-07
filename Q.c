#include <stdio.h>
#include <stdlib.h>

// Node structure
struct Node {
    int data;
    struct Node* next;
};

struct Node* front = NULL;
struct Node* rear = NULL;

// Function to enqueue a new element
void enqueue(int value) {
    // Create a new node
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Memory allocation failed. Cannot enqueue.\n");
        return;
    }
    newNode->data = value;
    newNode->next = NULL;

    // If the queue is empty, set both front and rear to the new node
    if (rear == NULL) {
        front = rear = newNode;
    } else {
        // Otherwise, add the new node to the end of the queue
        rear->next = newNode;
        rear = newNode;
    }
    printf("%d enqueued to queue.\n", value);
}

// Function to dequeue an element
void dequeue() {
    // If the queue is empty, print an error message
    if (front == NULL) {
        printf("Queue is empty. Cannot dequeue.\n");
        return;
    }

    // Store the front node and move front pointer to the next node
    struct Node* temp = front;
    front = front->next;

    // If front becomes NULL, set rear to NULL as well
    if (front == NULL) {
        rear = NULL;
    }

    printf("%d dequeued from queue.\n", temp->data);
    free(temp); // Free the memory of the dequeued node
}

// Function to display the elements of the queue
void display() {
    struct Node* temp = front;
    if (temp == NULL) {
        printf("Queue is empty.\n");
        return;
    }
    printf("Queue elements: ");
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
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
