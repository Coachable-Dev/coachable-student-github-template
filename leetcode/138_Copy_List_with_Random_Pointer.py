'''138. Copy List with Random Pointer'''
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    '''Solution Class'''
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        A dictionary is created with a {None:None} value in place so that
        if nodes point to None there is a value of none that maps to it.
        Then we traverse the linked list and add the orginal node as a key
        in the dictionary to a new node as its value that will be the copy.
        The after that we again travese the linked list and starting with 
        the head we use that key to get the copy as a value and then update
        that copy with the next and random fields based on the now 
        completed dictionary. Then we return the haed of the new list which
        is the value of the head of the original list in the dictionary.
        Runtime: O(n) -> traversing the linked list
        Space: O(n) -> the copy of the new list
        '''
        list_dict = {None:None}
        cur = head
        while cur:
            list_dict[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            copy = list_dict[cur]
            copy.next = list_dict[cur.next]
            copy.random = list_dict[cur.random]
            cur = cur.next
        return list_dict[head]
        