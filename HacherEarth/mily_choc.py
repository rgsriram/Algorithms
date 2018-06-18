
def construct_box(chocolates):
    box = dict()
    no = 1
    last_index = 0

    for n in chocolates:
        for i in range(last_index+1, n+last_index+1):
            box[i] = no

        no += 1
        last_index = n

    return box

if __name__ == '__main__':
    n = int(raw_input().strip())
    chocolates = map(int, raw_input().strip().split(' '))
    box = construct_box(chocolates)

    q = int(raw_input().strip())

    for a0 in range(q):
        q = int(raw_input().strip())
        print box.get(q, -1)
