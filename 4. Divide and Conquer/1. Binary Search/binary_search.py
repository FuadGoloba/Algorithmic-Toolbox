# python3

#Sorted Array Search Problem with Binary Search
#      Search a key in a sorted array of keys.
#           Input: A sorted array K = [k0; : : : ;kn􀀀1] of distinct integers (i.e., k0 < k1 <... < kn-1) and an integer q.
#           Output: Check whether q occurs in K.

import os
import sys
os.environ['OPENBLAS_NUM_THREADS'] = '1'

def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):
    assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4

    min_index, max_index = 0, len(keys) - 1

    while max_index >= min_index:
        mid_index = (max_index + min_index) // 2
        if keys[mid_index] == query:
            return mid_index

        if keys[mid_index] < query:
            min_index = mid_index + 1
        else:
            max_index = mid_index - 1
    return -1


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
