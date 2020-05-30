"""
A ring buffer is a non-growable buffer with a fixed size. When the ring buffer
is full and a new element is inserted, the oldest element in the ring buffer 
is overwritten with the newest element. This kind of data structure is very 
useful for use cases such as storing logs and history information, 
where you typically want to store information up until it reaches a certain age, 
after which you don't care about it anymore and don't mind seeing it overwritten by newer data.

Implement this behavior in the RingBuffer class. RingBuffer has two methods,
`append` and `get`. The `append` method adds the given element to the buffer. 
The `get` method returns all of the elements in the buffer in a list in their given order.
It should not return any `None`
values in the list even if they are present in the ring buffer.

For example:

buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']

"""


class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DLL:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        # what if the list is empty?
        # what if the list isnt empty?
        new_node = Node(value)

        self.length += 1

        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        else:
            self.head = new_node
            self.tail = new_node

    def remove_from_head(self):
        val = self.head
        self.delete(self.head)
        return val

    def add_to_tail(self, value):
        new_node = Node(value)
        self.length += 1
        # what if the tail doesnt exits
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove_from_tail(self):
        val = self.tail
        self.delete(self.tail)
        return val

    def delete(self, node):
        # this node is being removed...
        if not self.head:
            return

        self.length -= 1

        if self.head == self.tail:
            self.head = None
            self.tail = None

        if node == self.head:
            self.head = node.next
            self.head.prev = None

        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None

        else:
            node.delete()


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.count = 0

    def append(self, item):
        # if the storage is empty it needs to be added to..
        # once it hits the capacity it needs to flush the old and insert the new

        if len(self.storage) >= self.capacity:
            self.storage.insert(self.count + 1, item)
            self.storage.pop(self.count + 0)
            self.count += 1
            if self.count > self.capacity:
                self.count = 0
            
        else:
            self.storage.append(item)

    def get(self):

        return self.storage
