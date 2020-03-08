class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        current = self.head

        for _ in range(index):
            if not current:
                return -1

            current = current.next

        return current.val if current else -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        node.next = self.head

        self.head = node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        current = self.head
        if not current:
            self.head = node

        while current.next:
            current = current.next

        current.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node = Node(val)

        if index == 0:
            if self.head:
                node.next = self.head
                self.head = node
            else:
                self.head = node

            return

        current = self.head
        for _ in range(index-1):
            if not current:
                return

            current = current.next

        if current:
            node.next = current.next
            current.next = node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            if self.head:
                self.head = self.head.next
            return

        current = self.head
        for _ in range(index-1):
            if not current:
                return

            current = current.next

        if current and current.next:
            current.next = current.next.next


if __name__ == "__main__":
    list_ = MyLinkedList()
    list_.addAtIndex(0, 10)
    list_.addAtIndex(1, 20)
    list_.addAtIndex(1, 30)
    list_.deleteAtIndex(2)
    print(list_.get(1))
