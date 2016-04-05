__author__ = 'sriram'


def get_removable_edges(graph):
    edges = 0
    for k, v in graph.iteritems():
        if (len(v) + 1) % 2 == 0:
            edges += 1
    return edges


def even_tree(c, p):
    child_parent_map = {}
    parent_child_map = {}
    index = 0
    for e in p:
        if e in c:
            if e not in parent_child_map:
                parent_child_map[e] = []
            ch = c[index]
            if ch not in child_parent_map:
                child_parent_map[ch] = []
            child_parent_map[ch].append(e)
            parent_child_map[e].append(ch)
        index += 1

    for e in child_parent_map:
        for parent in child_parent_map[e]:
            if parent in child_parent_map:
                child_parent_map[e].extend(child_parent_map[parent])
                for pa in child_parent_map[parent]:
                    if e not in parent_child_map[pa]:
                        parent_child_map[pa].append(e)

    return get_removable_edges(parent_child_map)


def main():
    (n, m) = map(int, raw_input().strip().split(" "))
    child_nodes = []
    parent_nodes = []
    for a0 in xrange(m):
        (c, p) = map(int, raw_input().strip().split(" "))
        child_nodes.append(c)
        parent_nodes.append(p)
    print even_tree(child_nodes, parent_nodes)

if __name__ == '__main__':
    main()
