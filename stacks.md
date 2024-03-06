## Intro
- Stacks stores its elements in an ordered manner
- You can add/ remove and element but only from the topmost position.
- LIFO = Last in first out
- Element that was inserted last is the first one to be taken out.
- Stacks are used for function calls
- To keep track of the stack the function system stack or call stack is used.


## Array Representation of stacks
- Every stack has a variable called TOP: used to store the topmost element of the stack
- MAX is used to store the maximum number of elements that the stack can hold
- If TOP = NULL, then it indicates that the stack is empty and if TOP = MAX–1, then the stack is full.


## Operations on a stack
- suports three operations: push, pop, and peek.
- Push = adds element to top
- pop= removes the element from the top
- peek= returns the value of topmost element
### Push Operation
- Used to insert element into stack
- First you have to check to see if the stack is full so check if TOP = MAX-1
- If it is full and you add there will be an overflow message
### Pop Operation
- Used to delete topmost element
- Before deleting, check if TOP = NULL because if the stack is empty no deletions can be done
- If you delete and its epty there will be an underflow message
### Peek Operation
- Returns the value of the topmost element without deleting it from the stack

- new() returns a stack
popoff(push(v, S)) = S
top(push(v, S)) = v
- isEmpty(S) may be defined with the following additional axioms.

isEmpty(new()) = true
isEmpty(push(v, S)) = false
