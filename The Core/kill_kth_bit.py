"""
In the given number n the kth bit from the right was initially set to 0, 
but its current value might be different. It's now up to you to write a 
function that will change the kth bit of n back to 0.
https://stackoverflow.com/questions/40483029/java-setting-a-distinct-bit-of-an-integer-to-zero
"""
def solution(n, k):
    return n & ~(1 << (k - 1))
