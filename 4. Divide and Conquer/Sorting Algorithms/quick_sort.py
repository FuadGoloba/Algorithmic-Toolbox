from random import randint

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


# --------------------------------------------Randomized QUICK SORT 3 WAY ----------------------------------------------------------------------------#

def partition_3_way(arr, left_ptr, right_ptr):

    # Idea - We will traverse the array and at an index with an element less than the pivot, we swap this element and the pivot and increment the lt ptr, and move to the next index
    # If we are at an index with an element equal to the pivot, we do nothing and move to the next index
    # If we are at an index with an element greater than the pivot, then we swap this element with the gt ptr and decrement gt ptr to move to the element before it
    # We do this until only when our current index is greater than gt ptr (i.e when we know we have all larger elements to the right)

    pivot = arr[left_ptr] # Pivot element is the first element of the array
    lt = left_ptr   # Initialise a less than pointer to start of the array
    gt = right_ptr # Initialise a greater than pointer at the last element of the array
    idx = lt + 1 # index pointer to traverse the array

    while idx <= gt:
        # Check for elements less than the pivot and swap
        if arr[idx] < pivot:
            arr[idx], arr[lt] = arr[lt], arr[idx]
            lt += 1
            idx += 1

        # Check for elements greater than the pivot and swap
        elif arr[idx] > pivot:
            arr[idx], arr[gt] = arr[gt], arr[idx]
            gt -= 1

        # Check for elements equal to the pivot and move to the next pointer
        else:
            idx += 1

    return lt, gt

def randomized_quicksort_3_way(arr, left_ptr, right_ptr):

    if left_ptr >= right_ptr:
        return arr

    # Randomize the selection of pivot 
    random_element = randint(left_ptr, right_ptr)

    # Swap random element with left ptr
    arr[left_ptr], arr[random_element] = arr[random_element], arr[left_ptr]

    # Partition array to get elements less than pivot and elements greater than pivot
    lt, gt = partition_3_way(arr, left_ptr, right_ptr)

    # Recurse the halves of the array
    randomized_quicksort_3_way(arr, left_ptr, lt -1)
    randomized_quicksort_3_way(arr, gt + 1, right_ptr)
    


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quicksort_3_way(elements, 0, len(elements) - 1)
    print(*elements)


                                             