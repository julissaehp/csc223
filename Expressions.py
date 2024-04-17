class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def evaluate_expression_tree(root):
    # If the root is None, return 0
    if not root:
        return 0
    
    # If the root is a leaf node (operand), return its value
    if not root.left and not root.right:
        return int(root.value)
    
    # Recursively evaluate left and right subtrees
    left_value = evaluate_expression_tree(root.left)
    right_value = evaluate_expression_tree(root.right)
    
    # Perform operation based on the value of the root node
    if root.value == '+':
        return left_value + right_value
    elif root.value == '-':
        return left_value - right_value
    elif root.value == '*':
        return left_value * right_value
    elif root.value == '/':
        return left_value / right_value
    else:
        raise ValueError("Invalid operator")





root = TreeNode('-')
root.left = TreeNode('/')
root.right = TreeNode('+')
root.left.left = TreeNode('5')
root.left.right = TreeNode('4')
root.right.left = TreeNode('100')
root.right.right = TreeNode('20')

result = evaluate_expression_tree(root)
print("Result:", result)
# Evaluate the expression tree
