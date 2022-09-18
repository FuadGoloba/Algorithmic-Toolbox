def selection_sort(arr):

    # Loop through each element of the array to the the index of the minimum element
    for i in  range(len(arr)):
        min_index = i
        # loop through the rest of the array to update the index of the minimum element
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        # Swap the posirion of the minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == '__main__':

    input_n = int(input('Enter size of array:' ))
    input_arr = list(map(int, input('Enter elements of the array with a space between each :' ).split()))
    assert len(input_arr) == input_n
    print(selection_sort(input_arr))