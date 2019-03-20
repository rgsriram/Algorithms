import heapq

from linkedlist import LinkedList


class Node(object):
    def __init__(self, ll_node, arr):
        self.ll_node = ll_node
        self.arr = arr

    def __cmp__(self, other):
        return cmp(self.ll_node.data, other.ll_node.data)


def add_to_heap(heap, node):
    heapq.heappush(heap, node)


def merge_sorted_ll(*lists):
    heap = []

    for i in range(len(lists)):
        print(i, lists[i])

        if lists[i]:
            add_to_heap(heap, Node(lists[i], i))

    i = 0

    result = None
    linkedlist = LinkedList()

    while len(heap):
        node = heapq.heappop(heap)
        result = linkedlist.insert(result, node.ll_node.data)

        new_index = node.ll_node.next

        if new_index:
            add_to_heap(heap, Node(new_index, node.arr))

        i += 1

    return result


def print_ll(head):
    current = head

    while current is not None:
        print(current.data)
        current = current.next



# data = [
#     [1, 7, 29,30],
#     [2, 5, 6],
#     [8, 9, 10],
# ]


data = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6],
]

data = [
    []
]

results = []

l = LinkedList()
head = None

for array in data:
    l = LinkedList()
    head = None

    for each in array:
        head = l.insert(head, each)

    results.append(head)


# print(results)
#
# for res in results:
#     while res is not None:
#         print(res.data)
#         res = res.next

print_ll(merge_sorted_ll(*results))