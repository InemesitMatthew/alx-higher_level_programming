#!/usr/bin/python3


class Node:
    """
    Represent a node in a singly linked list.

    Attributes:
    - data: Data stored in the node.
    - next_node: Reference to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize the Node instance.

        Parameters:
        - data: Data to be stored in the node.
        - next_node: Reference to the next node in the list.
        """
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    """
    Represent a singly linked list.

    Attributes:
    - head: Reference to the head of the list.
    """

    def __init__(self):
        """
        Initialize the SinglyLinkedList instance.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list.

        Parameters:
        - value: Value to be stored in the new node.
        """
        new_node = Node(value)
        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Return a string representation of the list.

        Returns:
        str: String representation of the list.
        """
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)

    # Output:
    # -4
    # -3
    # 1
    # 2
    # 3
    # 3
    # 4
    # 5
    # 5
    # 10
    # 12
