import sys
sys.path.append('/Users/israelgonzalez/Documents/lambda/cs/Data-Structures/queue_and_stack')

from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value is None:
            return
        if self.value is None: # check to see if tree has a root
            self.value = BinarySearchTree(value) # if there's no root, make this new value the root
        elif value >= self.value: # passed in value is greater than current node, so move right
            # ...
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        else: # otherwise, go left
            # ...
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
            
        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Base cases:
        # target found or we hit None
        if self.value == target:
            print(f"Value of the node and target are the same, value is {self.value}, target is {target}, are they equal? {self.value == target}")
            return True
        # Recursive case
        # go down left or right subtree, depending on target
        elif self.value:
            print(f"Value and target are not the same. self.value is {self.value}, target is {target}")
            if target > self.value and self.right:
                return self.right.contains(target)
            elif target < self.value and self.left:
                return self.left.contains(target)
            else:
                return False


        pass

    # Return the maximum value found in the tree
    def get_max(self):
        # RIGHT as far as you can go
        if self.right:
            return self.right.get_max()
        else:
            return self.value
        

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # Base case: 
        # Left is None or Right is None

        # Recursive case:
        # Go LEFT and RIGHT as long they are not None
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
