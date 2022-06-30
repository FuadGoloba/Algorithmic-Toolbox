# Implementing a Fast algorithm to find the maximum product of 2 distinct numbers in a sequence of non -ve integers (o(n))

"""Find the maximum product of two distinct numbers in a sequence of non-negative integers.
    Input: A sequence of non-negative integers
    Output: The maximum value that can be obtained by multiplying two different elements from the sequence."""
    
def max_pairwise_product_Fast(numbers):
    
    """Find the largest and second largest numbers and multiply to get the max pairwise product"""
    
    # Gettimg the max number in the array and its index
    first_max = max(numbers)
    first_max_index = numbers.index(first_max)
    
    # Getting the 2nd max number
    second_max = 0
    for index in range(len(numbers)):
        # skipping the index of first max number
        if index != first_max_index:
            second_max = max(numbers[index], second_max)
            
    return (first_max * second_max)

if __name__ == "__main__":
    
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_Fast(input_numbers))    