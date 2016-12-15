# Data-Structures

###This repo holds sample code for a number of classic data structures implemented in Python.

##Singly-Linked List in Python
- **Module:** linked_list.py
- **Tests:** test_linked_list.py
- **Resources Used:** http://greenteapress.com/thinkpython/html/chap17.html

Our list implementation supports the following methods:

- **push(val)** will insert the value ‘val’ at the head of the list
- **pop()** will pop the first value off the head of the list and return it.
- **size()** will return the length of the list
- **search(val)** will return the node containing ‘val’ in the list, if present, else None
- **remove(node)** will remove the given node from the list, wherever it might be (node must be an item in the list)
- **display()** will return a unicode string representing the list as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”


##Stack using Class Composition
- **Module:** stack.py
- **Tests:** test_stack.py
- **Resources Used:** https://codefellows.github.io/sea-python-401d5/lectures/inheritance_v_composition.html

Our stack implementation supports the following methods:

- **push(value)** - Adds a value to the stack. The parameter is the value to be added to the stack.
- **pop()** - Removes a value from the stack and returns that value. If the stack is empty, attempts to call pop should raise an appropriate Python exception class.


##Double linked list
- **Module:** doublelinkedlist.py
- **Tests:** test_doublelinkedlist.py
- **Resources Used** https://en.wikipedia.org/wiki/Doubly_linked_list

Our double linked list implementation supports the following methods:

- **push(val)** - will insert the value ‘val’ at the head of the list
- **append(val)** - will append the value ‘val’ at the tail of the list
- **pop()** - will pop the first value off the head of the list and return it.
- **shift()** - will remove the last value from the tail of the list and return it.
- **remove(val)** - will remove the first instance of ‘val’ found in the list, starting from the head. If ‘val’ is not present, it will raise an appropriate Python exception.


##Queue
- **Module:** queue.py
- **Tests:** test_queue.py
- **Resources Used** http://www.princeton.edu/~achaney/tmve/wiki100k/docs/Queue_(data_structure).html

Our queue implementation supports the following methods:

- **enqueue(value)** - adds value to the queue
- **dequeue()** - removes the correct item from the queue and returns its value (should raise an error if the queue is empty)
- **peek()** - returns the next value in the queue without dequeueing it. If the queue is empty, returns None
- **size()** - return the size of the queue. Should return 0 if the queue is empty.


#Testing Coverage:
```
Name                           Stmts   Miss  Cover   Missing
------------------------------------------------------------
src/doublelinkedlist.py           68      0   100%
src/linked_list.py                58      0   100%
src/queue.py                      17      0   100%
src/stack.py                       8      0   100%
src/test_doublelinkedlist.py     103      0   100%
src/test_linked_list.py           82      0   100%
src/test_queue.py                 55      0   100%
src/test_stack.py                 29      0   100%
------------------------------------------------------------
TOTAL                            420      0   100%


========================== 66 passed in 0.22 seconds 


---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                           Stmts   Miss  Cover   Missing
------------------------------------------------------------
src/doublelinkedlist.py           68      0   100%
src/linked_list.py                58      0   100%
src/queue.py                      17      0   100%
src/stack.py                       8      0   100%
src/test_doublelinkedlist.py     103      0   100%
src/test_linked_list.py           82      0   100%
src/test_queue.py                 55      0   100%
src/test_stack.py                 29      0   100%
------------------------------------------------------------
TOTAL                            420      0   100%


========================== 66 passed in 0.21 seconds
```
