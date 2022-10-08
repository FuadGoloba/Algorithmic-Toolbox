# Longest Common Subsequence of 2 sequences

# Problem - Given two sequences s1 and s2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
# Note: A subsequence of a sequence is a new sequence generated from the original sequence with some characters (can be none) deleted without changing the relative order of the remaining characters.
# A common subsequence of two sequences is a subsequence that is common to both strings.

# For example, "ace" is a subsequence of "abcde".
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:
# Input: sequence1 = [2, 7, 5], sequence2 = [2, 5]
# Output: 2 
# Explanation: The longest common subsequence is 2,5 and its length is 2.

# SOLUTION - Using Dynamic Programming (Bottom Up Solution) - O(n * m)

def longestCommonSubsequence(first_sequence, second_sequence):
    
    # Create a 2D matrix of both sequences (with one additional row and column) and initilise their values to 0
    result = [[0 for col in range(len(second_sequence) + 1)] for row in range(len(first_sequence) + 1)]
    
    # Traverse each grid of the matrix (bottom up) checking if there's a match between its row and col values
    for row in range(len(first_sequence)- 1, -1, -1):
        for col in range(len(second_sequence) - 1, -1, -1):
            # Check that the current row and col are equal and add 1 to the value at their diagonal grid
            if first_sequence[row] == second_sequence[col]:
                result[row][col] = 1 + result[row + 1][col + 1]  # The grid with a match then has a value; 1 + the value at their diagonal grid
            else:
                # The grid without match has a value; the max value of the grid to the right and the grid below
                result[row][col] = max(result[row][col + 1], result[row + 1][col])
    
    # With the bottom approach, the value at the first grid gives us the longest common subsequence of both sequences
    return result[0][0]

if __name__ == '__main__':
    n = input()
    first_sequence = list(map(int, input().split()))
    
    m = input()
    second_sequence = list(map(int, input().split()))
    
    print(longestCommonSubsequence(first_sequence, second_sequence))
    
