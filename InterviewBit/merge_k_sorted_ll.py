import heapq
from linkedin_list import LinkedList


class Node(object):
    def __init__(self, index, arr, next, value, size):
        self.index = index
        self.arr = arr
        self.next = next
        self.value = value
        self.size = size

    def __cmp__(self, other):
        return cmp(self.value, other.value)


def add_to_heap(heap, node):
    heapq.heappush(heap, node)


def merge_sorted_ll(lists):
    heap = []
    linkedlist = LinkedList()

    i = 0
    size = 0

    while i < len(lists):
        ll = lists[i]
        cur_size = linkedlist.size(ll)
        size += cur_size

        node = Node(0, i, ll.next, ll.data, cur_size)
        add_to_heap(heap, node)

        i += 1

    result = None
    j = 0

    linkedlist = LinkedList()

    while len(heap):
        n = heapq.heappop(heap)
        result = linkedlist.insert(result, n.value)
        new_index = n.index

        if new_index < n.size:
            add_to_heap(heap, Node(new_index, n.arr, n.next.next, n.next.data, n.size))

        j += 1

    linkedlist.print_list(result)


data = [
    [1, 7, 29,30],
    [2, 5, 6],
    [8, 9, 10],
]

results = []

l = LinkedList()
head = None

for _list in data:
    for each in _list:
        head = l.insert(head, each)

    results.append(head)
    head = None

merge_sorted_ll(results)



