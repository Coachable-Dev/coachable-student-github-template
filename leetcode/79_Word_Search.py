def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    if not board or not word:
        return False
    
    m, n = len(board), len(board[0])

    def dfs(row, col, index):
        #Base case- if we've matched all characters in word
        if index == len(word):
            return True
        #Check if current character is out of bounds or
        #character doesn't match
        if (row < 0 or row >= m or
            col < 0 or col >= n or
            board[row][col] != word[index]):
            return False
        
        #Store original character and mark cell as visited
        temp = board[row][col]
        board[row][col] = '#'

        #Try all four directions
        result = (dfs(row + 1, col, index + 1) or #Down
                dfs(row - 1, col, index + 1) or #Up
                dfs(row, col + 1, index + 1) or #Right
                dfs(row, col - 1, index + 1)) #Left
        
        #Restore the cell
        board[row][col] = temp

        return result
    
    #Try each cell as starting point
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                if dfs(i, j, 0):
                    return True
    return False

    #time O(m * n * 3^L)
    #space O(L)
