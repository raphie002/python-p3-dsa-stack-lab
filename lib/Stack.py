# lib/Stack.py
class Stack:
    """
    Implements a Stack data structure with a fixed size limit.
    """

    def __init__(self, items=[], limit=100):
        """
        Initializes the stack with an optional list of items and a size limit.
        """
        # Ensure 'items' is treated as a copy for internal storage
        self.items = list(items)
        self.limit = limit

    def isEmpty(self):
        """
        Checks if the stack is empty.
        Returns: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Adds an item to the top of the stack (the end of the list).
        If the stack is at its limit, it behaves according to the test:
        it checks if the stack is full, and if so, it doesn't push,
        but the test case suggests an unusual behavior where a push is
        attempted even when full, and the stack size remains 1.

        Based on the `test_full` case:
        If full, it seems to pop the bottom element (first element) and then push the new one,
        but the test implies it might just **fail to push** OR it's a fixed-size stack where
        a push operation when full doesn't change the state based on the provided test.

        Let's assume standard behavior: if full, it fails to push and returns.
        However, the `test_full` is highly irregular:
        stk.push(1) -> size 1
        stk.push(2) -> size 1, pop() returns 1.
        This implies: If full, the push fails/does nothing *but* the test expects a subsequent pop to still return the original element 1.
        
        The only way to pass `test_full` exactly is to ensure that when full (size == limit), 
        a push *does nothing* to the stack's contents, and the size remains unchanged.
        
        Let's implement the **standard push** first:
        """
        if self.full():
            # Based on standard stack behavior and the most direct interpretation
            # of the test_full (push doesn't increase size beyond limit).
            return
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the item at the top of the stack (the end of the list).
        Returns: The top item, or None if the stack is empty.
        """
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        """
        Returns the item at the top of the stack without removing it.
        Returns: The top item, or None if the stack is empty.
        """
        if self.isEmpty():
            return None
        return self.items[-1]
    
    def size(self):
        """
        Returns the current number of items in the stack.
        """
        return len(self.items)

    def full(self):
        """
        Checks if the stack has reached its size limit.
        Returns: True if size == limit, False otherwise.
        """
        return self.size() >= self.limit

    def search(self, target):
        """
        Searches for the target element and returns its distance from the top of the stack.
        The top element is at distance 0, the next is 1, and so on.
        If the element is not found, returns -1.
        
        The search is done from the top (end of the list) to the bottom.
        
        Example: [5, 6, 7, 8, 9, 10] (10 is top)
        search(10) -> index 5, size 6, distance (6-1-5) = 0
        search(9) -> index 4, size 6, distance (6-1-4) = 1
        search(5) -> index 0, size 6, distance (6-1-0) = 5
        
        Distance = size - 1 - list_index
        """
        try:
            # Find the index of the target element. Python's list.index() finds the first match.
            list_index = self.items.index(target)
            
            # The distance from the top (last element) is calculated
            distance = self.size() - 1 - list_index
            return distance
        except ValueError:
            # list.index() raises ValueError if the target is not found
            return -1