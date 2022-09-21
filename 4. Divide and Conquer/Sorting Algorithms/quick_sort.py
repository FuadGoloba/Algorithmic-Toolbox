def quicksort(array, left_ptr, right_ptr):

    # Base case; if there's only one element in the array, we return the array
    if left_ptr >= right_ptr:
        return array

    # Partition the array to keep the pivot element at it's rightful index and return that index
    partitioned_ptr = partition(array, left_ptr, right_ptr)
    # Recursively call Quick sort on the left side and right side of the partition
    quicksort(array, left_ptr, partitioned_ptr - 1)
    quicksort(array, partitioned_ptr + 1, right_ptr)


# Partition function to move a pivot element to its rightful position such that elements smaller than pivot element are on the left side and elements larger than the pivot element are on the right side
def partition(array, left_ptr, right_ptr):

    # using the first element of the array as the pivot element
    pivot = array[left_ptr]
    partition_ptr = left_ptr # Initialising the partition ppinter to start at the begining of the array

    # Traverse the rest of the array, swapping smaller elements than the pivot to the front/left and larger elements to the back/right
    for idx in range(left_ptr + 1, right_ptr+1):
        if array[idx] <= pivot:
            partition_ptr += 1 # moving the partition pointer at each step we find a smaller element so we can swap with the element at the current index.
            # Swap elements at current idx with element at partition pointer
            array[partition_ptr], array[idx] = array[idx], array[partition_ptr]

    # At the end of the traversal, we put the pivot element at it's rightful position ; which is as the index pointer of the last partition element
    array[left_ptr], array[partition_ptr] = array[partition_ptr], array[left_ptr]
    return (partition_ptr)

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    quicksort(elements, 0, len(elements) - 1)
    print(elements)


