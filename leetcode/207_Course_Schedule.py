def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    # Build adjacency list representation of the graph
    graph = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        graph[course].append(prereq)
    
    # Track visited nodes for cycle detection
    # 0 = unvisited, 1 = visiting (in current DFS path), 2 = visited
    visited = [0] * numCourses
    
    def hasCycle(course):
        # If we encounter a node that's being visited, cycle found
        if visited[course] == 1:
            return True
        # If we've already fully explored this node, no cycle here
        if visited[course] == 2:
            return False
        
        # Mark as being visited
        visited[course] = 1
        
        # Check all prerequisites
        for prereq in graph[course]:
            if hasCycle(prereq):
                return True
        
        # Mark as fully visited
        visited[course] = 2
        return False
    
    # Check for cycles starting from each unvisited course
    for course in range(numCourses):
        if visited[course] == 0:
            if hasCycle(course):
                return False
    
    return True

    #time O(V + E)
    #space O(V)
