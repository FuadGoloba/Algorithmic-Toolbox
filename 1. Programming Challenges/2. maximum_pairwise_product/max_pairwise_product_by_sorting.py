# Implementing a Fast algorithm to find the maximum product of 2 distinct numbers in a sequence of non -ve integers (o(nlogn))

"""Find the maximum product of two distinct numbers in a sequence of non-negative integers.
    Input: A sequence of non-negative integers
    Output: The maximum value that can be obtained by multiplying two different elements from the sequence."""
    
def max_pairwise_product_by_sorting(numbers):
    
    numbers.sort()
    n = len(numbers)
    return (numbers[n-1] * numbers[n-2])

if __name__ == "__main__":
    
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_by_sorting(input_numbers))  