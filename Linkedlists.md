 # Linked Lists:

## Definition: Linked lists are a data structure addressing issues of arrays, such as limitations on maximum elements and sequential data storage.

# Structure: 
Divided into two parts - the left stores data, and the right contains a pointer to the next node.

Access: Sequential access only; no random access like arrays.

# Inserting Nodes:

- To insert at the beginning, new start node points to the previous start node.
- To insert at the end, previous end node points to the new end node, which contains the terminating value.
For insertion between nodes, set the preceding node to point to the new node, and the new node points to the succeeding node.
# Deleting Nodes:

To delete the starting node, change the starting variable to point to the desired new starting node.
- For nodes between start and end, set the preceding node to point to the succeeding node, bypassing the deleted node.
To delete the last node, replace the pointer of the preceding node with the terminating value.



