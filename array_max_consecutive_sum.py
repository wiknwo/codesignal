def calculateSubstringsLengthK(s, k):
    '''Calculate substrings of length k
    
    Args:
        s(int): List of integers
        k(int): Size of substring
    
    Return:
        substrings of size k
    
    Raises
    '''
    substrings, index = [], 0
    while index + k <= len(s):
        substrings.append(s[index:index + k])
        index += 1
    return substrings

def arrayMaxConsecutiveSum(inputArray, k):
    '''Find maximal possible sum of k consecutive elements in list of integers
    
    Args:
        intputArray(int): List of integers
        k: Number of consecutive elements
    
    Return
        Maximum sum of k consecutive elements
    
    Raises:
    '''
    max_consecutive_sum = -sys.maxsize
    substrings_of_length_k = calculateSubstringsLengthK(inputArray, k)
    for substring in substrings_of_length_k:
        max_consecutive_sum = max(sum(substring), max_consecutive_sum)
    return max_consecutive_sum

