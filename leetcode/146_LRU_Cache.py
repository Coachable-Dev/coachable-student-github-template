class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        #Hash map to store key -> Node mapping
        self.cache = {}

        #Dummy head and tail nodes to simplify ops
        self.head = Node
        self.tail = Node
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove_node(self, node):
        """
        Remove a node from the linked list

        :param node: Node to be removed
        """
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_to_head(self, node):
        """
        Add a node right after the head (most recently used)
        :param node: Node to be added
        """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        Get the value for a given key and mark it as
        most recently used

        :param key: Key to retrieve
        :return: Value associated with the key, or 
        -1 if not found
        """
        if key in self.cache:
            #Move the accessed node to the head
            node = self.cache[key]
            self._remove_node(node)
            self._add_to_head(node)
            return node.value
        return -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        Put a key-value pair into the cache

        :param key: Key to insert or update
        :param value: Value to associate with key
        """
        if key in self.cache:
            #Update existing node
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_to_head(node)
        else:
            #Create new node
            node = Node(key, value)

            #Check if cache is at capacity
            if len(self.cache) == self.capacity:
                #Remove least recently used(tail.prev)
                lru_node = self.tail.prev
                self._remove_node(lru_node)
                del self.cache[lru_node.key]
            
            #Add new node
            self._add_to_head(node)
            self.cache[key] = node
        
        #time- get O(1) lookups
        #time- put O(1) lookups

        #space O(capacity)
