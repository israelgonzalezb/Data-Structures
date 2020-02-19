"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    !! DONE
    """
    def add_to_head(self, value):
        current_head = self.head
        self.length += 1
        if current_head:
            current_head.insert_before(value)
            self.head = current_head.prev
        else:
            new_head = ListNode(value)
            self.head = new_head
            self.tail = new_head
            
            
       

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    !!! DONE
    """
    def remove_from_head(self):
        current_head = self.head
        self.head.prev = None
        if current_head.next:
            self.head = current_head.next
        else:
            self.head = None
            self.tail = None
        current_head.delete()
        self.length -= 1
        return current_head.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    !!! DONE
    """
    def add_to_tail(self, value):
        current_tail = self.tail
        if self.tail:
            self.tail.insert_after(value)
            self.tail = current_tail.next
            self.length += 1
        else:
            self.tail = ListNode(value)
            self.head = self.tail
            self.length = 1
        pass

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        current_tail = self.tail
        if current_tail.prev:
            self.tail = current_tail.prev
        else:
            self.tail = None
            self.head = None
        current_tail.delete()
        self.length -= 1
        return current_tail.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        node.delete()
        if self.head:
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if self.head == node:
            self.head = self.head.next
        node.delete()
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
        else:
            self.head = node
            self.tail = node
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if self.head != node and self.tail != node:
            node.delete()
            self.length -= 1
        elif self.length == 1:
            node.delete()
            self.head = None
            self.tail = None
            self.length -= 1
        elif self.tail == node:
            self.remove_from_tail()
        elif self.head == node:
            self.remove_from_head()
        pass
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        print("---")
        if self.length == 0:
            return None;
        elif self.length == 1:
            return self.head.value
        else:
            current_node = self.head
            current_max = current_node.value
            print(f"Current node value is {current_max}")
            for i in range(self.length):
                print(f"GET MAX: List lengths is {self.length}")
                print(f"GET MAX: Iteration {i}")
                print(f"GET MAX: current max is {current_max}")
                if current_node.next:
                    current_node = current_node.next
                    print(f"Current node value is {current_node.value}")
                    if current_node.value > current_max:
                        current_max = current_node.value
            print("---")
            return current_max
        print("---")
        pass
