import dsc40graph
def biggest_descendent(graph, root, value):
    for node in graph.neighbors(root):
        biggest_descendent(graph, node, value)
        if value[root] < value[node]:
            value[root] = value[node]
    return value
