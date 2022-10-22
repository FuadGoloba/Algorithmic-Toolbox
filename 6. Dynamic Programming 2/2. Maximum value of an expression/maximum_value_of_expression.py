# Maximum Value of an Arithmetic Expression Problem   ---  Parenthesize an arithmetic expression to maximize its value.
#   Input: An arithmetic expression consisting of digits as well as plus, minus, and multiplication signs.
#   Output: Add parentheses to the expression in order to maximize its value.

# For example, for an expression (3 + 2 x 4) there are two ways of parenthesizing it: (3 + (2 x 4)) = 11 and ((3 + 2) x 4) = 20.

import operator

operations = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
}

def MinAndMax(i, j, m, M, operation):
    mini = float('+inf')
    maxi = float('-inf')
    
    for k in range(i, j):
        a = operations[operation[k - 1]](M[i][k], M[k+1][j])
        b = operations[operation[k - 1]](M[i][k], m[k+1][j])
        c = operations[operation[k - 1]](m[i][k], M[k + 1][j])
        d = operations[operation[k - 1]](m[i][k], m[k + 1][j])
        
        mini = min(mini, a, b, c, d)
        maxi = max(maxi, a, b, c, d)
        
    return mini, maxi


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29
    
    n = len(dataset)
    m = [[0] * (n + 1) for _ in range(n + 1)]
    M = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        m[i][i] = dataset[i - 1]
        M[i][i] = dataset[i - 1]
    
    for s in range(1, n):
        for i in  range(1, n + 1 - s):
            j =  i + s
            m[i][j], M[i][j] = MinAndMax(i, j, m, M, operation)
            
    return int(M[1][n])


if __name__ == "__main__":
    expression = input()
    n = len(expression)
    dataset = [int(expression[i]) for  i in range(0, n + 1, 2)]
    operation = [expression[i] for i  in range(1, n, 2)]
    print(find_maximum_value(dataset)) 