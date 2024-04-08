## 9.1 Intro
- A tree is conceptually described as a grouping of one or more interconnected nodes, where a singular node is distinguished as the root, and the remaining nodes can be classified into non-empty subsets, each forming a sub-tree emanating from the root.
### 9.11
- **Root node:** The root node R is the topmost node in the tree. If R = NULL, then it means the tree is empty.
- **Sub-trees:** If the root node R is not NULL, then the trees T1, T2, and T3 are called the sub-trees of R.
- **Leaf node:** A node that has no children is called the leaf node or the terminal node.
- **Path:** A sequence of consecutive edges is called a path. For example, in Fig. 9.1, the path from the root node A to node I is given as: A, D, and I.
- **Ancestor node:** An ancestor of a node is any predecessor node on the path from root to that node. The root node does not have any ancestors. In the tree given in Fig. 9.1, nodes A, C, and G are the ancestors of node K.
- **Descendant node:** A descendant node is any successor node on any path from the node to a leaf node. Leaf nodes do not have any descendants. In the tree given in Fig. 9.1, nodes C, G, J, and K are the descendants of node A.
- **Level number:** Every node in the tree is assigned a level number in such a way that the root node is at level 0, children of the root node are at level number 1. Thus, every node is at one level higher than its parent. So, all child nodes have a level number given by parent’s level number + 1.
- **Degree:** Degree of a node is equal to the number of children that a node has. The degree of a leaf node is zero.
- **In-degree:** In-degree of a node is the number of edges arriving at that node.
- **Out-degree:** Out-degree of a node is the number of edges leaving that node.
# Trees Overview

Trees are categorized into the following six types:

1. General trees
2. Forests
3. Binary trees
4. Binary search trees
5. Expression trees
6. Tournament trees
## 9.21 General trees
- General trees serve as hierarchical data structures for storing elements. The apex node of a tree assumes the role of the root, and every node, except the root, possesses a progenitor. A node within a general tree (excluding terminal nodes) may sprout zero or more sub-trees. 
- General trees serve as hierarchical data structures for storing elements. The apex node of a tree assumes the role of the root, and every node, except the root, possesses a progenitor. A node within a general tree (excluding terminal nodes) may sprout zero or more sub-trees. 
- Despite the amenability of general trees to be encapsulated within Abstract Data Types (ADTs), complications arise when appending additional sub-trees to a node already saturated with the maximum quota of sub-trees. 
## 9.22 Forests
- A forest is a disjoint union of trees. A set of disjoint trees (or forests) is obtained by deleting the
root and the edges connecting the root node to nodes at level 1. 
## 9.23 Binary trees
- A binary tree is a data structure that is defined as a collection of elements called nodes. In a binary tree, the topmost element is called the root node, and each node has 0, 1, or at the most 2 children. A node that has zero children is called a leaf node or a terminal node. Every node contains a data element, a left pointer which points to the left child, and a right pointer which points to the right child. The root element is pointed by a 'root' pointer. If root = NULL, then it means the tree is empty.

### Terminology

- **Parent:** If N is any node in T that has left successor S1 and right successor S2, then N is called the parent of S1 and S2. Correspondingly, S1 and S2 are called the left child and the right child of N. Every node other than the root node has a parent.
- **Level number:** Every node in the binary tree is assigned a level number. The root node is defined to be at level 0. The left and the right child of the root node have a level number 1. Similarly, every node is at one level higher than its parents. So all child nodes are defined to have level number as parent's level number + 1.
- **Degree of a node:** It is equal to the number of children that a node has. The degree of a leaf node is zero.
- **Sibling:** All nodes that are at the same level and share the same parent are called siblings (brothers).
- **Leaf node:** A node that has no children is called a leaf node or a terminal node.
- **Similar binary trees:** Two binary trees T and T' are said to be similar if both these trees have the same structure.
- **Copies:** Two binary trees T and T' are said to be copies if they have similar structure and if they have the same content at the corresponding nodes.
- **Edge:** It is the line connecting a node N to any of its successors. A binary tree of n nodes has exactly n – 1 edges because every node except the root node is connected to its parent via an edge.
- **Path:** A sequence of consecutive edges.
- **Depth:** The depth of a node N is given as the length of the path from the root R to the node N. The depth of the root node is zero.
- **Height of a tree:** It is the total number of nodes on the path from the root node to the deepest node in the tree. A tree with only a root node has a height of 1.
#### Complete Binary Trees

A complete binary tree is a binary tree that satisfies two properties. First, in a complete binary tree, every level, except possibly the last, is completely filled. Second, all nodes appear as far left as possible.

In a complete binary tree Tn, there are exactly n nodes and level r of T can have at most 2^r nodes.

The height of a tree Tn having exactly n nodes is given as:
Hn = | log2 (n + 1) |

## Extended Binary Trees

A binary tree T is said to be an extended binary tree (or a 2-tree) if each node in the tree has either no child or exactly two children. In an extended binary tree, nodes having two children are called internal nodes and nodes having no children are called external nodes.

To convert a binary tree into an extended tree, every empty sub-tree is replaced by a new node. The original nodes in the tree are the internal nodes, and the new nodes added are called the external nodes. Representation of Binary Trees in the Memory

### Linked representation of binary trees

In the linked representation of a binary tree, every node will have three parts: the data element, a pointer to the left node, and a pointer to the right node. 

## Sequential Representation of Binary Trees

Sequential representation of trees is done using single or one-dimensional arrays. Though it is the simplest technique for memory representation, it is inefficient as it requires a lot of memory space. A sequential binary tree follows the following rules:

- A one-dimensional array, called TREE, is used to store the elements of the tree.
- The root of the tree will be stored in the first location. That is, TREE[1] will store the data of the root element.
- The children of a node stored in location K will be stored in locations (2 × K) and (2 × K + 1).
- The maximum size of the array TREE is given as (2^h – 1), where h is the height of the tree.
- An empty tree or sub-tree is specified using NULL. If TREE[1] = NULL, then the tree is empty.

Figure 9.12 shows a binary tree and its corresponding sequential representation. The tree has 11 nodes and its height is 4.

## 9.2.4 Binary Search Trees

A binary search tree, also known as an ordered binary tree, is a variant of binary tree in which the nodes are arranged in an order. We will discuss the concept of binary search trees and different operations performed on them in the next chapter.

## 9.2.5 Expression Trees

Binary trees are widely used to store algebraic expressions. For example, consider the algebraic expression given as:

Exp = (a – b) + (c * d)

This expression can be represented using a binary tree as shown in Fig. 9.13.

## Expression Trees

Given the expression for the binary tree:

[{(a/b) + (c*d)} ^ {(f % g)/(h – i)}]

Example 9.4:
Given the expression, Exp = a + b / c * d – e, construct the corresponding binary tree.

Solution:
Use the operator precedence chart to find the sequence in which operations will be performed. The given expression can be written as:

Exp = ((a + ((b/c) * d)) – e)

## 9.2.6 Tournament Trees

In a tournament, say of chess, n number of players participate. To declare the winner among all these players, a couple of matches are played and usually three rounds are played in the game.

In every match of round 1, a number of matches are played in which two players play the game against each other. The number of matches that will be played in round 1 will depend on the number of players. For example, if there are 8 players participating in a chess tournament, then 4 matches will be played in round 1. Every match of round 1 will be played between two players.

Then in round 2, the winners of round 1 will play against each other. Similarly, in round 3, the winners of round 2 will play against each other and the person who wins round 3 is declared the winner. Tournament trees are used to represent this concept.

In a tournament tree (also called a selection tree), each external node represents a player and each internal node represents the winner of the match played between the players represented by its children nodes. These tournament trees are also called winner trees because they are being used to record the winner at each level. We can also have a loser tree that records the loser at each level.

Consider the tournament tree given in Fig. 9.14. There are 8 players in total whose names are represented using a, b, c, d, e, f, g, and h. In round 1, a and b; c and d; e and f; and finally g and h play against each other. In round 2, the winners of round 1, that is, a, d, e, and g play against each other. In round 3, the winners of round 2, a and e play against each other. Whosoever wins is declared the winner. In the tree, the root node a specifies the winner.

## 9.3 Creating a Binary Tree from a General Tree

The rules for converting a general tree to a binary tree are given below. Note that a general tree is converted into a binary tree and not a binary search tree.

- Rule 1: Root of the binary tree = Root of the general tree
- Rule 2: Left child of a node = Leftmost child of the node in the binary tree in the general tree
- Rule 3: Right child of a node in the binary tree = Right sibling of the node in the general tree