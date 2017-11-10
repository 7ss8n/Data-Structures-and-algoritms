"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    i=0
    if head==None:
        return False
    current=head
    while current!=None and i<100:
        current=current.next
        i=i+1
    if current==None:
        return False
    else:
        return True
    

    
  
