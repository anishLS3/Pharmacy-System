class Node:
    """
    A node in a linked list.
    """

    def __init__(self, data):
        """
        Initialize a new node with the given data.
        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list implementation.
    """

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        self.size = 0

    def add(self, data):
        """
        Add a new node with the given data to the end of the linked list.
        Args:
            data: The data to be stored in the new node.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def remove(self, data):
        """
        Remove the first occurrence of the node with the given data from the linked list.
        Args:
            data: The data to be removed from the linked list.
        """
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        self.size -= 1

    def display(self):
        """
        Display the contents of the linked list.
        """
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def get_head(self):
        """
        Get the head node of the linked list.
        Returns:
            The head node.
        """
        return self.head

    def clear(self):
        """
        Clear the linked list by removing all nodes.
        """
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None
