def max_points_on_line(X, p):
    #X: A list of points, each point being a 2-tuple of integers.
    #p: A query point represented as a 2-tuple of integers.
    n = len(X)
    if n == 0:
        return 0
    if n == 1:
        return n
    max_count = 0
    point_dict = {}
    duplicate = 0
    cur_max = 0
    for point in X:
        if (p != point):
            if p[0] != point[0]:
                #slope formula
                slope = float(point[1]-p[1]) / float(point[0]-p[0])
            else:
                slope = "straight up"
            point_dict[slope] = point_dict.get(slope,0)+1
            cur_max = max(cur_max, point_dict[slope])
        else:
            duplicate = duplicate + 1
            
    max_val = max(max_count, cur_max + duplicate)
 
    return max_val
