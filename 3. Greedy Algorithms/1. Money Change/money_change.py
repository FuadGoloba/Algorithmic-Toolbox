# Money Change Problem
# Compute the minimum number of coins needed to change the given value into coins with denominations 1, 5, and 10.
    # Input: An integer money.
    # Output: The minimum number of coins with denominations 1, 5, and 10 that changes money.

# Example :
            # Input: 28
            # Output: 6
            # Solution : 28 = 10 + 10 + 5 + 1 + 1 + 1.

def money_change(money):
    assert 0 <= money <= 10 ** 3

    num_of_coins = 0
    # While the change isn't 0, keep taking a coin with the largest denomination that does not exceed money, subtract it's value from money and increment the count of coins
    while money > 0:
        if money >= 10:
            money -= 10
        elif money >= 5:
            money -= 5
        elif money >= 1:
            money -= 1
        num_of_coins += 1
    return num_of_coins

def money_change2(money):
    assert 0 <= money <= 10 ** 3

    return (money // 10 + (money % 10) // 5 + (money % 5))


if __name__ == '__main__':
    input_n = int(input())
    print(money_change(input_n))