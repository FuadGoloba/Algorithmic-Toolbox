#Majority Element Problem - 
    #Problem - Check whether a given sequence of numbers contains an element that appears more than half of the times.
    # Input: A sequence of n integers.
    # Output: 1, if there is an element that is repeated more than n=2 times, and 0 otherwise.

import collections

# Naive Algorithm
def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


# Using Divide and Conquer - if we divide an array into two halves and recursively fidn the majority element of left and right halves, we can easily determine the overall majority element in linear time
def majority_element(elements, lo=0, hi=None):
    assert len(elements) <= 10 ** 5
    # Recursively split the array in halves; the majority element of the entire array is the majority element in one of the halves
    def majority_element_recurse(lo, hi):
        # Base Case - an array of size 1 has only that element as its majority element
        if lo == hi:
            return elements[lo] # return the only element in array

        # Recurse on the 2 halves of the split
        mid = (hi - lo)//2 + lo
        left = majority_element_recurse(lo, mid) # recursively find the majority element in the left half
        right = majority_element_recurse(mid+1, hi) # recursively find majority element in right half

        # If both halves have the same element as their individual majority element, then we have found the majority element of the combined array
        if left == right:
            return left

        # Otherwise we count the occurrence of the majority element of each halves in the entire array and return the highest
        #element_dict = collections.Counter(elements[lo:hi+1])
        #left_count = element_dict.get(left)
        #right_count = element_dict.get(right)

        # Otherwise we count the occurrence of the majority element of each halves in the entire array and return the highest
        left_count = sum(1 for num in range(lo, hi+1) if elements[num] == left)
        right_count = sum(1 for num in range(lo, hi) if elements[num] == right)
        
        return left if left_count > right_count else right

    #return majority_element_recurse(lo=0, hi=len(elements) - 1)
    majority_element = majority_element_recurse(lo=0, hi=len(elements) - 1)

    # Get count of majority element and check if appears more than half of the times
    count = collections.Counter(elements)
    return 1 if  count[majority_element] > len(elements) // 2 else 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))

