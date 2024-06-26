from binarytree import Node
import sys

def isnumber(c):
    return c >= '0' and c <= '9' # checks if its a number

class Token:# breaks up each line into a sequence of lexical components 
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        if self.value is not None:
            return f"Token({self.type}, {self.value})"
        else:
            return f"Token({self.type})"

    def __repr__(self):
        return str(self)

def lex(str): # loops over the characters and turns them into tokens
    chars = list(str)
    tokens = []

    i = 0
    while i < len(chars):
        char = chars[i]
        if isnumber(char):
            while (i+1) < len(chars) and isnumber(chars[i+1]):
                i += 1
                char += chars[i]
            tokens.append(Token("number", int(char))) 
        elif char == '+' or char == '-' or char == '*' or char == '/':
            tokens.append(Token("op", char))
        elif char == '(':
            tokens.append(Token("open_paren", None))
        elif char == ')':
            tokens.append(Token("close_paren", None))
        else:
            print("Syntax error")
            sys.exit(1)

        i += 1

    return tokens

def parse_expression(tokens): # parses the expression, 
    token = tokens.pop(0)
    if token.type == "number": # if its a number put it on the left then check for operator then parse right recursively.
        left = Node(token.value)
        if len(tokens) != 0 and tokens[0].type == "op":
            op = tokens.pop(0)
            right = parse_expression(tokens)
            return Node(op.value, left, right)
        else:
            return left
    elif token.type == "open_paren": # if its a open paren parse the inside and put it on the left, then check for operator then parse right recursively.
        inside = parse_expression(tokens)
        assert tokens.pop(0).type == "close_paren" 
        if len(tokens) != 0 and tokens[0].type == "op":
            op = tokens.pop(0)
            right = parse_expression(tokens)
            return Node(op.value, inside, right)
        else:
            return inside
    else:
        print("Syntax error")
        sys.exit(1)

def infix_to_tree(str):
    lexed = lex(str)
    return(parse_expression(lexed))

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
        raise ValueError("Invalid operator") # evaulates the nodes
    
def to_rpn(tree):
    if tree.left is not None and tree.right is not None: # if is not leaf...
        return f"{to_rpn(tree.left)} {to_rpn(tree.right)} {tree.value}"
    else:
        return tree.value # converts it to reverse polish notation
    
if __name__ == '__main__':
    tree = infix_to_tree(input("Enter the infix expression: "))
    print(tree)
    print("Evaluation: "+str(evaluate_expression_tree(tree))+"\n")
    print("As RPN: "+to_rpn(tree))


    

# Grammar
# expression := number {op expression} | open_paren expression close_paren {op expression}
# op := + | - | * | /
# number := [0-9]+
# open_paren := (
# close_paren := )
