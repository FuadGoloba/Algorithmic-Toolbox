# Money Change Again Problem
# Compute the minimum number of coins needed to change the given value into coins with denominations 1, 3, and 4.
#           Input: An integer money.
#           Output: The minimum number of coins with denominations 1, 3, and 4 that changes money.

# As we already know, a natural greedy strategy for the change problem does not work correctly for any set of denominations. 
# For example, if the available denominations are 1, 3, and 4, the greedy algorithm will change 6 cents using three coins (4 + 1 + 1) while it can be changed using just two coins (3 + 3).


def DPmoneyChange_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins

#------------------------------------------------------------- Optimised Solution - O(nm)

def DPmoneyChange(money, coins):

    # Create an array to store minimum number of coins to change money from 0 up until money
    MinNumCoins = [money + 1] * (money + 1)

    # Min number of coins to change 0 cents is 0
    MinNumCoins[0] = 0
    # Go through entire cent in noney and get the minimum of number of coins that can change money using previous money calculated
    for m in range(1, money + 1):
        for coin in coins:
            if m >= coin:
                NumCoins = MinNumCoins[m - coin] + 1
                if NumCoins < MinNumCoins[m]:
                    MinNumCoins[m] = NumCoins

    return MinNumCoins[money]

if __name__ == '__main__':                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    input_money = int(input())
    input_coins = list(map(int,input().split()))


    print(DPmoneyChange(input_money, input_coins))