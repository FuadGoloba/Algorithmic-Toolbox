# Primitive Calculator Problem - You are given a calculator that only performs the following three operations with an integer x: add 1 to x, multiply x by 2, or multiply x by 3.
#   Given a positive integer n, your goal is to find the minimum number of operations needed to obtain n starting from the number 1. Note: A greedy algorithm approach might solve this leading to a local optima and not a global optima
# Therefore, With Dynamic Programmimg, we can achieve an optimal solution

# Problem; Find the minimum number of operations needed to get a positive integer n from 1 using only three operations: add 1, multiply by 2, and multiply by 3.
#   Input: An integer n.
#   Output: on the first line; The minimum number of operations “+1”, “x2”, and “x3” needed to get n from 1. In the second line, output a sequence of intermediate numbers that use operation

def DPprimitiveCalculator(number):
    '''
        Recursively with the help of memoization, the minimum number of operations can be calculated thus; 
            min_ops(n) = minimum( min_ops(n-1) + 1, min_ops(n//2) + 2 , min_ops(n//3) + 3 )
            
        But then since Dynamic Programming approach aims to optimise recursive solutions, We can choose to solve the problem bottom up (i.e solving from 1 to n) => O(n)
        We know that min_ops(1) = 0; min_ops(2) = 1,; min_ops(3) = 1; Therefore we can use these to compute the min_ops(n) such that n > 3
    '''
    
    MinOps = [float("inf")] * (number + 1) # An array the length of number
    if number == 1:
        MinOps[1] = 0
    elif number == 2:
        MinOps[2] = 1
    elif number == 3:
        MinOps[3] = 1
    else:
        MinOps[0], MinOps[1], MinOps[2], MinOps[3] = 0,0,1,1
        # Taking any number > 3; minimum operatiosn to reach number is the minimum of the following 3
        for n in range(4, number + 1):
            # Whatever is the minimum ops to reach (number - 1); we can add 1 to the operations count to get the number
            MinOps[n] = MinOps[n - 1] + 1 
            # If we consider making number from 1 using x3; We need to consider 3 cases and get the minimum; a. if number is divisible by 3, if number is not divisible by 3 but with a remainder of 1, and if number is not divisible by 3 but wiyth a remainder of 2
            MinOps[n] = min(MinOps[n], MinOps[n//3] + 1 if n % 3 == 0 else MinOps[(n-1)//3] + 2 if n % 3 == 1 else MinOps[(n-2)//3] + 3)
            # If we consider making number from 1 using x2; We need to consider 2 cases and get the minimum; a. if number is divisible by 2, if number is not divisible by 2 but with a remainder of 1
            MinOps[n] = min(MinOps[n], MinOps[n//2] + 1 if n % 2 == 0 else MinOps[(n-1)//2] + 2)
    
    result = MinOps[number] # Gives the minimum no of operations to reach number
    
    # Initialise a list to store sequence of intermediate numbers that lead to minimum operations
    sequence = []
    while number > 1:
        sequence.append(number)
        if MinOps[number - 1] == MinOps[number] - 1:
            number -= 1
        elif number % 2 == 0 and MinOps[number//2] == MinOps[number] - 1:
            number //= 2
        else:
            number = number // 3
            
    sequence.append(1)
    return (result, list(reversed(sequence))) # Returns the minimum no of operatiosn to reach number and the sequence of numbers that lead to the result


if __name__ == '__main__':
    input_n = int(input())
    minimum_ops, output_sequence = DPprimitiveCalculator(input_n)
    print(minimum_ops)
    print(*output_sequence)

