def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    islands = 0

    def dfs(row, col):
        #Check boundary conditions and if current cell is land
        if (row < 0 or row >= rows or
            col < 0 or col >= cols or
            grid[row][col] != '1'):
            return
        
        #Mark current land cell as visited by changing to '2'
        grid[row][col] = '2'

        #Recursively check all adjacent cells
        dfs(row + 1, col) #Down
        dfs(row - 1, col) #Up
        dfs(row, col + 1) #Right
        dfs(row, col - 1) #Left

    #Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                dfs(i, j) #Start dfs from each unvisited land cell
                islands += 1
    return islands

    #time O(m * n)
    #space O(m * n)
