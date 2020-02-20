from doubly_linked_list import ListNode
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        print(f"Getting {key}")
        if key in self.storage:
            self.order.move_to_front(self.storage[key])
            print(f"self.storage is now {self.storage}")
            print(f"head is {self.order.head.value}, tail is {self.order.tail.value}")
            return self.storage[key].value
        else:
            print(f"Something went wrong... key is {key} and self.storage is {self.storage}")
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # print(f"Setting key {key} with value {value}, storage is {self.storage}")
        if key in self.storage: # OVERWRITE
            self.storage[key].value = value
            self.order.move_to_front(self.storage[key])
            # print(f"Key is {key}, self.storage[key].value is {self.storage[key].value} and self.storage is now {self.storage}")
        else: # CREATE NEW KEY
            # print(f"The size of the cache is {self.size} and limit is {self.limit}")
            if self.size < self.limit:
                self.order.add_to_head(value)
                self.storage[key] = self.order.head
                self.size += 1
                # print(f"Key is {key} and self.storage is now {self.storage}")


            else: # The cache is full!
                # we need to remove the item at the tail...
                # print(f"self.storage keys are {self.storage.keys()}")
                self.order.remove_from_tail()
                for item in self.storage:
                    if self.storage[item] == self.order.tail:
                        del self.storage[item]
                        break
                        
                #del self.storage[self.order.tail]

                self.order.add_to_head(value)
                self.storage[key] = self.order.head
                # self.size += 1 # we wouldn't increment the size, because it's already at the max limit if it hit this condition

                # self.storage[key] = self.order.head.value

        pass
