def minCostConnectPoints(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    n = len(points)
    #Early return if less than 2 points
    if n < 2:
        return 0
    
    #Create adjacency matrix using Manhattan distance
    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    #Use Prim's algorithm
    #Keep track of visited nodes and minimum costs
    visited = [False] * n
    #Initialize min_costs to infinity except for starting node
    min_costs = [float('inf')] * n
    min_costs[0] = 0
    total_cost = 0

    for _ in range(n):
        #Find unvisited vertex with minimum cost
        curr_min_cost = float('inf')
        curr_vertex = -1

        for v in range(n):
            if not visited[v] and min_costs[v] < curr_min_cost:
                curr_min_cost = min_costs[v]
                curr_vertex = v
        
        #Mark current vertex as visited and add its cost
        visited[curr_vertex] = True
        total_cost += curr_min_cost

        #Update min_costs for unvisited vertices
        for next_vertex in range(n):
            if not visited[next_vertex]:
                #Calculate cost to reach next_vertex from curr_vertex
                cost = manhattan_distance(points[curr_vertex], points[next_vertex])
                min_costs[next_vertex] = min(min_costs[next_vertex], cost)
    return total_cost

    #time O(V^2)
    #space O(V)
