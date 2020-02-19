import sys
sys.path.append('/Users/israelgonzalez/Documents/lambda/cs/Data-Structures/doubly_linked_list')

from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()
    # We'll make the head the front of the queue, so things will be popped from the head
    def enqueue(self, value):
        self.storage.add_to_tail(value)
        pass

    def dequeue(self):
        if self.len() > 0:
            temp_head = self.storage.head
            self.storage.remove_from_head()
            return temp_head.value
        else:
            return None

    def len(self):
        return self.storage.length
        pass
