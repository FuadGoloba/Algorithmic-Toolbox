# Implementing a Naive algorithm to find the maximum product of 2 distinct numbers in a sequence of non -ve integers (o(n2))

"""Find the maximum product of two distinct numbers in a sequence of non-negative integers.
    Input: A sequence of non-negative integers
    Output: The maximum value that can be obtained by multiplying two different elements from the sequence."""
    
def max_pairwise_product_Naive(numbers):
    
    max_product = 0
    n = len(numbers)
    # Iterate through the numbers and updating max_product
    for row in range(n):
        for col in range(row + 1, n):
            max_product = max(max_product, numbers[row] * numbers[col])

    return max_product

if __name__ == "__main__":
    
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_Naive(input_numbers))