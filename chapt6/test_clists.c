#include <stdio.h>
#include "ctest.h"
#include "clist.h"

int main()
{
    BEGIN_TESTING("list.h");

    TEST("Can remove node from circular linked list") {
        Node* mylist = NULL;
        Node* n;

        // Creating a circular linked list with even numbers from 0 to 6
        for (int i = 0; i < 7; i += 2) {
            n = make_node(i);
            insert_at_end(&mylist, &n);
        }

        // Connecting the last node to the first node to form a circular list
        Node* last_node = mylist;
        while (last_node->next != NULL) {
            last_node = last_node->next;
        }
        last_node->next = mylist;

        // Testing the initial state of the circular linked list
        RETURNS_STR(print_list, "0 -> 2 -> 4 -> 6", (mylist));

        // Storing the pointer to the node to be removed
        Node* node_to_remove = mylist->next->next; // Pointing to node with value 4

        // Removing the node with value 4 from the circular linked list
        Node* removed_node = remove_from_list(&mylist, 4); 

        // Asserting that the removed node is the same as the expected node
        ASSERT_EQ(node_to_remove, removed_node);

        // Testing the state of the circular linked list after removal
        RETURNS_STR(print_list, "0 -> 2 -> 6", (mylist));
    }

    TEST("Can insert node at specified index in circular linked list") {
        Node* mylist = NULL;
        Node* n;

        // Creating a circular linked list with even numbers from 0 to 6
        for (int i = 0; i < 7; i += 2) {
            n = make_node(i);
            insert_at_end(&mylist, &n);
        }
        // Connecting the last node to the first node to form a circular list
        Node* last_node = mylist;
        while (last_node->next != NULL) {
            last_node = last_node->next;
        }
        last_node->next = mylist;

        // Testing the initial state of the circular linked list
        RETURNS_STR(print_list, "0 -> 2 -> 4 -> 6", (mylist));

        // Inserting a node with value 3 at index 2
        insert_at_index(&mylist, 3, 2);

        // Testing the state of the circular linked list after insertion
        RETURNS_STR(print_list, "0 -> 2 -> 3 -> 4 -> 6", (mylist));

        // Inserting a node with value 1 at index 0
        insert_at_index(&mylist, 1, 0);

        // Testing the state of the circular linked list after insertion
        RETURNS_STR(print_list, "1 -> 0 -> 2 -> 3 -> 4 -> 6", (mylist));

        // Inserting a node with value 7 at index 6
        insert_at_index(&mylist, 7, 6);

        // Testing the state of the circular linked list after insertion
        RETURNS_STR(print_list, "1 -> 0 -> 2 -> 3 -> 4 -> 6 -> 7", (mylist));
    }

    TEST("Can insert node in order in descending list") {
        // Confirm works with empty list
        Node* myclist = NULL;

        Node* n = make_node(4);
        clist_insert_in_order(&myclist, &n);
        RETURNS_STR(print_list, "4", (myclist));

        n = make_node(2);
        clist_insert_in_order(&myclist, &n);
        RETURNS_STR(print_list, "2 -> 4", (myclist));

        n = make_node(3);
        clist_insert_in_order(&myclist, &n);
        RETURNS_STR(printlist, "2 -> 3 -> 4", (myclist));

        n = make_node(5);
        clist_insert_in_order(&myclist, &n);
        RETURNS_STR(print_list, "2 -> 3 -> 4 -> 5", (myclist));
    }


    END_TESTING();
}

