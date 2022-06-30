# Implementing a Fast algorithm to find the maximum product of 2 distinct numbers in a sequence of non -ve integers (o(n))

"""Find the maximum product of two distinct numbers in a sequence of non-negative integers.
    Input: A sequence of non-negative integers
    Output: The maximum value that can be obtained by multiplying two different elements from the sequence."""
    
def max_pairwise_product_Fast(numbers):
    
    """Find the largest and second largest numbers and multiply to get the max pairwise product"""
    
    # Gettimg the index of max element in array
    n = len(numbers)
    
    first_max_index = 1
    for index in range(n):
        if numbers[index] > numbers[first_max_index]:
            first_max_index = index
    # Swapping the index of last element and max element in array in order to find index of second max element
    numbers = swap(numbers, n-1, first_max_index)
    
    # Getting the index of second max element in array skipping the first max element
    second_max_index = 1
    for index in range(n-1):
        if numbers[index] > numbers[second_max_index]:
            second_max_index = index
    # Swapping the index of last element and max element in array
    numbers = swap(numbers, n-2, second_max_index)
    
    return (numbers[n-1] * numbers[n-2])


def swap(arr,last_index,max_index):
    
    """A function that swaps index of last element and max element in an array
        arr: array containing elements
        last_index: index of last element in array
        max_index: index of maximum element in array"""
    
    temp = arr[last_index]
    arr[last_index] = arr[max_index]
    arr[max_index] = temp
    return arr
  
    
if __name__ == "__main__":
    
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_Fast(input_numbers))     