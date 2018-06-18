

def queue_game(a, x, n):
    index_element_map = dict((a[i], i) for i in range(len(a)))

    elements = [[i, a[i]] for i in range(len(a))]

    while True:
        queue = elements[(x+1):n]
        new_elements = list(reversed(elements))
        tmp = []
        new_items = []
        ni = x

        while ni > 0:
            it = new_elements.pop()
            new_items
            ni -= 1
    


def main():
    n, x = map(int, raw_input().strip().split(' '))
    elements = map(int, raw_input().strip().split(' '))
    print(elements)
    queue_game(elements, x, n)

main()