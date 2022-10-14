# Maximum Amount of Gold Problem
# Given a set of gold bars of various weights and a backpack that can hold at most W pounds, place as much gold as possible into the backpack.
#   Input: A set of n gold bars of integer weights w1...wn and a backpack that can hold at most W pounds.
#   Output: A subset of gold bars of maximum total weight not exceeding W.

# This problem is the Knapsack Problem without Repetition (Which is different from the Fractional Knapsack problem solved using Greedy Approach)
#       Greey Algorithm will not guarantee an optimal solution for the Discrete Knapsack problem, Hence the use of Dynamic Programming

from sys import stdin

def maximum_gold(capacity, weights):
    # assert 1 <= capacity <= 10 ** 4
    # assert 1 <= len(weights) <= 10 ** 3
    # assert all(1 <= w <= 10 ** 5 for w in weights)
    
    '''
        capacity : Total capacity W of the backpack
        weights : list of weights of gold bars
    '''

    Capacity_dict = {} # Dictionary to map each knapsack capacity to it's maximum value of gold it can contain
    bars = [0] + weights # include a weight of 0 to the list of gold bars
    
    # Loop through each gold bar and initialise a value of 0 for a backpack with 0 capacity
    for i in range(len(bars)):
        Capacity_dict[(0, i)] = 0
    
    # Loop through the capacity from 1 and initialise a value of 0 if there are no gold bars to pack
    for c in range(capacity + 1):
        Capacity_dict[(c, 0)] = 0

    for bar in range(1, len(bars)):
        for c in range(1, capacity + 1):
            # If the last gold bar was not included in the current backpack capacity, (i.e all other items except last gold bar is packed
            Capacity_dict[(c, bar)] = Capacity_dict[(c, bar - 1)]
            # The current capacity uses the last gold bar
            if bars[bar] <= c:
                val = Capacity_dict[(c - bars[bar], bar - 1)] + bars[bar]
                if Capacity_dict[(c, bar)] < val:
                    Capacity_dict[(c, bar)] = val
                #Capacity_dict[(c, bar)] = max(Capacity_dict[(c - bars[bar], bar - 1)] + bars[bar], Capacity_dict[(c, bar - 1)])
    
    # return the maximum amount of gold the backpack capacity can handle
    return Capacity_dict[(capacity, len(weights))]

if __name__ == '__main__':
    inputs1 = list(map(int, input().split()))
    input_capacity = inputs1[0]
    n = inputs1[1]
    input_weights = list(map(int, input().split()))
    print(maximum_gold(input_capacity, input_weights))
