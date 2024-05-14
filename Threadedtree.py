# 
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.is_threaded_right = False


class ThreadedBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):# Insert a new node
        if not self.root:# If the tree is empty (no root node) 
            self.root = TreeNode(key)# then the new key becomes the root node
            return

        node = self.root
        while True:
            if key < node.key:# If the new key is less than the currents node's key then move to the left subtree
                if node.left:# if there is a left child 
                    node = node.left# then "node" will move down to the left subtree
                else:# if no left childe insert new node as left child of the node
                    node.left = TreeNode(key)
                    node.left.right = node #This established the threaded connection by setting the right pointer of the new node to the current node
                    node.left.is_threaded_right = True # indicate that the right pointer of the new node is a thread
                    return
            else:
                if node.is_threaded_right or not node.right:#If the current node's right pointer is a thread or there's no right child, we insert the new node here
                    new_node = TreeNode(key)
                    new_node.right = node.right# Set the right child of the new node to the current node's right child.
                    node.right = new_node#Make the new node the right child of the current node
                    node.is_threaded_right = False #Since we've inserted a new right child, we mark the right pointer of the current node as not being a thread.
                    new_node.is_threaded_right = True#Mark the right pointer of the new node as a thread.
                    return# new node is inserted exit the function
                node = node.right

    def inorder_traversal(self):
        current = self.root# start the traversal from root node
        while current:# continues traversing until current is none, meaning its at the end of the tree
            if not current.left:
                print(current.key, end=" ")
                current = current.right
            else:  #If the current node has a left child, find its predecessor
                predecessor = self.find_predecessor(current)
                if predecessor.right == current:#If the predecessor's right child points to the current node, it means we've visited the left subtree already
                    print(current.key, end=" ")# print current nodes key and move to right child
                    current = current.right
                else:
                    predecessor.right = current
                    current = current.left

    def find_predecessor(self, node):
        current = node.left
        while current.right and not current.is_threaded_right:
            current = current.right
        return current

def test_threaded_binary_tree():
    tree = ThreadedBinaryTree()
    keys = [5, 3, 7, 2, 4, 6, 8]
    
    for key in keys:
        tree.insert(key)

    print("Inorder traversal:")
    tree.inorder_traversal()
    print()
    

if __name__ == "__main__":
    test_threaded_binary_tree()