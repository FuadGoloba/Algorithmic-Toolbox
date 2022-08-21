# Given the capacity of a backpack as well as the weights and prices of n different compounds, compute the maximum total price of items that fit into the backpack of the given capacity.
# Input: The capacity of a backpack W as well as the weights (w1; : : : ;wn) and prices (p1; : : : ;pn) of n different compounds.
# Output: The maximum total price of items that fit into the backpack of the given capacity: i.e., the maximum value of p1f1w1+  +pnfn wn such that u1 +    + un  W and 0  fi  1 for all i (fi is the fraction of the i-th item taken to the backpack).

from sys import stdin

def maximum_loot_value(capacity, weights, prices):
    """
        capacity : Capacity of backpack -> float
        weights : List of weights of items -> List
        prices : List of prices of items -> List
    """
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    total_items = len(weights)
    # First we compute the unit price per weight of each item and zip them with their index in a tuple
    unit_price_per_weight = [(prices[idx]/weights[idx], idx) for idx in range(total_items)]

    # We have to sort the List of tuple in descending order to have the most valuable item per weight
    sorted_price_per_weight = sorted(unit_price_per_weight, reverse=True)

    total_loot = 0

    # Loop through the sorted price per weight list
    for ppw, index in sorted_price_per_weight:
        # If we don't have the capacity to take the item, then we take as muchas we can and quit
        if capacity < weights[index]:
            total_loot += ppw * capacity
            break
        # If we do have capacity, we take all of the item
        total_loot += prices[index]
        # Update the capacity
        capacity -= weights[index]
        # Check that we aren't out of capacity
        if capacity == 0:
            break
    return total_loot

if __name__ == '__main__':

    x = input("Enter Capacity of backpack :")
    y = input("Enter each weight of items :")
    z = input("Enter each price of item :")

    capacity = float(x)
    weights = list(map(float, y.split()))
    prices = list(map(float, z.split()))

    optimal_loot = maximum_loot_value(capacity, weights, prices)
    print(optimal_loot)
