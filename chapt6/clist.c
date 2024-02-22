#include <stdio.h>
#include <stdlib.h>
#include "clist.h"


Node* make_node(int data)
{
    Node* new = malloc(sizeof(Node));
    if (new == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    new->val = data;
    new->next = NULL;

    return new;
}


void insert_in_front(Node** list, Node** newnode)
{
    (*newnode)->next = *list;
    *list = *newnode;
}


int list_length(Node* head) {
    int count = 0;
    Node* ptr = head;
    while (ptr != NULL) {
        count = count + 1;
        ptr = ptr->next;
    }
    return count;
}


char* print_list(Node* head) {
    char* result = malloc(1024);

    int index = 0;
    Node* node = head;
    while (node != NULL) {
        int num_len = snprintf(NULL, 0, "%d", node->val);
        snprintf(result + index, 8, "%d", node->val);
        index += num_len - 1;
        if (node->next != NULL) {
            result[++index] = ' ';
            result[++index] = '-';
            result[++index] = '>';
            result[++index] = ' ';
        }
        index++;

        node = node->next;
    }
    result[index] = '\0';

    return result;
}


Node* find_in_list(Node* list, int target)
{
    Node* current = list;

    for (Node* current = list; current != NULL; current = current->next) {
        if (current->val == target) {
            return current;
        }
    }
    return NULL;
}


void insert_at_end(Node** list, Node** newnode) {
    // If the list is empty, make the new node the head of the list
    if (*list == NULL) {
        *list = *newnode;
    } else {
        // Traverse the list to find the last node
        Node* current = *list;
        while (current->next != NULL) {
            current = current->next;
        }
        // Insert the new node at the end of the list
        current->next = *newnode;
    }
}

void insert_in_order(Node** list, Node** newnode) {
    Node *current, *previous;

    previous = *list;
    if (previous == NULL) {     
        *list = *newnode;
        return;
    }
    current = previous->next;
    while (current != NULL && current->val > (*newnode)->val) {
        previous = current;
        current = current->next;
    }
    // insert newnode between previous and current (or at end)
    (*newnode)->next = current;
    previous->next = *newnode;
}


Node* remove_from_list(Node** list, int val) {
    Node *current, *previous;
    previous = *list;
    if (previous == NULL) {     
        return NULL;
    }
    current = previous->next;
    while (current != NULL && current->val != val) {
        previous = current;
        current = current->next;
    }

    if (current == NULL) return NULL;  // val not found

    // disconnect found node from list and return
    previous->next = current->next;
    return current;
}
typedef struct Node {
    int val;
    struct Node *next;
} Node;

// Function to find the length of a circular linked list
int list_length(Node *head) {
    int count = 0;
    Node *ptr = head;

    // Check if the list is empty
    if (head == NULL) {
        return count;
    }

    // Traverse the circular list
    do {
        count = count + 1;
        ptr = ptr->next;
    } while (ptr != head);

    return count;
}

// Function to insert a node at the end of the circular linked list
void insert_at_end(Node **head, int data) {
    Node *new_node = (Node *)malloc(sizeof(Node));
    new_node->val = data;
    new_node->next = *head;

    if (*head == NULL) {
        *head = new_node;
        new_node->next = *head;
    } else {
        Node *temp = *head;
        while (temp->next != *head) {
            temp = temp->next;
        }
        temp->next = new_node;
    }
}

// Function to display the circular linked list
void display_list(Node *head) {
    Node *current = head;

    if (head != NULL) {
        do {
            printf("%d ", current->val);
            current = current->next;
        } while (current != head);
        printf("\n");
    }
}

int main() {
    Node *circularList = NULL;

    // Insert nodes at the end to create a circular linked list
    for (int i = 1; i <= 5; i++) {
        insert_at_end(&circularList, i);
    }

    // Display the circular linked list
    printf("Circular Linked List: ");
    display_list(circularList);

    // Find the length of the circular linked list
    int length = list_length(circularList);
    printf("Length of the circular linked list: %d\n", length);

    return 0;
}