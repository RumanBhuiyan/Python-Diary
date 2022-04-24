"""
    Finding the middle element of singly linked list
"""

class Node:
    def __init__(self, value = None):
        self.data =value
        self.next = None

class LinkedList:
    def __init__(self, values=[]):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.current_node = self.head

        if len(values):
            for node_value in values:
                new_node = Node(node_value)
                self.current_node.next = new_node
                new_node.next = self.tail
                self.current_node = new_node
        
    def show_items(self, head):
        temp_node = head.next
        while temp_node != self.tail:
            print(temp_node.data, end=' ')
        print()

ll1 = LinkedList([1,2,3,4,5])
ll2 = LinkedList([1,2,3,4,5,6])

ll1.show_items()
