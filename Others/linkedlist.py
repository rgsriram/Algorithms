class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, head, element):

        if not head:
            head = Node(element)
            return head

        temp = head

        while temp.next is not None:
            temp = temp.next

        temp.next = Node(element)

        return head

    def print_list(self, head):

        while head is not None:
            print(head.data),
            print('->'),
            head = head.next

        print()