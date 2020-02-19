import sys
sys.path.append('/Users/israelgonzalez/Documents/lambda/cs/Data-Structures/doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()
        self.size = self.storage.length
    # We'll make the tail the part of the list where items are popped off from
    def push(self, value):
        self.storage.add_to_tail(value)
        pass

    def pop(self):
        if self.storage.length > 0:
            temp_tail = self.storage.tail
            self.storage.remove_from_tail()
            return temp_tail.value
        else:
            return None
        

    def len(self):
        return self.storage.length
        pass
