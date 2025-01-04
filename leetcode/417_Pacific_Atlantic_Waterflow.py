from collections import deque

def pacificAtlantic(heights):
    """
    :type heights: List[List[int]]
    :rtype: List[List[int]]
    """
    if not heights or not heights[0]:
        return []
    
    m, n = len(heights), len(heights[0])

    #Initialize sets to track cells that can reach each ocean
    pacific = set()
    atlantic = set()

    def bfs(queue, reachable):
        """
        BFS from ocean edges to find all reachable cells.
        Water flows from higher/equal elevation to lower elevation.
        """
        directions = (1,0), (-1,0), (0,1), (0,-1)

        while queue:
            row, col = queue.popleft()

            #Check all 4 directions
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
            
                #Check if the new position is valid and not visited.
                if (new_row, new_col) in reachable:
                    continue
                
                if (new_row < 0 or new_row >= m or
                    new_col < 0 or new_col >= n):
                    continue
                
                #Water can only flow from higher/equal elevation
                #to lower elevation
                if heights[new_row][new_col] < heights[row][col]:
                    continue
                
                reachable.add((new_row, new_col))
                queue.append((new_row, new_col))

    #Initialize queues with cells adjacent to oceans
    pacific_queue = deque()
    atlantic_queue = deque()

    #Add top and left edges (Pacific)
    for i in range(m):
        pacific_queue.append((i, 0))
        pacific.add((i, 0))
        atlantic_queue.append((i, n - 1))
        atlantic.add((i, n - 1))
    
    for j in range(n):
        pacific_queue.append((0, j))
        pacific.add((0, j))
        atlantic_queue.append((m - 1, j))
        atlantic.add((m - 1, j))
    
    #Run BFS from both oceans
    bfs(pacific_queue, pacific)
    bfs(atlantic_queue, atlantic)

    #Find intersection of cells that can reach both oceans
    result = list(pacific & atlantic)

    #Convert to required format
    return [[r, c] for r, c in result]

    #time O(m * n)
    #space O(m * n)
