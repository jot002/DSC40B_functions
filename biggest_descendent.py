import dsc40graph
def biggest_descendent(graph, root, value, answer={}):
    answer[root] = value[root]
    for node in graph.neighbors(root):
        biggest_descendent(graph, node, value, answer)
        if answer[root] < answer[node]:
            answer[root] = answer[node]
    return answer
