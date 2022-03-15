# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
# 
# Remove all nodes from linked list whose value is equal to k
def solution(l, k):
    # If the node we want to delete is the head node
    # we skip over nodes until we reach one that is
    # not equal to k
    while l is not None and l.value == k:
        l = l.next
    
    current = l # Set current to the new head
    while current is not None and current.next is not None:
        if current.next.value == k:
            current.next = current.next.next
        else:
            current = current.next
    return l