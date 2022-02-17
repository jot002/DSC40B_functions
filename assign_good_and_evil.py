import dsc40graph

def assign_good_and_evil(graph):
    school_dict = {}
    index = 0
    for node in graph.nodes:
        if index % 2 == 0:
            school_dict[node] = "good"
            index += 1
        else:
            school_dict[node] = "evil"
            index += 1
    for node in graph.nodes:
        for neighbor in graph.neighbors(node):
            rival = school_dict[node]
            if school_dict[neighbor] == rival and rival == "evil":
                school_dict[neighbor] = "good"
            elif school_dict[neighbor] == rival and rival == "good":
                school_dict[neighbor] = "evil"
                
    for node in graph.nodes:
        for neighbor in graph.neighbors(node):
            rival = school_dict[node]
            if school_dict[neighbor] == rival:
                return None
    return school_dict        
    
    
