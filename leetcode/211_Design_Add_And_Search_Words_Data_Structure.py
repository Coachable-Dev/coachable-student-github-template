class TrieNode(object):
    def __init__(self):
        #Use dict to store child nodes
        self.children = {}
        #Flag to mark end of word
        self.is_end = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize the WordDictionary with a root TrieNode
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        Add a word to the data structure
        """
        node = self.root
        #Traverse the trie, creating new nodes as needed.
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        Search for a word in the data structure.
        The word can contain dots '.' which matches any character.
        """
        def dfs(node, i):
            #Base case: reached end of word
            if i == len(word):
                return node.is_end
            
            #Current character is a dot
            if word[i] == '.':
                #Try all possible characters at this position
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
                
            #Current character is a letter
            if word[i] not in node.children:
                return False
            
            return dfs(node.children[word[i]], i + 1)
        
        return dfs(self.root, 0)
        
        #time O(n)
        #space O(n)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
