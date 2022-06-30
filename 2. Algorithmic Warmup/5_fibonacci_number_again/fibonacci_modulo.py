# implementing a naive algorithm that computes the n-th fibonacci modulo m; Given two integers 0<=n<=10**18; and 2<=m<=10**3
# Note: As n gets larger, the algoritgms gets slower : O(n)

def fibonacci_nth_modulo_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for i in range(n - 1): 
        previous, current = current, (previous + current) % m
    return current



# implementing a fast algorithm that computes the n-th fibonacci modulo m; Given two integers 0<=n<=10**18; and 2<=m<=10**3
# An intreresting property of nth-fibonacci modulo m is; for any integer m >= 2, the sequence of n-th fibonacci modulo m is periodic.
# The period always starts with 01 and is known as PISANO period (Pisano is another name for Fibonacci)

# To implement this algorithm, first we need to compute the Pisano period of n; This would reduce the number of iterations to O(logn)

def get_pisano_period(m):
    a = 0 
    b =  1
    c = a + b
    for i in range(m * m):
        c = (a + b) % m
        a = b
        b = c
        if a == 0 and b == 1:
            return i + 1

def fibonacci_nth_modulo_fast(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    pisano_period = get_pisano_period(m) # Get pisano period of m
    
    n = n % pisano_period # Get the remainer of n  divided by pisano length to update n; reducing the number of iterations
    if n <= 1:
        return n

    previous, current = 0, 1
    for i in range(n - 1):
        previous, current = current, previous + current

    return current % m

if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_nth_modulo_fast(input_n, input_m))