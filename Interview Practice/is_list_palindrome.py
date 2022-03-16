"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
def solution(l):
    stack = []
    pointer = current = l
    # Iterate through list and push items onto stack
    while current:
        stack.append(current.value)
        current = current.next
    # Pop items from stack while 
    while stack:
        character = stack.pop()
        if pointer.value != character:
            return False
        pointer = pointer.next
    return True