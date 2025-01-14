class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = ''

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        #Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
            node.word = word
        
        rows, cols = len(board), len(board[0])
        result = set()

        def dfs(row, col, node):
            #Base cases:
            if (row < 0 or col < 0 or
            row >= rows or col >= cols or
            board[row][col] not in node.children):
                return

            char = board[row][col]
            curr_node = node.children[char]

            #If we found a word, add it to result
            if curr_node.is_end:
                result.add(curr_node.word)
            
            #Mark cell as visited
            board[row][col] = "#"

            #Explore all 4 directions
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                dfs(new_row, new_col, curr_node)

            #Restore the cell
            board[row][col] = char

        #Start dfs from each cell
        for i in range(rows):
            for j in range(cols):
                dfs(i,j,root)
        return list(result)
