'''1091. Shortest Path in Binary Matrix'''
from collections import deque
from typing import List

class Solution:
    '''Solution Class'''
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        Uses a BFS to traverse the grid and find the shortest path from the
        top left corner to the bottom right corner. If there is no path 
        from those cells then -1 is returned. The BFS is done using a queue
        and starts from the top left cell and adds any viable directions to
        take to the queue and adds those cells to the visited set so that
        we do not traverse the same cells multiple times. If we make it to
        bottom left cell then we return the length of the path which is 
        stored each time with the cells in the queue.
        Runtime: O(n) -> as we travese each cell one time
        Space: O(n) -> for the queue and the visited set
        '''
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        q = deque([(0, 0, 1)])
        visited = {(0, 0)}
        directions = [(0,-1), (0,1), (1,0), (-1,0), (-1,-1), (1,1), (-1,1), (1,-1)]
        while q:
            row, col, path_len = q.popleft()
            if row == n - 1 and col == n - 1:
                return path_len
            for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                        q.append((nr, nc, path_len + 1))
                        visited.add((nr, nc))
        return -1
