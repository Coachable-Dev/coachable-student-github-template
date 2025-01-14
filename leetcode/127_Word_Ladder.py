from collections import deque, defaultdict

def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    #If endWord not in wordList, no transformation sequence exists
    if endWord not in wordList:
        return 0
    
    #Create a dictionary to store pattern -> words mapping
    pattern_to_words = defaultdict(list)

    #Add beginWord to wordList for pattern generation
    wordList.append(beginWord)

    #Generate patterns for each word
    for word in wordList:
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i + 1:]
            pattern_to_words[pattern].append(word)
    
    #Remove beginWord from wordList as it's not needed anymore
    wordList.pop()

    #Create a queue for BFS and a set to keep track of visited words
    queue = deque([(beginWord, 1)]) # (word, distance)
    visited = {beginWord}

    #BFS
    while queue:
        current_word, distance = queue.popleft()
        #If we found the endWord, return the distance
        if current_word == endWord:
            return distance
        
        #Generate all possible patterns for current word
        for i in range(len(current_word)):
            pattern = current_word[:i] + '*' + current_word[i + 1:]

            #Check all words that match this pattern
            for neighbor in pattern_to_words[pattern]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))
    
    #If we get here, no transformation sequence exists
    return 0

    #time O(N * L * 26) N = number of words in list.
    # L = length of each word.
    #26 is the possible number of letters at each position

    #space O(N * L) for storing of the dictionary and visited set.
