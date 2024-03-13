# Reversing a List:
### Summary 
- To reverse a list of integers, read each number from the array starting at the first index and push it onto a stack.
### Implementation:
 - Utilizes a stack to push elements from the list and then pop them back into the list in reverse order.

# Parentheses Checker:
### Summary: 
- Makes sure that  an expression has balanced parenthesis using a stack to keep track.
### Implementation: 
- Utilizes a stack to push opening parentheses and pop to match with closing parentheses.

# Infix to Postfix Conversion:
### Summary: 
- Converts infix expressions to postfix using a stack to manage operators.
### Implementation: 
- Utilizes a stack to temporarily store operators according to precedence rules.
# Evaluation of Postfix Expression:
### Summary 
- Evaluates postfix expressions using a stack to store operands and perform operations.
### Implementation
- Utilizes a stack to push operands and perform operations based on encountered operators.

# Infix to Prefix Conversion:
### Summary: 
- Converts infix expressions to prefix using a stack. A postfix operation does not even follow the rules of
operator precedence
### Implementation: 
- Utilizes a stack to reverse the infix expression, convert to postfix, and then reverse again to obtain prefix.  Every character of the postfix
expression is scanned from left to right. If the character encountered is an operand, it is pushed
on to the stack.

# Evaluation of Prefix Expression:
### Summary
- Evaluates prefix expressions using a stack to store operands and perform operations.
### Implementation
- Utilizes a stack to reverse the prefix expression, convert to postfix, and then evaluate.

# Recursion:
### Summary
- A recursive function solves a smaller version of its job by calling itself until it reaches a final call that doesn't need to be called again. Recursive functions use the system stack to keep the return address and local variables of the caller function, as they call themselves repeatedly.Solves problems by dividing into subproblems and calling itself. 
- Recursion is a technique that breaks a problem into one or more sub-problems.

### Implementation
- Uses a call stack for each recursive call and a base case to end recursion.

# Tower of Hanoi:
### Summary
-  Moves disks from one peg to another adhering to specific rules.
- Main applicaiton sof recursion.
- Recursive programs may incur significant run-time overhead. Implementing a recursive solution involves balancing the time spent on construction and maintenance with the cost of operating time and memory space. 

### Implementation
- Uses recursion and stack frames to move disks efficiently.