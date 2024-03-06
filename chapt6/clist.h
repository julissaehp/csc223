typedef struct node {
    int val;
    struct node* next;
} Node;

Node* make_node(int);
Node* remove_from_list(Node**, int);
void insert_at_end(Node**, Node**);
char* print_list(Node*);
void clist_insert_in_order(Node**, Node**);
void insert_at_index(Node**, int, int);

